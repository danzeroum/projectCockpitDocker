"""Mordidas da catraca da ingestão (CP-003 / ci/catraca.py).

A pergunta que estes testes protegem: *um repositório que nasce vermelho de propósito consegue
distinguir "vermelho declarado" de "vermelho esquecido"?* Sem catraca não consegue — e o modo de
falha não é teórico: dentro de um CI que já está vermelho, um achado novo é invisível.

O núcleo (`comparar`, `nao_regrediu`) é puro, então cada cenário é uma chamada de função. Medir o
repositório é outra pergunta, e mora na camada de I/O.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(RAIZ / "ci"))

import catraca  # noqa: E402

BASE = {"meta:órfão": 133, "meta:regra": 24, "meta:teste órfão": 76}


def test_igual_ao_baseline_segura():
    """O caso comum: um PR que não mexe no contador atravessa."""
    assert catraca.comparar(atual=dict(BASE), baseline=dict(BASE)).segurou is True


def test_UM_ORFAO_NOVO_reprova():
    """O cenário que motiva a catraca. Um teste novo sem componente sobe `teste órfão` em 1 —
    e, num CI já vermelho, ninguém veria."""
    atual = dict(BASE); atual["meta:teste órfão"] += 1
    v = catraca.comparar(atual=atual, baseline=dict(BASE))
    assert v.segurou is False
    assert v.subiram == (("meta:teste órfão", 76, 77),)
    assert "SUBIDA" in " ".join(v.motivos)


def test_CONTAGEM_IGUAL_com_CATEGORIA_TROCADA_reprova():
    """A borda que um contador de total deixaria passar.

    Trocar dez órfãos por dez regras quebradas mantém o total em 233 e muda o PROBLEMA. Uma
    catraca que olhasse só o número diria "não subiu" — e estaria certa sobre a aritmética e
    errada sobre o repositório.
    """
    atual = {"meta:órfão": 123, "meta:regra": 24, "meta:teste órfão": 76, "meta:REQ": 10}
    assert sum(atual.values()) == sum(BASE.values())
    v = catraca.comparar(atual=atual, baseline=dict(BASE))
    assert v.segurou is False
    assert v.novas == (("meta:REQ", 10),)
    assert "CATEGORIA NOVA" in " ".join(v.motivos)


def test_categoria_nova_reprova_mesmo_com_total_MENOR():
    """E a versão mais tentadora dela: o total caiu, e ainda assim recusa."""
    atual = {"meta:órfão": 10, "governance:stage_partition": 1}
    assert sum(atual.values()) < sum(BASE.values())
    assert catraca.comparar(atual=atual, baseline=dict(BASE)).segurou is False


def test_descida_NAO_e_silenciosa_exige_regravar():
    """Descer é o esperado — e ainda assim não passa sem regravar.

    Não é rigor gratuito. Se a descida passasse calada, o baseline ficaria alto para sempre: o PR
    seguinte poderia subir de volta até ele sem a catraca girar. É o diff do baseline, no PR, que
    registra que ela girou.
    """
    atual = dict(BASE); atual["meta:órfão"] = 100
    v = catraca.comparar(atual=atual, baseline=dict(BASE))
    assert v.segurou is False
    assert v.desceram == (("meta:órfão", 133, 100),)
    assert "DESCEU" in " ".join(v.motivos)
    assert "--gravar" in " ".join(v.motivos), "a mensagem tem de dizer como girar a catraca"


def test_categoria_ZERADA_conta_como_descida():
    """Sumir do atual é descer até zero — o melhor caso, e mesmo assim regrava: um baseline que
    lista categoria inexistente descreve outro repositório."""
    atual = {"meta:regra": 24, "meta:teste órfão": 76}
    v = catraca.comparar(atual=atual, baseline=dict(BASE))
    assert ("meta:órfão", 133, 0) in v.desceram


def test_REGRAVAR_PARA_CIMA_e_recusado_contra_a_BASE():
    """O buraco que a comparação com o próprio baseline deixaria aberto.

    Bastaria subir o contador E regravar o baseline no mesmo PR: `comparar` ficaria feliz, porque
    o arquivo passaria a descrever fielmente um repositório pior. Por isso o workflow busca o
    baseline da branch BASE e confere contra ele.
    """
    anterior = dict(BASE)
    novo = dict(BASE); novo["meta:órfão"] = 140
    ruins = catraca.nao_regrediu(novo=novo, anterior=anterior)
    assert ruins and "eleva" in ruins[0]


def test_baseline_do_PR_nao_pode_inventar_categoria():
    novo = dict(BASE); novo["meta:inventada"] = 1
    ruins = catraca.nao_regrediu(novo=novo, anterior=dict(BASE))
    assert ruins and "inventa" in ruins[0]


def test_descer_o_baseline_e_sempre_permitido():
    novo = {"meta:órfão": 0, "meta:regra": 24, "meta:teste órfão": 76}
    assert catraca.nao_regrediu(novo=novo, anterior=dict(BASE)) == []


# --------------------------------------------------------------------------------------
# O baseline REAL na árvore — a catraca vale sobre este repositório, não sobre fixtures
# --------------------------------------------------------------------------------------

def test_o_baseline_gravado_existe_e_descreve_este_repositorio():
    """Sem arquivo não há catraca, só vermelho. E o total tem de ser a soma das categorias —
    um `total` escrito à mão divergiria em silêncio no primeiro PR."""
    doc = json.loads((RAIZ / catraca.BASELINE).read_text(encoding="utf-8"))
    por_cat = doc["por_categoria"]
    assert por_cat, "baseline vazio não segura nada"
    assert doc["total"] == sum(por_cat.values())
    assert all(isinstance(v, int) and v >= 0 for v in por_cat.values())


def test_o_baseline_ainda_bate_com_a_medicao():
    """O teste que faz a catraca ser catraca: se este falhar, ou o repositório mudou e o baseline
    não foi regravado, ou o baseline foi regravado sem o repositório mudar."""
    doc = json.loads((RAIZ / catraca.BASELINE).read_text(encoding="utf-8"))
    v = catraca.comparar(atual=catraca.medir(), baseline=doc["por_categoria"])
    assert v.segurou, "\n".join(v.motivos)

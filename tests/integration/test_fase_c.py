"""O modo `active_discovery` faz o que o nome diz? — a pergunta que ninguém tinha feito.

Este arquivo existe por causa de um defeito que passou despercebido porque cada
peça, sozinha, estava certa: a cerimônia de autorização era impecável (disparo
humano, `confirmo`, `environment: production` com revisores, escopo vindo de
segredo) e protegia um run que **não emitia probe nenhum** — `pytest -m "seguranca
and not load"`, um subconjunto do que a auditoria passiva já roda.

É o mesmo modo de errar que apareceu cinco vezes no produto auditado: a peça
construída, o teste lendo a peça, e o fio nunca ligado. Aqui o fio é o
`webqa.sondagem`, único consumidor de `WEBQA_DISCOVERY_AUTHORIZED` — nenhum
arquivo em `checks/` lê esse gate.

Os testes abaixo verificam a ligação lendo o workflow. O que eles NÃO conseguem
provar é que a régua aceita o escopo traduzido: isso depende de a régua estar
instalada, e por isso o caso correspondente pula quando ela não está — dizendo
por quê, em vez de passar em silêncio.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest
import yaml

QA = ".github/workflows/qa.yml"


@pytest.fixture(scope="module")
def passo_segregado(request) -> str:
    doc = yaml.safe_load((Path(request.config.rootpath) / QA).read_text(encoding="utf-8"))
    passos = doc["jobs"]["segregated-load-or-active"]["steps"]
    corrida = [p for p in passos if p.get("name") == "Rodar modo segregado"]
    assert corrida, "o passo que roda o modo segregado sumiu"
    return corrida[0]["run"]


@pytest.fixture(scope="module")
def passo_passivo(request) -> str:
    doc = yaml.safe_load((Path(request.config.rootpath) / QA).read_text(encoding="utf-8"))
    passos = doc["jobs"]["inventory-and-passive"]["steps"]
    corrida = [p for p in passos if str(p.get("name", "")).startswith("Auditoria passiva")]
    assert corrida, "o passo de auditoria passiva sumiu"
    return corrida[0]["run"]


# ---------------------------------------------------------------------------
# 1. active_discovery precisa DESCOBRIR
# ---------------------------------------------------------------------------

def test_o_modo_ativo_invoca_a_sondagem(passo_segregado: str):
    """Sem esta linha, todo o resto do job é cerimônia em volta de nada."""
    assert "webqa.sondagem" in passo_segregado, (
        "active_discovery não chama a sondagem — o modo tem o nome da coisa e não faz a coisa")
    assert "--executar" in passo_segregado, (
        "sem --executar a sondagem só planeja: o padrão da régua é dry-run")


def test_o_modo_ativo_nao_e_um_repeteco_do_passivo(passo_segregado: str):
    """`pytest -m "seguranca ..."` era o que ele fazia, e a auditoria passiva já roda
    a mesma família. Repetir não é descobrir."""
    assert 'pytest -m "seguranca' not in passo_segregado


def test_a_sondagem_recebe_o_escopo_traduzido(passo_segregado: str):
    """Os dois `escopo-autorizado.yaml` têm schemas incompatíveis. O `cp` anterior
    entregava um arquivo que `webqa.escopo.carregar` recusa com "escopo sem alvos
    declarados" — e isso nunca apareceu porque a sondagem nunca era chamada."""
    assert "escopo-regua" in passo_segregado, "sem tradução, a régua não lê nosso escopo"
    assert "cp tests/qa/escopo-autorizado.yaml" not in passo_segregado, (
        "o cp direto voltou: o schema do consumidor não é o schema da régua")


def test_o_veredito_e_nosso(passo_segregado: str):
    """`webqa.sondagem` sai 0 mesmo com `inconclusivo: true` no laudo. Confiar no
    código de saída dela faria um alvo fora do ar passar como alvo limpo."""
    assert "cockpit_harness veredito" in passo_segregado


def test_a_evidencia_da_fase_c_e_arquivada(request):
    doc = yaml.safe_load((Path(request.config.rootpath) / QA).read_text(encoding="utf-8"))
    passos = doc["jobs"]["segregated-load-or-active"]["steps"]
    upload = [p for p in passos if str(p.get("uses", "")).startswith("actions/upload-artifact")]
    assert upload, "o run que mais precisa de evidência era o único que não a arquivava"


def test_o_modo_de_carga_continua_por_marcador(passo_segregado: str):
    """A correção é do `active_discovery`. `load` roda por marcador porque é assim que
    a régua o expõe — mexer nele aqui seria consertar o que não estava quebrado."""
    assert "pytest -m load" in passo_segregado


# ---------------------------------------------------------------------------
# 2. a expressão do passivo não pode esvaziar uma família em silêncio
# ---------------------------------------------------------------------------

def test_o_passivo_instala_navegador(passo_passivo: str):
    """Os 16 checks de `seguranca` são todos `browser`. Com `not browser` fixo, a
    expressão nomeava cinco famílias e media quatro."""
    assert "playwright install" in passo_passivo


def test_o_passivo_guarda_contra_familia_vazia(passo_passivo: str):
    """A guarda é o que impede o defeito de voltar por outro filtro. Foi um
    `and not browser` que zerou `seguranca`; o próximo pode ser outra coisa."""
    assert "--collect-only" in passo_passivo
    assert "não coletam teste nenhum" in passo_passivo


def test_o_fallback_diz_o_que_deixou_de_medir(passo_passivo: str):
    """Se o navegador não instalar, o run segue — mas nomeando o buraco. Verde sobre
    quatro famílias quando cinco foram prometidas é o defeito, não o alívio."""
    assert "::warning::" in passo_passivo and "seguranca" in passo_passivo


def test_a_expressao_nasce_da_lista_de_prometidas(passo_passivo: str):
    """A expressão é DERIVADA do que o run pode medir, e não uma constante ao lado dela.

    Com as duas separadas, o fallback tirava `seguranca` do filtro e a deixava na
    expressão — voltando ao defeito por dentro da própria correção. Foi a guarda que
    pegou isso, o que já é uma medição a favor dela.
    """
    assert "$EXPRESSAO" in passo_passivo and "$PROMETIDAS" in passo_passivo
    assert 'pytest -m "(backend or frontend or ux or seguranca or lgpd) and not load and not browser"' \
        not in passo_passivo, "a expressão antiga, que nomeava seguranca e a descartava, voltou"


# ---------------------------------------------------------------------------
# 3. a régua aceita o que traduzimos (só com a régua instalada)
# ---------------------------------------------------------------------------

def _regua_disponivel():
    try:
        import webqa.escopo  # noqa: F401
    except ImportError:
        return False
    return True


@pytest.mark.skipif(not _regua_disponivel(),
                    reason="régua não instalada — a tradução é verificada, não validada")
def test_a_regua_aceita_o_escopo_traduzido(tmp_path, request):
    """A única prova que importa de verdade: o arquivo traduzido passa pelo loader
    REAL da régua, com todas as validações dela (autor não-vazio, evidência
    não-vazia, data não-futura, origem canônica, https obrigatório)."""
    from webqa import escopo as escopo_regua_externa

    from cockpit_harness import contrato, escopo_regua

    shutil.copytree(request.config.rootpath / "tests" / "qa", tmp_path / "tests" / "qa")
    shutil.copy(request.config.rootpath / "requirements-qa.txt", tmp_path / "requirements-qa.txt")

    config = yaml.safe_load((tmp_path / "tests/qa/config.yaml").read_text(encoding="utf-8"))
    config["target"]["base_url"] = "https://homolog.exemplo.test"
    (tmp_path / "tests/qa/config.yaml").write_text(yaml.safe_dump(config), encoding="utf-8")
    (tmp_path / "tests/qa/escopo-autorizado.yaml").write_text(yaml.safe_dump({
        "authorized": True,
        "authorized_by": "danzeroum",
        "authorized_on": "2026-08-01",
        "evidence": "pr#1",
        "scope": {"hosts": ["homolog.exemplo.test"]},
        "proof_of_possession": {"method": "file", "reference": "arquivo"},
        "authorization_expires": "2099-12-31",
    }), encoding="utf-8")

    destino = escopo_regua.escrever(contrato.situacao(tmp_path), tmp_path / "escopo-regua.yaml")
    carregado = escopo_regua_externa.carregar(destino)

    assert [e.origem for e in carregado.entradas] == ["https://homolog.exemplo.test"]
    assert carregado.esta_no_escopo("https://homolog.exemplo.test/qualquer/caminho")
    assert not carregado.esta_no_escopo("https://docker.danzeroum.com/")

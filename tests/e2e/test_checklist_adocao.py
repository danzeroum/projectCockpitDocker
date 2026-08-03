"""Aceitação — o checklist de "pronto" do playbook, item por item, executável.

`docs/COMO-ADOTAR.md` do molde termina com uma lista de caixas a marcar. Enquanto ela for prosa,
marcar a caixa é opinião. Aqui cada caixa vira uma asserção: se alguém desfizer a adoção — copiar
a régua "para simplificar", trocar o pin por faixa, comitar o escopo real, apontar a auditoria
para produção — o inventário reprova antes da revisão humana.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from cockpit_harness import contrato, procedencia

LAUDO = "docs/laudo-adocao.json"


# [ ] webqa/, checks/, data/caminhos-sensiveis.yaml ausentes no REPO_ALVO
@pytest.mark.parametrize("proibido", contrato.CAMINHOS_PROIBIDOS)
def test_a_regua_nao_foi_copiada(raiz: Path, proibido: str):
    assert not (raiz / proibido).exists()


# [ ] requirements-qa.txt pina a régua na versão exata; standard_version casa
def test_pin_exato_e_espelho_casam(raiz: Path):
    assert contrato.versao_pinada(raiz) == contrato.versao_espelhada(raiz)


# [ ] config.yaml aponta para um alvo de HOMOLOGAÇÃO
def test_alvo_de_homologacao_ou_pendencia_declarada(raiz: Path):
    """Sem URL de homologação, a saída correta é INCOMPLETE:target_url — não produção.

    O Docker Cockpit publicado é produção (docker.danzeroum.com). Apontar a auditoria para lá
    porque "era a URL que existia" é o acidente que o escopo autorizado previne. Enquanto não
    houver homologação declarada, este teste exige a PENDÊNCIA, não um alvo qualquer.
    """
    alvo = contrato.alvo_declarado(raiz)
    if alvo is None:
        assert contrato.situacao(raiz).pendencias[0] == "INCOMPLETE:target_url"
    else:
        assert contrato.ambiente_do_alvo(raiz) != "production"


def test_producao_nunca_e_o_alvo_declarado(raiz: Path):
    bruto = (raiz / contrato.CONFIG_QA).read_text(encoding="utf-8")
    assert "base_url: \"https://docker.danzeroum.com\"" not in bruto


# [ ] escopo-autorizado.yaml real NÃO comitado (só o .example)
def test_segredo_nao_comitado(raiz: Path):
    assert not (raiz / contrato.ESCOPO_QA).exists()
    assert (raiz / f"{contrato.ESCOPO_QA}.example").exists()
    assert contrato.ESCOPO_QA in (raiz / ".gitignore").read_text(encoding="utf-8")


# [ ] load/active_discovery só em workflow_dispatch; ambiente do agente sem WEBQA_*
def test_modo_pesado_nunca_e_automatico(raiz: Path):
    qa = (raiz / ".github/workflows/qa.yml").read_text(encoding="utf-8")
    antes_do_dispatch, _, depois = qa.partition("segregated-load-or-active")
    assert "WEBQA_LOAD_AUTHORIZED" not in antes_do_dispatch
    assert "WEBQA_DISCOVERY_AUTHORIZED" not in antes_do_dispatch
    assert "WEBQA_LOAD_AUTHORIZED" in depois


# [ ] a casca mínima existe
@pytest.mark.parametrize(
    "caminho",
    [
        "harness/harness.yaml",
        "tests/qa/config.yaml",
        "tests/qa/campanha.yaml",
        "requirements-qa.txt",
        ".github/workflows/qa.yml",
        "WEBQA_CONSUMER_CONTRACT.md",
    ],
)
def test_casca_minima_presente(raiz: Path, caminho: str):
    assert (raiz / caminho).exists()


# [ ] PR com laudo carimbando a procedência
def test_laudo_da_adocao_esta_commitado_e_valido(raiz: Path):
    laudo = json.loads((raiz / LAUDO).read_text(encoding="utf-8"))
    procedencia.validar(laudo, raiz / "harness" / "schemas")


def test_laudo_carimba_a_regua_declarada(raiz: Path):
    """O laudo é artefato DERIVADO: sua versão tem de casar com a fonte única, ou está velho."""
    laudo = json.loads((raiz / LAUDO).read_text(encoding="utf-8"))
    assert laudo["standard"]["version"] == contrato.versao_pinada(raiz)
    assert laudo["standard"]["name"] == "webqa-suite"
    assert len(laudo["standard"]["commit"]) == 40
    assert laudo["standard"]["sensitive_paths_hash"].startswith("sha256:")


def test_laudo_prova_que_nenhuma_rede_foi_tocada(raiz: Path):
    laudo = json.loads((raiz / LAUDO).read_text(encoding="utf-8"))
    assert laudo["execution"]["mode"] == "inventory"
    assert laudo["execution"]["network_used"] is False
    assert laudo["execution"]["active_gates"] == []
    assert "INCOMPLETE:target_url" in laudo["summary"]["pendencias"]

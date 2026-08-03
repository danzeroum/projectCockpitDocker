"""Integração — o repositório REAL, lido pelos módulos reais.

Se o teste de unidade prova que a trava morde quando acionada, este aqui prova que ela está
instalada neste repositório: o pin é exato, o espelho casa, a fronteira da régua está intacta e
o plano de controle declara a matriz de modos que o contrato exige.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator

from cockpit_harness import contrato, plano


def test_fonte_unica_da_versao(raiz: Path):
    """O número mora só em requirements-qa.txt; config.yaml é o único espelho tolerado."""
    assert contrato.conferir_fonte_unica(raiz) == contrato.versao_pinada(raiz)


def test_fronteira_da_regua_intacta(raiz: Path):
    assert contrato.regua_copiada(raiz) == []


def test_escopo_real_nao_esta_comitado(raiz: Path):
    """Invariante 4: o segredo não se comita — só o .example vive versionado."""
    assert not (raiz / contrato.ESCOPO_QA).exists()
    assert (raiz / f"{contrato.ESCOPO_QA}.example").exists()
    assert contrato.ESCOPO_QA in (raiz / ".gitignore").read_text(encoding="utf-8")


def test_harness_yaml_valida_contra_o_proprio_schema(raiz: Path):
    schema = json.loads((raiz / "harness/schemas/harness.schema.json").read_text(encoding="utf-8"))
    erros = list(Draft202012Validator(schema).iter_errors(plano.carregar(raiz)))
    assert erros == [], [e.message for e in erros]


@pytest.mark.parametrize("modo", ["inventory", "passive", "load", "active_discovery"])
def test_os_quatro_modos_estao_declarados(raiz: Path, modo: str):
    assert modo in plano.modos(plano.carregar(raiz))


@pytest.mark.parametrize("modo", ["load", "active_discovery"])
def test_modo_pesado_e_segregado_e_humano(raiz: Path, modo: str):
    declarado = plano.modos(plano.carregar(raiz))[modo]
    assert declarado["agent_may_trigger"] is False
    assert declarado["job"] == "segregated"
    assert declarado.get("trigger") == "human_only"


def test_agente_nao_dispara_modo_pesado_no_plano_real(raiz: Path):
    controle = plano.carregar(raiz)
    assert plano.pode_disparar(controle, "load", "agent") is False
    assert plano.pode_disparar(controle, "active_discovery", "agent") is False
    assert plano.pode_disparar(controle, "inventory", "agent") is True


def test_denylist_de_ambiente_esta_ligado(raiz: Path):
    higiene = plano.carregar(raiz)["env_hygiene"]
    assert "WEBQA_" in higiene["env_denylist_prefix"]
    assert higiene["fail_on_denied_env"] is True


def test_caminhos_protegidos_cobrem_o_que_muda_a_regua(raiz: Path):
    protegidos = plano.carregar(raiz)["repository"]["protected_paths"]
    for esperado in ("requirements-qa.txt", "harness/", ".github/", contrato.ESCOPO_QA):
        assert esperado in protegidos


def test_plano_referencia_o_arquivo_de_pin_sem_restatar_a_versao(raiz: Path):
    """harness.yaml aponta para requirements-qa.txt; se restatasse o número, seriam duas fontes."""
    bruto = (raiz / plano.HARNESS_YAML).read_text(encoding="utf-8")
    assert "requirements-qa.txt" in bruto
    assert contrato.versao_pinada(raiz) not in bruto


def test_campanha_nao_agenda_modo_pesado(raiz: Path):
    campanha = yaml.safe_load((raiz / "tests/qa/campanha.yaml").read_text(encoding="utf-8"))
    assert set(campanha["modes"]).isdisjoint({"load", "active_discovery"})


def test_todos_os_schemas_sao_json_schema_validos(raiz: Path):
    for arquivo in sorted((raiz / "harness/schemas").glob("*.json")):
        Draft202012Validator.check_schema(json.loads(arquivo.read_text(encoding="utf-8")))

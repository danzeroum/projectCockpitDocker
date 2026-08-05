"""Integração — a enforcement mora no CI, então o CI é objeto de teste.

A harness é declarativa; quem recusa de fato é o workflow. Um `qa.yml` que rodasse carga no push
tornaria a declaração de `harness.yaml` decorativa — e ninguém perceberia, porque o YAML "passa".
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

QA = ".github/workflows/qa.yml"
META = ".github/workflows/validate-metadata.yml"


@pytest.fixture(scope="module")
def qa(request) -> dict:
    raiz = Path(request.config.rootpath)
    return yaml.safe_load((raiz / QA).read_text(encoding="utf-8"))


def _job(doc: dict, nome: str) -> dict:
    return doc["jobs"][nome]


def test_qa_roda_em_push_e_pull_request(qa: dict):
    # PyYAML lê a chave `on:` como booleano True — daí a busca pelas duas formas.
    gatilhos = qa.get("on", qa.get(True))
    assert "push" in gatilhos and "pull_request" in gatilhos
    assert "workflow_dispatch" in gatilhos


def test_modo_pesado_so_existe_por_workflow_dispatch(qa: dict):
    gatilhos = qa.get("on", qa.get(True))
    opcoes = gatilhos["workflow_dispatch"]["inputs"]["mode"]["options"]
    assert sorted(opcoes) == ["active_discovery", "load"]


def test_job_automatico_se_exclui_do_dispatch(qa: dict):
    assert _job(qa, "inventory-and-passive")["if"] == "github.event_name != 'workflow_dispatch'"


def test_job_segregado_so_roda_no_dispatch_e_exige_ambiente(qa: dict):
    segregado = _job(qa, "segregated-load-or-active")
    assert segregado["if"] == "github.event_name == 'workflow_dispatch'"
    assert segregado["environment"] == "production"


def test_job_automatico_nao_monta_gate_de_modo_pesado(qa: dict):
    """O gate WEBQA_* só é montado no job segregado. No automático, nem como env de passo."""
    bruto = str(_job(qa, "inventory-and-passive"))
    assert "WEBQA_LOAD_AUTHORIZED" not in bruto
    assert "WEBQA_DISCOVERY_AUTHORIZED" not in bruto


def test_job_automatico_guarda_a_fronteira_da_regua(qa: dict):
    passos = _job(qa, "inventory-and-passive")["steps"]
    guarda = [p for p in passos if "Recusar régua copiada" in p.get("name", "")]
    assert guarda, "o passo que recusa webqa/, checks/ e data/caminhos-sensiveis.yaml sumiu"
    assert "data/caminhos-sensiveis.yaml" in guarda[0]["run"]


def test_job_automatico_exige_pin_exato(qa: dict):
    passos = _job(qa, "inventory-and-passive")["steps"]
    assert any("Exigir pin exato" in p.get("name", "") for p in passos)


def test_job_automatico_roda_o_inventario(qa: dict):
    passos = _job(qa, "inventory-and-passive")["steps"]
    assert any("pytest" in str(p.get("run", "")) for p in passos)


def test_job_segregado_exige_confirmacao_humana(qa: dict):
    passos = _job(qa, "segregated-load-or-active")["steps"]
    assert any("confirmo" in str(p.get("run", "")) for p in passos)


def test_fiscal_de_metadados_roda_no_ci(request):
    """REANCORADO na fatia-3: o teste exigia a string `ci/validate_metadata.py` no workflow, e a
    carcaça v1.0.0 roda `ci/validate_all.py`, que chama aquele fiscal in-process junto dos outros
    oito.

    A promessa do ADR-002 é "regra que precisa morder tem fiscal EXECUTÁVEL, e ele roda no CI" —
    e ela continua verdadeira. O que estava errado era a âncora: presa à MENÇÃO de um comando em
    vez de ao FATO de o fiscal rodar. É a mesma classe de erro que eu cometi quatro vezes nesta
    migração, e reancorá-la aqui é fechá-la no caso que a originou.

    A âncora nova é o FATO: importar o módulo do fiscal e conferir que o comando que o workflow
    roda de fato o alcança. Se um dia `validate_all` deixar de chamá-lo, isto cai — e é isso que
    a asserção antiga não conseguia detectar, porque a string continuaria lá.
    """
    doc = yaml.safe_load((Path(request.config.rootpath) / META).read_text(encoding="utf-8"))
    comandos = " ".join(str(p.get("run", "")) for p in doc["jobs"]["validate-metadata"]["steps"])

    fiscal = next((c for c in ("ci/validate_all.py", "ci/validate_metadata.py") if c in comandos),
                  None)
    assert fiscal, f"nenhum fiscal de metadados roda no workflow: {comandos[:200]}"

    if fiscal == "ci/validate_all.py":
        fonte = (Path(request.config.rootpath) / "ci/validate_all.py").read_text(encoding="utf-8")
        assert "validate_metadata" in fonte, (
            "o workflow roda validate_all.py, que NÃO alcança validate_metadata — o fiscal saiu "
            "do caminho e a string no workflow não denunciaria")
        assert "generate_graph" in fonte, (
            "o workflow roda validate_all.py, que NÃO confere o grafo derivado — e o grafo em "
            "dia é o que impede docs/metadata-graph.md de virar ficção editada à mão")
    else:
        assert "ci/generate_graph.py --check" in comandos

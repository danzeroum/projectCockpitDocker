"""Unidade — procedência e comparabilidade do laudo (contrato §5 e §7).

O caso interessante não é o laudo que passa: é o par de laudos que NÃO deve ser comparado. Um
painel que soma dois laudos produzidos por réguas diferentes é preciso e mentiroso ao mesmo tempo.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

import pytest

from cockpit_harness import procedencia
from cockpit_harness.codigos import Codigo, NaoComparavel, ProcedenciaInvalida

SCHEMAS = Path(__file__).resolve().parents[2] / "harness" / "schemas"

REGUA = procedencia.Regua(
    name="webqa-suite",
    version="1.0.0",
    commit="090b7b4336e513a327d33713ea9bb2272262faa1",
    sensitive_paths_hash="sha256:" + "f" * 64,
)


def _laudo(**troca) -> dict:
    base = dict(
        regua=REGUA,
        repositorio="danzeroum/projectCockpitDocker",
        commit="a1b2c3d",
        run_id="2026-08-03T13-34-00Z",
        modo="inventory",
        runner_kind="ci",
        rede_usada=False,
    )
    base.update(troca)
    return procedencia.montar_laudo(**base)


def test_hash_da_lista_curada_tem_prefixo(tmp_path):
    lista = tmp_path / "caminhos-sensiveis.yaml"
    lista.write_text("- /.env\n", encoding="utf-8")
    assert procedencia.hash_lista_curada(lista).startswith("sha256:")


def test_hash_de_lista_inexistente_e_erro_30(tmp_path):
    with pytest.raises(ProcedenciaInvalida) as erro:
        procedencia.hash_lista_curada(tmp_path / "nao-existe.yaml")
    assert erro.value.codigo is Codigo.PROVENANCE_INVALID


def test_run_id_e_utc_e_ordenavel():
    momento = dt.datetime(2026, 8, 3, 13, 34, 0, tzinfo=dt.timezone.utc)
    assert procedencia.novo_run_id(momento) == "2026-08-03T13-34-00Z"


def test_laudo_valido_contra_o_schema():
    procedencia.validar(_laudo(), SCHEMAS)


def test_laudo_de_inventario_nao_usa_rede():
    laudo = _laudo()
    assert laudo["execution"]["network_used"] is False
    assert laudo["execution"]["active_gates"] == []


def test_regua_ausente_degrada_para_uninstalled():
    laudo = _laudo(regua=procedencia.Regua.ausente(), resultado="suite_not_installed")
    procedencia.validar(laudo, SCHEMAS)
    assert laudo["standard"]["version"] == "UNINSTALLED"


@pytest.mark.parametrize(
    "troca",
    [
        {"modo": "sondagem"},
        {"runner_kind": "robo"},
        {"resultado": "talvez"},
        {"resultado": "findings"},  # findings sem achados
    ],
)
def test_laudo_incoerente_e_recusado(troca):
    with pytest.raises(ProcedenciaInvalida):
        _laudo(**troca)


def test_achado_sem_result_findings_e_recusado():
    achado = ({"id": "X-1", "severity": "high", "dimension": "seguranca"},)
    with pytest.raises(ProcedenciaInvalida):
        _laudo(resultado="ok", achados=achado)


def test_laudo_sem_procedencia_falha_no_schema():
    laudo = _laudo()
    del laudo["standard"]["commit"]
    with pytest.raises(ProcedenciaInvalida):
        procedencia.validar(laudo, SCHEMAS)


def test_bloco_artifact_exige_bump_de_schema():
    """schema_version 1.0 não admite `artifact` — o campo novo obriga o bump para 1.1."""
    laudo = _laudo()
    laudo["artifact"] = {"kind": "laudo", "id": "x", "created_at": "2026-08-03T13:34:00Z"}
    with pytest.raises(ProcedenciaInvalida):
        procedencia.validar(laudo, SCHEMAS)


def test_laudos_da_mesma_regua_sao_comparaveis():
    assert procedencia.comparaveis(_laudo(), _laudo(run_id="2026-08-04T10-00-00Z"))


@pytest.mark.parametrize(
    "outra",
    [
        procedencia.Regua("webqa-suite", "1.1.0", REGUA.commit, REGUA.sensitive_paths_hash),
        procedencia.Regua("webqa-suite", "1.0.0", "outro-commit", REGUA.sensitive_paths_hash),
        procedencia.Regua("webqa-suite", "1.0.0", REGUA.commit, "sha256:" + "0" * 64),
    ],
    ids=["versão", "commit", "lista-curada-editada"],
)
def test_regua_diferente_torna_incomparavel(outra):
    """Mesma versão com hash de lista diferente = alguém editou a régua. Não é comparável."""
    with pytest.raises(NaoComparavel) as erro:
        procedencia.exigir_comparaveis(_laudo(), _laudo(regua=outra))
    assert erro.value.codigo is Codigo.NOT_COMPARABLE


def test_fingerprint_incompleta_e_erro_30():
    laudo = _laudo()
    laudo["standard"]["sensitive_paths_hash"] = ""
    with pytest.raises(ProcedenciaInvalida):
        procedencia.fingerprint(laudo)

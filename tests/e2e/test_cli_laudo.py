"""Sistema — a CLI de ponta a ponta, pelos códigos de saída do contrato §6.

Aqui não se inspeciona objeto nenhum: roda-se o processo como o CI roda e olha-se o código de
saída. É o nível em que "a trava morde" deixa de ser afirmação e vira observação.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from cockpit_harness.codigos import Codigo


def _cli(raiz: Path, *args: str, extra_env: dict[str, str] | None = None) -> subprocess.CompletedProcess:
    ambiente = {**os.environ, "PYTHONPATH": str(raiz / "src")}
    ambiente.update(extra_env or {})
    return subprocess.run(
        [sys.executable, "-m", "cockpit_harness", "--raiz", str(raiz), *args],
        cwd=raiz, capture_output=True, text=True, timeout=120, env=ambiente,
    )


def test_checar_descreve_o_consumidor(raiz: Path):
    saida = _cli(raiz, "checar")
    assert saida.returncode == int(Codigo.OK), saida.stderr
    assert "fonte única" in saida.stdout
    assert "RECUSADOS" in saida.stdout


def test_versao_vem_da_fonte_unica(raiz: Path):
    """O CI lê a versão daqui em vez de repetir o número no YAML — segunda fonte não nasce."""
    from cockpit_harness import contrato

    saida = _cli(raiz, "versao")
    assert saida.returncode == int(Codigo.OK)
    assert saida.stdout.strip() == contrato.versao_pinada(raiz)


def test_alvo_sem_homologacao_sai_12_e_nao_imprime_url(raiz: Path):
    saida = _cli(raiz, "alvo")
    assert saida.returncode == int(Codigo.SCOPE_MISSING)
    assert saida.stdout.strip() == ""


def test_pendencias_imprime_o_marcador_de_alvo(raiz: Path):
    saida = _cli(raiz, "pendencias")
    assert saida.returncode == int(Codigo.OK)
    assert saida.stdout.splitlines()[0] == "INCOMPLETE:target_url"


def test_pendencias_com_exigir_sai_12(raiz: Path):
    assert _cli(raiz, "pendencias", "--exigir").returncode == int(Codigo.SCOPE_MISSING)


def test_agente_nao_dispara_carga(raiz: Path):
    saida = _cli(raiz, "modo", "--modo", "load", "--runner", "agent")
    assert saida.returncode == int(Codigo.MODE_FORBIDDEN)
    assert "MODE_FORBIDDEN" in saida.stderr


def test_agente_nao_dispara_sondagem_ativa(raiz: Path):
    assert _cli(raiz, "modo", "--modo", "active_discovery", "--runner",
                "agent").returncode == int(Codigo.MODE_FORBIDDEN)


def test_inventario_e_liberado_para_o_agente(raiz: Path):
    assert _cli(raiz, "modo", "--modo", "inventory", "--runner", "agent").returncode == int(Codigo.OK)


def test_passivo_e_recusado_sem_alvo(raiz: Path):
    """Permitido pelo plano, recusado pelo escopo: a segunda porta é que fecha (12)."""
    saida = _cli(raiz, "modo", "--modo", "passive", "--runner", "ci")
    assert saida.returncode == int(Codigo.SCOPE_MISSING)
    assert "INCOMPLETE:target_url" in saida.stderr


def test_variavel_do_denylist_aborta_o_comando(raiz: Path):
    saida = _cli(raiz, "modo", "--modo", "inventory", "--runner", "ci",
                 extra_env={"WEBQA_LOAD_AUTHORIZED": "1"})
    assert saida.returncode == int(Codigo.DENIED_ENV)
    assert "DENIED_ENV" in saida.stderr


def test_laudo_de_inventario_sai_valido(raiz: Path, tmp_path: Path):
    destino = tmp_path / "laudo.json"
    saida = _cli(raiz, "laudo", "--modo", "inventory", "--runner", "ci", "--saida", str(destino))
    assert saida.returncode == int(Codigo.OK), saida.stderr
    laudo = json.loads(destino.read_text(encoding="utf-8"))
    assert laudo["execution"]["mode"] == "inventory"
    assert laudo["execution"]["network_used"] is False
    assert laudo["standard"]["name"] == "webqa-suite"
    assert laudo["summary"]["pendencias"] == ["INCOMPLETE:target_url", "INCOMPLETE:escopo-autorizado"]


def test_laudo_de_modo_de_rede_e_recusado(raiz: Path):
    """Sem alvo não há laudo passivo: melhor nenhum número que um número sem objeto."""
    assert _cli(raiz, "laudo", "--modo", "passive", "--runner",
                "ci").returncode == int(Codigo.SCOPE_MISSING)

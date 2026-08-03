"""Unidade — o plano de controle decide quem dispara o quê (contrato §4).

O plano usado aqui é fabricado, não o do repositório: o teste de unidade prova o COMPORTAMENTO
(default deny, agente nunca dispara modo segregado, denylist aborta em vez de ignorar). Que o
plano REAL declare essa matriz é assunto do teste de integração.
"""

from __future__ import annotations

import pytest

from cockpit_harness import plano
from cockpit_harness.codigos import AmbienteSujo, Codigo, ModoProibido

PLANO = {
    "execution_modes": {
        "inventory": {"network": False, "requires_auth": False, "agent_may_trigger": True, "job": "inline"},
        "passive": {"network": True, "requires_auth": True, "agent_may_trigger": True, "job": "inline"},
        "load": {"network": True, "requires_auth": True, "agent_may_trigger": False,
                 "job": "segregated", "trigger": "human_only"},
        "active_discovery": {"network": True, "requires_auth": True, "agent_may_trigger": False,
                             "job": "segregated", "trigger": "human_only"},
    },
    "env_hygiene": {
        "env_allowlist": ["PATH", "HOME", "LANG"],
        "env_denylist_prefix": ["WEBQA_"],
        "fail_on_denied_env": True,
    },
    "paths": {"runs": "harness/runs", "reports": "harness/reports", "state": "harness/state"},
}


@pytest.mark.parametrize(
    ("modo", "runner", "esperado"),
    [
        ("inventory", "agent", True),
        ("inventory", "ci", True),
        ("inventory", "human", True),
        ("passive", "agent", True),
        ("passive", "ci", True),
        ("load", "agent", False),
        ("load", "ci", False),
        ("load", "human", True),
        ("active_discovery", "agent", False),
        ("active_discovery", "ci", False),
        ("active_discovery", "human", True),
    ],
)
def test_matriz_de_modo_por_runner(modo, runner, esperado):
    assert plano.pode_disparar(PLANO, modo, runner) is esperado


def test_modo_desconhecido_e_negado_por_default():
    """Default deny: o que a harness não reconhece, ela não roteia como operação barata."""
    assert plano.pode_disparar(PLANO, "sondagem-nova", "human") is False


def test_runner_desconhecido_e_negado():
    assert plano.pode_disparar(PLANO, "inventory", "robo") is False


def test_exigir_permissao_levanta_codigo_11():
    with pytest.raises(ModoProibido) as erro:
        plano.exigir_permissao(PLANO, "load", "agent")
    assert erro.value.codigo is Codigo.MODE_FORBIDDEN


def test_ambiente_limpo_passa():
    assert plano.inspecionar_ambiente(PLANO, {"PATH": "/usr/bin", "HOME": "/root"}).limpo


def test_variavel_negada_e_listada_e_aborta():
    """fail_on_denied_env: aborta (10) em vez de ignorar — silêncio esconderia o erro."""
    resultado = plano.inspecionar_ambiente(PLANO, {"WEBQA_LOAD_AUTHORIZED": "1"})
    assert resultado.negadas == ("WEBQA_LOAD_AUTHORIZED",)
    with pytest.raises(AmbienteSujo) as erro:
        plano.exigir_ambiente_limpo(PLANO, {"WEBQA_LOAD_AUTHORIZED": "1"})
    assert erro.value.codigo is Codigo.DENIED_ENV


def test_denylist_desligado_nao_aborta():
    tolerante = {**PLANO, "env_hygiene": {**PLANO["env_hygiene"], "fail_on_denied_env": False}}
    plano.exigir_ambiente_limpo(tolerante, {"WEBQA_X": "1"})  # não levanta


def test_caminhos_de_evidencia_vem_do_plano():
    assert plano.caminho_de_evidencia(PLANO, "reports") == "harness/reports"

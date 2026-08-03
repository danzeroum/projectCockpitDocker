"""Leitura do plano de controle (harness/harness.yaml) — quem pode disparar o quê.

A matriz de modos não é hardcoded aqui: ela é LIDA da declaração. Um código que repete a matriz
seria uma segunda fonte de verdade, e a primeira divergência entre as duas passaria despercebida.
Aqui só mora o comportamento: default deny, e o modo desconhecido é recusado em vez de inferido.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

from cockpit_harness.codigos import AmbienteSujo, ConfigInvalida, ModoProibido

HARNESS_YAML = "harness/harness.yaml"

RUNNERS = ("agent", "human", "ci")


def carregar(raiz: Path) -> dict:
    arquivo = raiz / HARNESS_YAML
    if not arquivo.exists():
        raise ConfigInvalida(f"{HARNESS_YAML} ausente — a harness não age sem plano de controle")
    dados = yaml.safe_load(arquivo.read_text(encoding="utf-8"))
    if not isinstance(dados, dict):
        raise ConfigInvalida(f"{HARNESS_YAML}: esperado um mapeamento YAML")
    return dados


def modos(plano: dict) -> dict[str, dict]:
    return plano.get("execution_modes") or {}


def pode_disparar(plano: dict, modo: str, runner_kind: str) -> bool:
    """Default deny: modo ou runner que a harness não reconhece NÃO é autorizado.

    - ``agent`` só dispara modos com ``agent_may_trigger: true``.
    - ``ci`` automático nunca dispara modo de job ``segregated`` (esse é workflow_dispatch humano).
    - ``human`` dispara qualquer modo declarado.
    """
    if runner_kind not in RUNNERS:
        return False
    declarado = modos(plano).get(modo)
    if not isinstance(declarado, dict):
        return False
    if runner_kind == "human":
        return True
    if runner_kind == "agent":
        return bool(declarado.get("agent_may_trigger", False))
    return declarado.get("job") != "segregated"


def exigir_permissao(plano: dict, modo: str, runner_kind: str) -> None:
    """Porta fail-closed do roteamento de modo. Levanta ModoProibido (11)."""
    if not pode_disparar(plano, modo, runner_kind):
        raise ModoProibido(f"runner-kind {runner_kind!r} não pode disparar o modo {modo!r}")


@dataclass(frozen=True)
class Higiene:
    """Resultado da inspeção de ambiente (contrato §4 — a trava que morde)."""

    negadas: tuple[str, ...]
    aborta: bool

    @property
    def limpo(self) -> bool:
        return not self.negadas


def inspecionar_ambiente(plano: dict, ambiente: dict[str, str]) -> Higiene:
    """Lista as variáveis do denylist presentes no ambiente recebido."""
    higiene = plano.get("env_hygiene") or {}
    prefixos = tuple(higiene.get("env_denylist_prefix") or ())
    negadas = tuple(sorted(nome for nome in ambiente if nome.startswith(prefixos))) if prefixos else ()
    return Higiene(negadas=negadas, aborta=bool(higiene.get("fail_on_denied_env", False)))


def exigir_ambiente_limpo(plano: dict, ambiente: dict[str, str]) -> None:
    """Aborta (10) se encontrar variável proibida — NÃO apenas ignora.

    Ignorar em silêncio esconderia o erro de configuração que o controle existe para revelar.
    """
    resultado = inspecionar_ambiente(plano, ambiente)
    if resultado.negadas and resultado.aborta:
        raise AmbienteSujo("variáveis negadas presentes: " + ", ".join(resultado.negadas))


def caminho_de_evidencia(plano: dict, qual: str) -> str:
    caminhos = plano.get("paths") or {}
    if qual not in caminhos:
        raise ConfigInvalida(f"{HARNESS_YAML}: paths.{qual} não declarado")
    return str(caminhos[qual])

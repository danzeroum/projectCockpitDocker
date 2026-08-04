"""Códigos de saída e exceções — espelho executável de WEBQA_CONSUMER_CONTRACT.md §6.

Falha de configuração é evento operacional, não crash: a CLI sai com código estável e mensagem,
nunca com traceback. Manter a tabela do contrato em código (e não em prosa) é o que permite ao
teste provar que o código de saída anunciado é o código de saída real.
"""

from __future__ import annotations

from enum import IntEnum


class Codigo(IntEnum):
    """Códigos de saída estáveis (contrato §6)."""

    OK = 0
    USAGE = 2
    DENIED_ENV = 10
    MODE_FORBIDDEN = 11
    SCOPE_MISSING = 12
    SUITE_UNINSTALLED = 20
    SUITE_ERROR = 21
    # 22 e 23 nascem de uma medição: `webqa.sondagem` sai 0 mesmo quando o laudo diz
    # `inconclusivo: true` ou `abortado_por: circuit-breaker`. O relatório é honesto; o
    # código de saída não — e código de saída é o que um gate de CI lê. Distinguir os
    # dois casos importa: 22 é "não medi", 23 é "medi e reprovou". Confundi-los faria
    # um alvo inalcançável passar como alvo limpo.
    RUN_INCONCLUSIVE = 22
    THRESHOLD_EXCEEDED = 23
    PROVENANCE_INVALID = 30
    NOT_COMPARABLE = 31
    CONFIG_INVALID = 40


class ErroHarness(Exception):
    """Base de todo erro previsto. Carrega o código de saída correspondente."""

    codigo: Codigo = Codigo.SUITE_ERROR


class AmbienteSujo(ErroHarness):
    """Variável do denylist presente com fail_on_denied_env (10)."""

    codigo = Codigo.DENIED_ENV


class ModoProibido(ErroHarness):
    """Este runner-kind não pode disparar este modo (11)."""

    codigo = Codigo.MODE_FORBIDDEN


class EscopoAusente(ErroHarness):
    """Modo de rede sem alvo/escopo autorizado ou sem prova de posse (12)."""

    codigo = Codigo.SCOPE_MISSING


class RunInconclusivo(ErroHarness):
    """A sondagem não cobriu a superfície declarada (22). Não é "limpo": é "não medido"."""

    codigo = Codigo.RUN_INCONCLUSIVE


class LimiteExcedido(ErroHarness):
    """Achados acima do que config.yaml tolera (23)."""

    codigo = Codigo.THRESHOLD_EXCEEDED


class ProcedenciaInvalida(ErroHarness):
    """Laudo sem bloco de procedência válido (30)."""

    codigo = Codigo.PROVENANCE_INVALID


class NaoComparavel(ErroHarness):
    """Agregação recusada: réguas incompatíveis (31)."""

    codigo = Codigo.NOT_COMPARABLE


class ConfigInvalida(ErroHarness):
    """harness.yaml/config.yaml falhou schema ou regra de pin (40)."""

    codigo = Codigo.CONFIG_INVALID

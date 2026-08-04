"""Veredito sobre o laudo da Fase C — onde a honestidade do relatório vira código de saída.

O achado que motivou este módulo, medido na bancada:

    $ docker stop bancada-ingress
    $ python -m webqa.sondagem --alvo https://cockpit.bancada --executar
    Sondagem [https://cockpit.bancada]: 0/8 caminhos, 0 achado(s), ABORTADO por circuit-breaker
      Resultado INCONCLUSIVO: o run não cobriu a superfície declarada.
    EXIT CODE = 0

O laudo é honesto: diz `inconclusivo: true` e `abortado_por: circuit-breaker`. O
PROCESSO diz sucesso — `_emitir_relatorios` só devolve diferente de zero quando
`--baseline` pega achado novo. Um gate de CI lê o código de saída, não o JSON, e
recebe "limpo" de um run que não mediu absolutamente nada.

Isso é da régua e não temos escrita lá. O que dá para fazer do lado do consumidor
é não confiar no código de saída dela: lemos o laudo e emitimos o nosso.

Três vereditos, e a diferença entre os dois primeiros é a razão de existir do módulo:

  * 22 RUN_INCONCLUSIVE  — não medi. Alvo fora do ar, kill-switch, cobertura parcial.
  * 23 THRESHOLD_EXCEEDED — medi e reprovou, contra os limites de config.yaml §2.
  *  0 OK                 — medi tudo e passou.

"Zero achados" só significa alguma coisa depois de `esperado == executado`.
"""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from cockpit_harness.codigos import ConfigInvalida, LimiteExcedido, RunInconclusivo

# régua → chave de `thresholds` em tests/qa/config.yaml (§2). `baixa` não tem teto
# declarado: contá-la exigiria um limite que o contrato não define, e inventar o
# limite seria reprovar por um número que ninguém revisou.
TETOS = {"alta": "max_high", "media": "max_medium"}


def _ler_laudo(caminho: Path) -> dict:
    if not caminho.exists():
        raise RunInconclusivo(
            f"laudo ausente: {caminho}. A sondagem não chegou a gravar resultado — "
            "trate como não medido, nunca como limpo."
        )
    try:
        dados = json.loads(caminho.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise RunInconclusivo(f"laudo ilegível: {caminho} ({exc})") from None
    if not isinstance(dados, dict) or not isinstance(dados.get("alvos"), list):
        raise RunInconclusivo(f"laudo sem bloco 'alvos': {caminho}")
    return dados


def _tetos(raiz: Path) -> dict:
    config = raiz / "tests" / "qa" / "config.yaml"
    if not config.exists():
        raise ConfigInvalida(f"arquivo declarativo ausente: {config}")
    dados = yaml.safe_load(config.read_text(encoding="utf-8")) or {}
    limites = dados.get("thresholds") or {}
    return {sev: int(limites.get(chave, 0) or 0) for sev, chave in TETOS.items()}


def _exigir_cobertura(alvos: list) -> None:
    """Um alvo parcial condena o laudo inteiro. Não há média aqui.

    Dois alvos, um deles inconclusivo, não é "50% medido": é um laudo que não pode
    dizer se o alvo não-medido está limpo. Aprovar o conjunto porque a maioria
    passou é a média que esconde justamente o que não se olhou.
    """
    quebrados = []
    for alvo in alvos:
        nome = alvo.get("alvo", "?")
        esperado = int(alvo.get("esperado") or 0)
        executado = int(alvo.get("executado") or 0)
        abortado = str(alvo.get("abortado_por") or "")
        if alvo.get("inconclusivo") or abortado or executado != esperado:
            motivo = abortado or f"{executado}/{esperado} caminhos"
            quebrados.append(f"{nome} ({motivo})")
    if quebrados:
        raise RunInconclusivo(
            "a sondagem não cobriu a superfície declarada: " + "; ".join(quebrados)
            + ". Isto NÃO é 'nenhum achado' — é 'não medido'."
        )


def _exigir_limites(alvos: list, tetos: dict) -> None:
    contagem: dict[str, int] = {}
    for alvo in alvos:
        for achado in alvo.get("findings") or []:
            sev = str(achado.get("severidade") or "")
            contagem[sev] = contagem.get(sev, 0) + 1
    estouros = [
        f"{sev}: {contagem[sev]} achado(s), teto {teto}"
        for sev, teto in tetos.items()
        if contagem.get(sev, 0) > teto
    ]
    if estouros:
        raise LimiteExcedido(
            "achados acima do tolerado em tests/qa/config.yaml: " + "; ".join(estouros)
        )


def avaliar(laudo: Path, raiz: Path) -> str:
    """Levanta RunInconclusivo (22) ou LimiteExcedido (23); devolve o resumo se passou.

    A ORDEM importa: cobertura antes de limites. Um run que mediu 0 de 8 caminhos
    tem zero achados por construção, e checar os limites primeiro o aprovaria com
    louvor — o modo exato de errar que este módulo existe para impedir.
    """
    dados = _ler_laudo(laudo)
    alvos = dados["alvos"]
    if not alvos:
        raise RunInconclusivo(f"laudo sem alvo nenhum: {laudo}")

    _exigir_cobertura(alvos)
    _exigir_limites(alvos, _tetos(raiz))

    total = sum(len(a.get("findings") or []) for a in alvos)
    coberto = sum(int(a.get("executado") or 0) for a in alvos)
    return (f"veredito: {len(alvos)} alvo(s), {coberto} caminho(s) sondado(s), "
            f"{total} achado(s) dentro do tolerado")

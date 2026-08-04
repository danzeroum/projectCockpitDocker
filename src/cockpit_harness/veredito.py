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


def _config(raiz: Path) -> dict:
    config = raiz / "tests" / "qa" / "config.yaml"
    if not config.exists():
        raise ConfigInvalida(f"arquivo declarativo ausente: {config}")
    return yaml.safe_load(config.read_text(encoding="utf-8")) or {}


def _tetos(dados: dict) -> dict:
    limites = dados.get("thresholds") or {}
    return {sev: int(limites.get(chave, 0) or 0) for sev, chave in TETOS.items()}


def _vao_declarado(dados: dict) -> int:
    """Caminhos que o NOSSO ingress derruba antes de chegarem ao app.

    Medido: o ingress de homologação emite `location ~* (wp-login|\\.git|\\.env)
    { return 444; }` (deploy/homologacao/setup-ingress-homolog.sh). Três caminhos da
    lista curada caem nessa regra, a conexão é fechada sem resposta, e a régua não os
    conta como executados — 5/8, inconclusivo, para sempre.

    Sem esta declaração o modo sairia 22 em TODO run contra a superfície publicada. E
    um check permanentemente vermelho é um check que se aprende a ignorar: trocaria um
    exit 0 que mente por um exit 22 que grita sempre.

    Default 0: quem não declara nada continua exigindo cobertura total.
    """
    return int((dados.get("active_discovery") or {}).get("unreachable_by_our_ingress", 0) or 0)


def _exigir_cobertura(alvos: list, vao: int) -> list[str]:
    """Um alvo parcial condena o laudo inteiro. Não há média aqui.

    Dois alvos, um deles inconclusivo, não é "50% medido": é um laudo que não pode
    dizer se o alvo não-medido está limpo. Aprovar o conjunto porque a maioria
    passou é a média que esconde justamente o que não se olhou.

    O `vao` declarado é a ÚNICA tolerância, e ela é assimétrica de propósito:

    * vão MAIOR que o declarado → 22. Algo falhou além do que se sabia.
    * vão MENOR → passa, avisando. Mediu-se MAIS do que se esperava, o que é um
      resultado melhor; reprovar aqui puniria a melhora. Mas a declaração ficou
      velha (o ingress pode ter parado de derrubar aqueles caminhos, e isso é do
      interesse de quem lê), então o aviso sai nomeando o alvo.
    * `abortado_por` → 22 SEMPRE, vão nenhum perdoa. Kill-switch, circuit-breaker e
      falha de posse não são "o ingress derrubou três caminhos": são o run parando.

    O que esta tolerância NÃO consegue ser: precisa. O laudo informa `esperado` e
    `executado`, e a régua conta `falhas_rede`/`recuos` sem serializá-los — de fora
    não dá para saber QUAIS caminhos faltaram. A declaração fixa o número, não o
    conjunto. É mais fraco do que se gostaria e muito mais forte que o exit 0.
    """
    quebrados, avisos = [], []
    for alvo in alvos:
        nome = alvo.get("alvo", "?")
        esperado = int(alvo.get("esperado") or 0)
        executado = int(alvo.get("executado") or 0)
        abortado = str(alvo.get("abortado_por") or "")
        faltando = esperado - executado

        if abortado:
            quebrados.append(f"{nome} (abortado por {abortado})")
        elif faltando > vao:
            quebrados.append(f"{nome} ({executado}/{esperado} caminhos, vão declarado {vao})")
        elif faltando < vao:
            avisos.append(
                f"::warning::{nome} sondou {executado}/{esperado} — o vão declarado é {vao} e "
                f"foram {faltando}. Mediu-se mais que o esperado; confirme se o ingress parou "
                f"de derrubar caminhos e atualize active_discovery.unreachable_by_our_ingress."
            )
    if quebrados:
        raise RunInconclusivo(
            "a sondagem não cobriu a superfície declarada: " + "; ".join(quebrados)
            + ". Isto NÃO é 'nenhum achado' — é 'não medido'."
        )
    return avisos


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

    config = _config(raiz)
    vao = _vao_declarado(config)
    avisos = _exigir_cobertura(alvos, vao)
    _exigir_limites(alvos, _tetos(config))

    total = sum(len(a.get("findings") or []) for a in alvos)
    coberto = sum(int(a.get("executado") or 0) for a in alvos)
    esperado = sum(int(a.get("esperado") or 0) for a in alvos)
    linhas = list(avisos)
    linhas.append(
        f"veredito: {len(alvos)} alvo(s), {coberto}/{esperado} caminho(s) sondado(s)"
        + (f" (vão declarado: {vao} por alvo)" if vao else "")
        + f", {total} achado(s) dentro do tolerado"
    )
    return "\n".join(linhas)

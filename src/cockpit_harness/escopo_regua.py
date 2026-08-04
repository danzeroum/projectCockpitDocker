"""Tradução do escopo do CONSUMIDOR para o escopo que a RÉGUA lê.

Por que isto existe. Dois arquivos chamados `escopo-autorizado.yaml`, schemas
incompatíveis, e o CI copiava um no lugar do outro:

    contrato §3 (nosso)          régua (webqa/escopo.py)
    ─────────────────────        ────────────────────────
    authorized: true             alvos:
    scope.hosts: [...]             - origem: "https://host"
    proof_of_possession: {...}       autorizado_por: "..."
    authorization_expires: ...       data: 2026-08-04
                                     evidencia: "..."
                                     ambiente: homologacao
                                     verificacao: {tipo, valor}

`webqa.escopo.carregar` levanta `escopo sem alvos declarados` diante do nosso
formato — o `cp` do workflow entregava um arquivo que a régua não consegue ler.
Isso ficou invisível porque o modo `active_discovery` nunca chamou a sondagem.

A tradução mora AQUI e não no workflow por um motivo prático: bash de CI não tem
teste. Aqui tem, e a régua continua intocada — a fronteira do contrato é que o
consumidor contribui configuração, nunca código de verificação.

**Nada é inventado.** A régua recusa entrada sem `autorizado_por`, sem
`evidencia`, sem `data` ou com `ambiente` inválido. Preencher esses campos com
"ci", "n/a" ou `date.today()` faria a autorização parecer completa quando não é
— e uma autorização inventada é exatamente o que o escopo existe para impedir.
Faltando qualquer um, a tradução RECUSA com SCOPE_MISSING e diz qual declarar.
"""

from __future__ import annotations

from pathlib import Path
from urllib.parse import urlsplit

import yaml

from cockpit_harness.codigos import EscopoAusente
from cockpit_harness.contrato import Situacao

# contrato §2 (staging|production|preview) → régua (homologacao|producao|sandbox).
# `production` mapeia para `producao` de propósito, mesmo sendo o alvo que nunca
# deveria estar aqui: é o mapeamento que faz a régua PROIBIR escrita (C2) sozinha,
# via `EntradaEscopo.permite_escrita`. Traduzir produção como "sandbox" para
# "facilitar" desligaria essa proteção justamente onde ela mais importa.
AMBIENTES = {
    "staging": "homologacao",
    "production": "producao",
    "preview": "sandbox",
}

# Só este método tem equivalente na régua. `file` e `header` não têm: a entrada sai
# SEM `verificacao`, e a posse cai no padrão da régua (pino de IP no carregamento,
# takeover aborta o alvo). Emitir `tipo: dns_txt` sem token publicado seria pior que
# omitir — todo alvo abortaria com `dns-txt-ausente`, e o CI acusaria a régua.
METODO_DNS_TXT = "dns-txt"

# Placeholder do `.example`. Tratado como ausência: é o valor que um repositório
# recém-adotado carrega, e aceitá-lo autorizaria uma sondagem sem prova nenhuma.
NAO_CONFIGURADO = "not-configured"


def _origem(host: str, alvo: str | None) -> str:
    """`https://host[:porta]`, canônica como `webqa.auth.origem_de` produz.

    A porta vem do ALVO declarado quando o host é o mesmo: `scope.hosts` não
    carrega porta, e um alvo em `https://h:8443` com origem traduzida `https://h`
    seria recusado pela régua como fora de escopo — recusa correta, causa
    invisível.
    """
    if alvo:
        partes = urlsplit(alvo)
        if (partes.hostname or "").lower() == host.lower() and partes.port:
            return f"https://{host}:{partes.port}"
    return f"https://{host}"


def _exigir(situacao: Situacao) -> None:
    """Os quatro campos que a régua cobra e o contrato não pedia. Fail-closed."""
    escopo = situacao.escopo
    faltando = []
    if not (escopo and escopo.autorizado_em.strip()):
        faltando.append("authorized_on")
    if not (escopo and escopo.autorizado_por.strip()):
        faltando.append("authorized_by")
    if not (escopo and escopo.evidencia.strip()):
        faltando.append("evidence")
    if situacao.ambiente not in AMBIENTES:
        faltando.append(f"target.environment (é {situacao.ambiente!r}; use um de {sorted(AMBIENTES)})")
    if faltando:
        raise EscopoAusente(
            "escopo insuficiente para active_discovery; declare em "
            "tests/qa/escopo-autorizado.yaml: " + ", ".join(faltando)
        )


def traduzir(situacao: Situacao) -> dict:
    """Escopo no formato da régua. Levanta EscopoAusente (12) se faltar declaração.

    `situacao` precisa ter passado por `contrato.exigir_rede_liberada`: sem alvo e
    sem autorização vigente não há o que traduzir, e traduzir mesmo assim produziria
    um arquivo de escopo tecnicamente válido para uma autorização que não existe.
    """
    if not situacao.rede_liberada:
        raise EscopoAusente(
            "escopo não liberado; pendências: " + ", ".join(situacao.pendencias)
        )
    _exigir(situacao)
    escopo = situacao.escopo
    assert escopo is not None  # garantido por rede_liberada

    verificacao = {}
    if escopo.metodo_de_posse == METODO_DNS_TXT:
        referencia = escopo.prova_de_posse.strip()
        if not referencia or referencia == NAO_CONFIGURADO:
            raise EscopoAusente(
                "proof_of_possession.method é 'dns-txt' mas reference está vazio ou "
                f"{NAO_CONFIGURADO!r} — publique o TXT e declare o token"
            )
        verificacao = {"tipo": "dns_txt", "valor": referencia}

    alvos = []
    for host in escopo.hosts:
        entrada = {
            "origem": _origem(host, situacao.alvo),
            "autorizado_por": escopo.autorizado_por,
            "data": escopo.autorizado_em,
            "evidencia": escopo.evidencia,
            "ambiente": AMBIENTES[situacao.ambiente],
        }
        if verificacao:
            entrada["verificacao"] = dict(verificacao)
        alvos.append(entrada)

    if not alvos:
        raise EscopoAusente("scope.hosts vazio — não há origem para sondar")
    return {"alvos": alvos}


def escrever(situacao: Situacao, destino: Path) -> Path:
    """Grava o escopo traduzido. O arquivo é efêmero: vive no runner e some com ele."""
    dados = traduzir(situacao)
    destino.parent.mkdir(parents=True, exist_ok=True)
    cabecalho = (
        "# GERADO por `python -m cockpit_harness escopo-regua` a partir de\n"
        "# tests/qa/escopo-autorizado.yaml (contrato §3). Não edite e não comite:\n"
        "# é efêmero, vive no runner e some com ele.\n"
    )
    destino.write_text(
        cabecalho + yaml.safe_dump(dados, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    return destino

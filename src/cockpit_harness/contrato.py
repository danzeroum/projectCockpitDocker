"""Conformidade do consumidor com WEBQA_CONSUMER_CONTRACT.md (§1, §2, §3).

O que este módulo faz é VERIFICAÇÃO (o repositório está correto?), não validação do alvo
publicado (a auditoria faz isso, e exige rede + autorização). Ele responde três perguntas
que não dependem de rede nenhuma:

1. A régua está DECLARADA e não copiada? (§1 — fronteira do consumidor)
2. A versão mora em fonte única e o único espelho tolerado casa com ela? (§2 — pin exato)
3. Há alvo de homologação e autorização para tocar a rede? (§3 — escopo)

A terceira pergunta é a que costuma faltar. Quando falta, a resposta honesta é uma PENDÊNCIA
declarada (``INCOMPLETE:target_url``), não um alvo inventado: apontar a auditoria para produção
"porque era a URL que existia" é exatamente o acidente que o escopo autorizado existe para evitar.
"""

from __future__ import annotations

import datetime as _dt
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from cockpit_harness.codigos import ConfigInvalida, EscopoAusente

# §1 — nunca copiados para o consumidor. A régua é declarada por versão, não vendorizada.
CAMINHOS_PROIBIDOS = ("webqa", "checks", "data/caminhos-sensiveis.yaml")

REQUIREMENTS_QA = "requirements-qa.txt"
CONFIG_QA = "tests/qa/config.yaml"
ESCOPO_QA = "tests/qa/escopo-autorizado.yaml"

# RFC 2606 reserva .invalid para nomes garantidamente não resolvíveis. Um alvo terminado em
# .invalid é, por construção, um PLACEHOLDER — nunca um alvo real. Isso torna "alvo ausente"
# uma condição verificável em vez de uma convenção de comentário.
TLD_RESERVADO = ".invalid"

PENDENCIA_ALVO = "INCOMPLETE:target_url"
PENDENCIA_ESCOPO = "INCOMPLETE:escopo-autorizado"

_PIN = re.compile(r"^\s*webqa-suite==([^\s#]+)\s*(?:#.*)?$")
_FAIXA = re.compile(r"^\s*webqa-suite\s*(?:[><~!]=|[<>])")


def _ler_yaml(caminho: Path) -> dict:
    if not caminho.exists():
        raise ConfigInvalida(f"arquivo declarativo ausente: {caminho}")
    dados = yaml.safe_load(caminho.read_text(encoding="utf-8"))
    if not isinstance(dados, dict):
        raise ConfigInvalida(f"{caminho}: esperado um mapeamento YAML")
    return dados


def versao_pinada(raiz: Path) -> str:
    """Lê a FONTE ÚNICA da versão da régua. Faixa (>=, ~=) é erro, não tolerância.

    Faixa é recusada porque a superfície do que a suíte procura é dado de segurança: dois runs
    da "mesma" configuração não podem medir com réguas diferentes (contrato §7).
    """
    arquivo = raiz / REQUIREMENTS_QA
    if not arquivo.exists():
        raise ConfigInvalida(f"{REQUIREMENTS_QA} ausente — o pin do padrão é obrigatório")
    for linha in arquivo.read_text(encoding="utf-8").splitlines():
        achado = _PIN.match(linha)
        if achado:
            return achado.group(1)
        if _FAIXA.match(linha):
            raise ConfigInvalida(
                f"{REQUIREMENTS_QA}: webqa-suite declarado por faixa; exige-se pin exato (==)"
            )
    raise ConfigInvalida(f"{REQUIREMENTS_QA}: webqa-suite não está pinado com ==")


def versao_espelhada(raiz: Path) -> str:
    """Lê o único espelho tolerado da versão: tests/qa/config.yaml → standard_version."""
    config = _ler_yaml(raiz / CONFIG_QA)
    espelho = config.get("standard_version")
    if not isinstance(espelho, str) or not espelho:
        raise ConfigInvalida(f"{CONFIG_QA}: standard_version ausente ou vazio")
    return espelho


def conferir_fonte_unica(raiz: Path) -> str:
    """Cruza pin e espelho. Divergência é erro de configuração (40), nunca negociação."""
    pin = versao_pinada(raiz)
    espelho = versao_espelhada(raiz)
    if pin != espelho:
        raise ConfigInvalida(
            f"{CONFIG_QA} standard_version ({espelho!r}) != pin de {REQUIREMENTS_QA} ({pin!r})"
        )
    return pin


def regua_copiada(raiz: Path) -> list[str]:
    """Retorna os caminhos proibidos que existem no consumidor. Vazio = fronteira intacta.

    Uma cópia editável da lista curada é pior que nenhuma: quem edita remove a linha que dava
    trabalho, a suíte para de procurar aquilo, e o laudo segue dizendo "nenhum achado".
    """
    return [alvo for alvo in CAMINHOS_PROIBIDOS if (raiz / alvo).exists()]


def alvo_declarado(raiz: Path) -> str | None:
    """Devolve a base_url do alvo, ou None se ainda for placeholder (host .invalid)."""
    config = _ler_yaml(raiz / CONFIG_QA)
    base_url = (config.get("target") or {}).get("base_url", "")
    if not isinstance(base_url, str) or not base_url:
        return None
    host = base_url.split("//", 1)[-1].split("/", 1)[0].split(":", 1)[0]
    if host.endswith(TLD_RESERVADO):
        return None
    return base_url


def ambiente_do_alvo(raiz: Path) -> str:
    """staging | production | preview — declarado em config.yaml."""
    config = _ler_yaml(raiz / CONFIG_QA)
    return str((config.get("target") or {}).get("environment", ""))


@dataclass(frozen=True)
class Escopo:
    """Autorização declarada para modos que tocam a rede (contrato §3)."""

    autorizado: bool
    hosts: tuple[str, ...] = ()
    expira_em: str | None = None
    prova_de_posse: str = ""

    def expirado(self, hoje: _dt.date | None = None) -> bool:
        if not self.expira_em:
            return True
        hoje = hoje or _dt.date.today()
        try:
            return _dt.date.fromisoformat(self.expira_em) < hoje
        except ValueError as exc:
            raise ConfigInvalida(f"authorization_expires inválido: {self.expira_em!r}") from exc


def escopo_autorizado(raiz: Path) -> Escopo | None:
    """Lê tests/qa/escopo-autorizado.yaml. None quando o arquivo não existe.

    O arquivo REAL nunca é comitado (invariante 4): ele é injetado como segredo no CI. O que
    vive no repositório é o ``.example``, e a ausência do real é a condição normal — modos de
    rede simplesmente não são liberados.
    """
    arquivo = raiz / ESCOPO_QA
    if not arquivo.exists():
        return None
    dados = _ler_yaml(arquivo)
    prova = dados.get("proof_of_possession") or {}
    return Escopo(
        autorizado=bool(dados.get("authorized", False)),
        hosts=tuple((dados.get("scope") or {}).get("hosts", [])),
        expira_em=dados.get("authorization_expires"),
        prova_de_posse=str(prova.get("reference", "")),
    )


@dataclass(frozen=True)
class Situacao:
    """Retrato verificável do consumidor num instante — o que a CLI e o CI leem para decidir."""

    versao: str
    fronteira_intacta: bool
    alvo: str | None
    ambiente: str
    escopo: Escopo | None
    pendencias: tuple[str, ...] = field(default=())

    @property
    def rede_liberada(self) -> bool:
        """Modo de rede só roda com alvo declarado E escopo autorizado, vigente e com o host em escopo."""
        return not self.pendencias


def situacao(raiz: Path, hoje: _dt.date | None = None) -> Situacao:
    """Verificação completa e sem rede do consumidor (o Trabalho B do próprio repositório)."""
    versao = conferir_fonte_unica(raiz)
    copiados = regua_copiada(raiz)
    if copiados:
        raise ConfigInvalida(
            "régua copiada para dentro do consumidor (declarar, não copiar): " + ", ".join(copiados)
        )

    alvo = alvo_declarado(raiz)
    escopo = escopo_autorizado(raiz)
    pendencias: list[str] = []
    if alvo is None:
        pendencias.append(PENDENCIA_ALVO)
    if escopo is None or not escopo.autorizado or escopo.expirado(hoje):
        pendencias.append(PENDENCIA_ESCOPO)
    elif alvo is not None:
        host = alvo.split("//", 1)[-1].split("/", 1)[0].split(":", 1)[0]
        if host not in escopo.hosts:
            # Comparação de ORIGEM EXATA: host fora da lista nunca é tocado (contrato §3).
            pendencias.append(PENDENCIA_ESCOPO)

    return Situacao(
        versao=versao,
        fronteira_intacta=True,
        alvo=alvo,
        ambiente=ambiente_do_alvo(raiz),
        escopo=escopo,
        pendencias=tuple(pendencias),
    )


def exigir_rede_liberada(raiz: Path, hoje: _dt.date | None = None) -> Situacao:
    """Porta fail-closed para os modos de rede: sem alvo + escopo, levanta EscopoAusente (12)."""
    atual = situacao(raiz, hoje)
    if not atual.rede_liberada:
        raise EscopoAusente(
            "modo de rede recusado; pendências: " + ", ".join(atual.pendencias)
        )
    return atual

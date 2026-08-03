"""Unidade — conformidade com o contrato de consumo (§1, §2, §3).

Verificação, não validação: nada aqui toca a rede. Os casos escolhidos são os LIMITES, porque é
onde a trava morde ou deixa de morder — faixa em vez de pin, espelho divergente, host fora do
escopo, autorização vencida, régua copiada.
"""

from __future__ import annotations

import datetime as dt

import pytest

from cockpit_harness import contrato
from cockpit_harness.codigos import Codigo, ConfigInvalida, EscopoAusente


# --- §2 fonte única da versão -------------------------------------------------------------

def test_pin_exato_e_lido(repo_falso):
    assert contrato.versao_pinada(repo_falso()) == "1.0.0"


@pytest.mark.parametrize("faixa", ["webqa-suite>=1.0.0", "webqa-suite~=1.0", "webqa-suite>1.0.0"])
def test_faixa_e_recusada(repo_falso, faixa):
    """Faixa deixaria dois runs medirem com réguas diferentes — é erro de configuração (40)."""
    with pytest.raises(ConfigInvalida) as erro:
        contrato.versao_pinada(repo_falso(pin=faixa))
    assert erro.value.codigo is Codigo.CONFIG_INVALID


def test_pin_ausente_e_recusado(repo_falso):
    with pytest.raises(ConfigInvalida):
        contrato.versao_pinada(repo_falso(pin="# nenhum pin aqui"))


def test_espelho_divergente_e_erro(repo_falso):
    with pytest.raises(ConfigInvalida, match="standard_version"):
        contrato.conferir_fonte_unica(repo_falso(espelho="0.9.0"))


def test_espelho_igual_ao_pin_passa(repo_falso):
    assert contrato.conferir_fonte_unica(repo_falso()) == "1.0.0"


# --- §1 fronteira: declarar, não copiar ---------------------------------------------------

@pytest.mark.parametrize("caminho", ["webqa/gates.py", "checks/backend/x.py",
                                     "data/caminhos-sensiveis.yaml"])
def test_regua_copiada_e_detectada(repo_falso, caminho):
    raiz = repo_falso(copiar_regua=caminho)
    assert contrato.regua_copiada(raiz)
    with pytest.raises(ConfigInvalida, match="régua copiada"):
        contrato.situacao(raiz)


def test_fronteira_intacta_quando_nada_foi_copiado(repo_falso):
    assert contrato.regua_copiada(repo_falso()) == []


# --- §3 alvo e escopo ---------------------------------------------------------------------

def test_host_invalid_nao_conta_como_alvo(repo_falso):
    """RFC 2606: .invalid nunca resolve, logo nunca é alvo real — é placeholder verificável."""
    assert contrato.alvo_declarado(repo_falso()) is None


def test_alvo_real_e_reconhecido(repo_falso):
    raiz = repo_falso(base_url="https://homolog.exemplo.test")
    assert contrato.alvo_declarado(raiz) == "https://homolog.exemplo.test"


def test_sem_alvo_a_pendencia_e_target_url(repo_falso):
    pendencias = contrato.situacao(repo_falso()).pendencias
    assert contrato.PENDENCIA_ALVO in pendencias
    assert pendencias[0] == "INCOMPLETE:target_url"


def test_sem_escopo_a_rede_fica_recusada(repo_falso):
    assert contrato.situacao(repo_falso()).rede_liberada is False


def test_alvo_e_escopo_completos_liberam_a_rede(repo_falso, escopo_valido):
    raiz = repo_falso(base_url="https://homolog.exemplo.test", escopo=escopo_valido)
    atual = contrato.situacao(raiz)
    assert atual.pendencias == ()
    assert atual.rede_liberada is True


def test_host_fora_do_escopo_recusa_mesmo_com_alvo(repo_falso, escopo_valido):
    """Comparação de ORIGEM EXATA: um host que não está na lista nunca é tocado."""
    raiz = repo_falso(base_url="https://outro.exemplo.test", escopo=escopo_valido)
    assert contrato.PENDENCIA_ESCOPO in contrato.situacao(raiz).pendencias


def test_autorizacao_vencida_recusa(repo_falso, escopo_valido):
    vencido = escopo_valido.replace("2999-12-31", "2020-01-01")
    raiz = repo_falso(base_url="https://homolog.exemplo.test", escopo=vencido)
    assert contrato.PENDENCIA_ESCOPO in contrato.situacao(raiz, hoje=dt.date(2026, 8, 3)).pendencias


def test_authorized_false_recusa(repo_falso, escopo_valido):
    desligado = escopo_valido.replace("authorized: true", "authorized: false")
    raiz = repo_falso(base_url="https://homolog.exemplo.test", escopo=desligado)
    assert contrato.PENDENCIA_ESCOPO in contrato.situacao(raiz).pendencias


def test_exigir_rede_liberada_falha_com_codigo_12(repo_falso):
    with pytest.raises(EscopoAusente) as erro:
        contrato.exigir_rede_liberada(repo_falso())
    assert erro.value.codigo is Codigo.SCOPE_MISSING
    assert "INCOMPLETE:target_url" in str(erro.value)

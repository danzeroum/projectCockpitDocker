"""A ponte entre os dois `escopo-autorizado.yaml` de schemas incompatíveis.

Dois arquivos, mesmo nome, formatos que não se leem. O CI copiava um no lugar do
outro e ninguém percebeu, porque o modo que consumiria o arquivo nunca chamava a
sondagem. O teste que faltava não é "a tradução tem os campos certos" — é "a
RÉGUA aceita o que traduzimos", e esse mora em tests/integration/test_fase_c.py.

Aqui ficam as recusas: o que a tradução se nega a inventar.
"""

from __future__ import annotations

import shutil

import pytest
import yaml

from cockpit_harness import contrato, escopo_regua
from cockpit_harness.codigos import Codigo, EscopoAusente

ESCOPO_COMPLETO = {
    "authorized": True,
    "authorized_by": "danzeroum",
    "authorized_on": "2026-08-01",
    "evidence": "pr#1",
    "scope": {"hosts": ["homolog.exemplo.test"]},
    "proof_of_possession": {"method": "file", "reference": "arquivo-publicado"},
    "authorization_expires": "2099-12-31",
}


@pytest.fixture
def raiz(tmp_path, request):
    """Cópia mínima do consumidor, com alvo e escopo já declarados."""
    origem = request.config.rootpath
    shutil.copytree(origem / "tests" / "qa", tmp_path / "tests" / "qa")
    shutil.copy(origem / "requirements-qa.txt", tmp_path / "requirements-qa.txt")
    config = yaml.safe_load((tmp_path / "tests/qa/config.yaml").read_text(encoding="utf-8"))
    config["target"]["base_url"] = "https://homolog.exemplo.test"
    (tmp_path / "tests/qa/config.yaml").write_text(yaml.safe_dump(config), encoding="utf-8")
    return tmp_path


def _declarar(raiz, **mudancas):
    dados = {**ESCOPO_COMPLETO, **mudancas}
    for chave, valor in list(dados.items()):
        if valor is None:
            del dados[chave]
    (raiz / "tests/qa/escopo-autorizado.yaml").write_text(
        yaml.safe_dump(dados), encoding="utf-8")
    return contrato.situacao(raiz)


def test_traduz_o_que_foi_declarado(raiz):
    alvos = escopo_regua.traduzir(_declarar(raiz))["alvos"]
    assert alvos == [{
        "origem": "https://homolog.exemplo.test",
        "autorizado_por": "danzeroum",
        "data": "2026-08-01",
        "evidencia": "pr#1",
        "ambiente": "homologacao",
    }]


@pytest.mark.parametrize("campo,contrato_diz", [
    ("authorized_by", "quem autorizou"),
    ("authorized_on", "quando autorizou"),
    ("evidence", "com que evidência"),
])
def test_campo_faltando_recusa_em_vez_de_inventar(raiz, campo, contrato_diz):
    """A régua recusa entrada com autor vazio, evidência vazia ou data futura.

    Preencher com "ci" ou `date.today()` faria a autorização passar na validação da
    régua sem existir de verdade — o arquivo diria que alguém autorizou hoje quando
    ninguém autorizou nunca. Recusar é a única resposta honesta.
    """
    with pytest.raises(EscopoAusente) as erro:
        escopo_regua.traduzir(_declarar(raiz, **{campo: ""}))
    assert campo in str(erro.value), f"a recusa não diz qual campo falta ({contrato_diz})"
    assert erro.value.codigo is Codigo.SCOPE_MISSING


def test_producao_e_traduzida_como_producao(raiz):
    """Não é descuido: é `EntradaEscopo.permite_escrita` que lê este campo, e ela
    proíbe C2 exatamente quando o ambiente é `producao`. Traduzir produção como
    "sandbox" para o arquivo "passar" desligaria a proteção onde ela mais importa."""
    config = yaml.safe_load((raiz / "tests/qa/config.yaml").read_text(encoding="utf-8"))
    config["target"]["environment"] = "production"
    (raiz / "tests/qa/config.yaml").write_text(yaml.safe_dump(config), encoding="utf-8")

    alvos = escopo_regua.traduzir(_declarar(raiz))["alvos"]
    assert alvos[0]["ambiente"] == "producao"


def test_ambiente_desconhecido_recusa(raiz):
    config = yaml.safe_load((raiz / "tests/qa/config.yaml").read_text(encoding="utf-8"))
    config["target"]["environment"] = "qualquer-coisa"
    (raiz / "tests/qa/config.yaml").write_text(yaml.safe_dump(config), encoding="utf-8")
    with pytest.raises(EscopoAusente):
        escopo_regua.traduzir(_declarar(raiz))


def test_dns_txt_sem_token_recusa_antes_de_sondar(raiz):
    """`not-configured` é o placeholder do `.example`. Traduzi-lo abriria um run cuja
    prova de posse é a string "not-configured" — e a régua abortaria cada alvo com
    `dns-txt-ausente`, fazendo parecer defeito dela."""
    with pytest.raises(EscopoAusente, match="not-configured"):
        escopo_regua.traduzir(_declarar(
            raiz, proof_of_possession={"method": "dns-txt", "reference": "not-configured"}))


def test_dns_txt_com_token_vira_verificacao(raiz):
    alvos = escopo_regua.traduzir(_declarar(
        raiz, proof_of_possession={"method": "dns-txt", "reference": "webqa-ownership=abc"}))["alvos"]
    assert alvos[0]["verificacao"] == {"tipo": "dns_txt", "valor": "webqa-ownership=abc"}


def test_metodo_sem_equivalente_sai_sem_verificacao(raiz):
    """`file` e `header` não existem na régua. Emitir `tipo: dns_txt` mesmo assim
    abortaria todo alvo; omitir cai no padrão dela — pino de IP, takeover aborta."""
    alvos = escopo_regua.traduzir(_declarar(
        raiz, proof_of_possession={"method": "header", "reference": "X-Prova: abc"}))["alvos"]
    assert "verificacao" not in alvos[0]


def test_porta_do_alvo_sobrevive_a_traducao(raiz):
    """`scope.hosts` não carrega porta. Um alvo em :8443 traduzido para origem sem
    porta seria recusado pela régua como fora de escopo — recusa correta, causa
    invisível, meia hora de CI para descobrir."""
    config = yaml.safe_load((raiz / "tests/qa/config.yaml").read_text(encoding="utf-8"))
    config["target"]["base_url"] = "https://homolog.exemplo.test:8443/painel"
    (raiz / "tests/qa/config.yaml").write_text(yaml.safe_dump(config), encoding="utf-8")

    alvos = escopo_regua.traduzir(_declarar(raiz))["alvos"]
    assert alvos[0]["origem"] == "https://homolog.exemplo.test:8443"


def test_sem_autorizacao_nao_ha_traducao(raiz):
    with pytest.raises(EscopoAusente):
        escopo_regua.traduzir(_declarar(raiz, authorized=False))


def test_autorizacao_expirada_nao_ha_traducao(raiz):
    with pytest.raises(EscopoAusente):
        escopo_regua.traduzir(_declarar(raiz, authorization_expires="2020-01-01"))


def test_o_arquivo_gerado_avisa_que_e_gerado(raiz, tmp_path):
    destino = escopo_regua.escrever(_declarar(raiz), tmp_path / "saida" / "escopo.yaml")
    texto = destino.read_text(encoding="utf-8")
    assert "GERADO" in texto and "não comite" in texto
    assert yaml.safe_load(texto)["alvos"][0]["origem"] == "https://homolog.exemplo.test"

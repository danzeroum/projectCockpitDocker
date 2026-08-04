"""O veredito que a régua não emite.

Medido na bancada, com o ingress parado:

    Sondagem [https://cockpit.bancada]: 0/8 caminhos, 0 achado(s), ABORTADO por circuit-breaker
      Resultado INCONCLUSIVO: o run não cobriu a superfície declarada.
    EXIT CODE = 0

O laudo é honesto; o código de saída não. Estes testes fixam a diferença entre
"não medi" (22) e "medi e reprovou" (23) — confundir os dois faria um alvo
inalcançável passar como alvo limpo, que é o pior resultado possível numa
auditoria: o silêncio com cara de aprovação.
"""

from __future__ import annotations

import json
import shutil

import pytest
import yaml

from cockpit_harness import veredito
from cockpit_harness.codigos import Codigo, LimiteExcedido, RunInconclusivo


def _alvo(nome="https://homolog.exemplo.test", esperado=8, executado=8,
          inconclusivo=False, abortado="", findings=()):
    return {"alvo": nome, "esperado": esperado, "executado": executado,
            "inconclusivo": inconclusivo, "abortado_por": abortado,
            "run_id": "fase-c-teste", "findings": list(findings)}


def _achado(severidade="alta"):
    return {"tipo": "vcs", "recurso": "/.git/HEAD", "severidade": severidade,
            "evidencia": "HEAD 200", "fase": "C", "remediacao": "bloquear no ingress",
            "procedencia": "sondagem"}


@pytest.fixture
def raiz(tmp_path, request):
    shutil.copytree(request.config.rootpath / "tests" / "qa", tmp_path / "tests" / "qa")
    return tmp_path


def _laudo(raiz, *alvos):
    caminho = raiz / "laudo.json"
    caminho.write_text(json.dumps({"alvos": list(alvos)}), encoding="utf-8")
    return caminho


def test_cobertura_completa_e_sem_achado_passa(raiz):
    resumo = veredito.avaliar(_laudo(raiz, _alvo()), raiz)
    assert "8 caminho(s)" in resumo and "0 achado(s)" in resumo


def test_alvo_fora_do_ar_nao_e_alvo_limpo(raiz):
    """O caso exato medido na bancada. Zero achados porque zero requisições."""
    with pytest.raises(RunInconclusivo) as erro:
        veredito.avaliar(
            _laudo(raiz, _alvo(esperado=8, executado=0, inconclusivo=True,
                               abortado="circuit-breaker")), raiz)
    assert erro.value.codigo is Codigo.RUN_INCONCLUSIVE
    assert "circuit-breaker" in str(erro.value)
    assert "não medido" in str(erro.value)


def test_cobertura_parcial_reprova_mesmo_sem_flag(raiz):
    """`executado != esperado` basta: não se depende de a régua ter marcado a flag.
    Duas fontes concordando é redundância barata; confiar só na flag é confiar que
    quem produziu o laudo classificou o próprio run corretamente.

    4/8 e não 5/8 porque `unreachable_by_our_ingress: 3` tolera exatamente três —
    e o caso 5/8 tem teste próprio logo abaixo.
    """
    with pytest.raises(RunInconclusivo, match="4/8"):
        veredito.avaliar(_laudo(raiz, _alvo(executado=4, inconclusivo=False)), raiz)


# ---------------------------------------------------------------------------
# o vão do nosso próprio ingress
# ---------------------------------------------------------------------------
# `return 444` em (wp-login|\.git|\.env) derruba três caminhos da lista curada antes
# de chegarem ao app. Sem declarar isso, o modo sairia 22 em TODO run contra a
# superfície publicada — e check permanentemente vermelho é check ignorado.

def test_o_vao_declarado_e_tolerado(raiz):
    """O caso real medido na bancada: 5/8 com `unreachable_by_our_ingress: 3`."""
    resumo = veredito.avaliar(_laudo(raiz, _alvo(executado=5, inconclusivo=True)), raiz)
    assert "vão declarado: 3" in resumo


def test_um_caminho_a_mais_faltando_reprova(raiz):
    """A tolerância é do TAMANHO declarado, não "parcial tudo bem". O quarto caminho
    que some é o que ninguém previu — exatamente o que se quer ver."""
    with pytest.raises(RunInconclusivo, match="vão declarado 3"):
        veredito.avaliar(_laudo(raiz, _alvo(executado=4, inconclusivo=True)), raiz)


def test_abortado_nao_e_perdoado_pelo_vao(raiz):
    """Kill-switch e circuit-breaker não são "o ingress derrubou três caminhos": são
    o run parando. Nenhum vão declarado cobre isso — nem um run que, por coincidência,
    parou com a diferença exata do vão."""
    with pytest.raises(RunInconclusivo, match="abortado por circuit-breaker"):
        veredito.avaliar(
            _laudo(raiz, _alvo(executado=5, inconclusivo=True, abortado="circuit-breaker")), raiz)


def test_vao_menor_passa_avisando_que_a_declaracao_envelheceu(raiz):
    """Assimetria deliberada: mediu-se MAIS que o esperado, e reprovar puniria a
    melhora. Mas a declaração ficou velha — o ingress pode ter parado de derrubar
    aqueles caminhos, e quem lê o laudo tem interesse nisso."""
    resumo = veredito.avaliar(_laudo(raiz, _alvo(executado=8)), raiz)
    assert "::warning::" in resumo
    assert "unreachable_by_our_ingress" in resumo


def test_sem_declaracao_a_cobertura_total_volta_a_ser_exigida(raiz):
    """Default 0. Quem não declara vão nenhum continua com a régua antiga —
    a tolerância é opt-in, não um relaxamento que chega de graça."""
    config = yaml.safe_load((raiz / "tests/qa/config.yaml").read_text(encoding="utf-8"))
    del config["active_discovery"]
    (raiz / "tests/qa/config.yaml").write_text(yaml.safe_dump(config), encoding="utf-8")
    with pytest.raises(RunInconclusivo):
        veredito.avaliar(_laudo(raiz, _alvo(executado=5, inconclusivo=True)), raiz)


def test_um_alvo_parcial_condena_o_laudo_inteiro(raiz):
    """Não há média: o alvo medido não diz nada sobre o não medido."""
    with pytest.raises(RunInconclusivo, match="segundo"):
        veredito.avaliar(
            _laudo(raiz, _alvo(), _alvo(nome="segundo", executado=0, inconclusivo=True)), raiz)


def test_achado_alto_estoura_o_teto_declarado(raiz):
    """`max_high: 0` em tests/qa/config.yaml — o knob existia e ninguém o lia."""
    with pytest.raises(LimiteExcedido) as erro:
        veredito.avaliar(_laudo(raiz, _alvo(findings=[_achado("alta")])), raiz)
    assert erro.value.codigo is Codigo.THRESHOLD_EXCEEDED
    assert "teto 0" in str(erro.value)


def test_achado_medio_dentro_do_teto_passa(raiz):
    """`max_medium: 5`: reprovar no primeiro médio ignoraria o número que o
    repositório declarou depois de pensar nele."""
    veredito.avaliar(_laudo(raiz, _alvo(findings=[_achado("media")] * 5)), raiz)
    with pytest.raises(LimiteExcedido):
        veredito.avaliar(_laudo(raiz, _alvo(findings=[_achado("media")] * 6)), raiz)


def test_cobertura_e_avaliada_antes_dos_limites(raiz):
    """A ORDEM é a propriedade. Um run que mediu 0 de 8 tem zero achados por
    construção: checar limites primeiro o aprovaria com louvor."""
    with pytest.raises(RunInconclusivo):
        veredito.avaliar(
            _laudo(raiz, _alvo(executado=0, inconclusivo=True, findings=[])), raiz)


def test_laudo_ausente_e_nao_medido_e_nao_limpo(raiz):
    with pytest.raises(RunInconclusivo):
        veredito.avaliar(raiz / "nunca-existiu.json", raiz)


def test_laudo_corrompido_nao_vira_aprovacao(raiz):
    caminho = raiz / "laudo.json"
    caminho.write_text("{isto não é json", encoding="utf-8")
    with pytest.raises(RunInconclusivo):
        veredito.avaliar(caminho, raiz)


def test_laudo_sem_alvo_nenhum_reprova(raiz):
    with pytest.raises(RunInconclusivo):
        veredito.avaliar(_laudo(raiz), raiz)


def test_o_teto_vem_do_config_do_projeto(raiz):
    """Muda o número declarado, muda o veredito — senão o teto seria decorativo."""
    config = yaml.safe_load((raiz / "tests/qa/config.yaml").read_text(encoding="utf-8"))
    config["thresholds"]["max_high"] = 2
    (raiz / "tests/qa/config.yaml").write_text(yaml.safe_dump(config), encoding="utf-8")
    veredito.avaliar(_laudo(raiz, _alvo(findings=[_achado("alta")] * 2)), raiz)

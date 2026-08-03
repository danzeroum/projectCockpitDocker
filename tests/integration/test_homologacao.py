"""Integração — o stack de homologação, lido como declaração fiscalizável.

Um compose de ambiente de teste é onde as travas se afrouxam sem que ninguém repare: alguém
copia o de produção, mantém ENABLE_ACTIONS="1" e POST/DELETE no socket-proxy, e o "ambiente
de teste" vira uma segunda porta para o daemon Docker do servidor real — com uma senha mais
fraca, porque "é só homologação".

Estes testes são o que impede isso de passar em revisão. Eles não sobem nada: leem o YAML.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml

COMPOSE = "deploy/homologacao/compose.yml"
ENV_EXEMPLO = "deploy/homologacao/.env.example"
ENV_REAL = "deploy/homologacao/.env"
SETUP = "deploy/homologacao/setup-ingress-homolog.sh"

# Nomes do stack de PRODUÇÃO (danzeroum/docker@89ce0ae). Colidir com qualquer um deles
# significa que `compose up` em homologação derruba o cockpit de verdade.
NOMES_DE_PRODUCAO = {"docker-cockpit", "docker-cockpit-proxy"}
HOST_DE_PRODUCAO = "docker.danzeroum.com"


@pytest.fixture(scope="module")
def compose(request) -> dict:
    return yaml.safe_load((Path(request.config.rootpath) / COMPOSE).read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def ambiente(request) -> dict[str, str]:
    texto = (Path(request.config.rootpath) / ENV_EXEMPLO).read_text(encoding="utf-8")
    pares = {}
    for linha in texto.splitlines():
        if linha.strip() and not linha.startswith("#") and "=" in linha:
            chave, _, valor = linha.partition("=")
            pares[chave.strip()] = valor.strip()
    return pares


# --- isolamento em relação a produção -----------------------------------------------------

@pytest.mark.parametrize("servico", ["app", "docker-socket-proxy"])
def test_container_nao_colide_com_producao(compose: dict, servico: str):
    nome = compose["services"][servico]["container_name"]
    assert nome not in NOMES_DE_PRODUCAO, f"{nome} é o container de produção"
    assert nome.endswith("-homolog")


def test_volume_de_dados_e_proprio(compose: dict):
    """`down -v` em homologação não pode apagar 30 dias de série de produção."""
    assert "cockpit-data-homolog" in compose["volumes"]
    assert "cockpit-data" not in compose["volumes"]


def test_projeto_compose_tem_nome_proprio(compose: dict):
    assert compose["name"] == "docker-cockpit-homolog"


def test_app_aponta_para_o_proxy_de_homologacao(compose: dict):
    ambiente = compose["services"]["app"]["environment"]
    assert "homolog" in ambiente["SOCKET_PROXY"]
    assert "homolog" in ambiente["DOCKER_HOST"]


# --- as duas trancas contra superfície de escrita ------------------------------------------

def test_acoes_de_escrita_desligadas(compose: dict):
    """Produção fixa "1"; homologação fixa "0" — as rotas de mutação nem são registradas."""
    assert compose["services"]["app"]["environment"]["ENABLE_ACTIONS"] == "0"


@pytest.mark.parametrize("verbo", ["POST", "DELETE"])
def test_socket_proxy_nega_escrita_no_daemon(compose: dict, verbo: str):
    """A segunda tranca, fora do alcance da aplicação: mesmo com a flag ligada por engano,
    o daemon não aceita escrita vinda deste stack."""
    assert compose["services"]["docker-socket-proxy"]["environment"][verbo] == 0


def test_socket_do_daemon_e_somente_leitura(compose: dict):
    montagens = compose["services"]["docker-socket-proxy"]["volumes"]
    assert any(m.endswith("docker.sock:ro") for m in montagens)


def test_montagens_do_host_sao_somente_leitura(compose: dict):
    """Só o volume nomeado do próprio stack pode ser escrito."""
    for montagem in compose["services"]["app"]["volumes"]:
        if montagem.startswith("/"):
            assert montagem.endswith(":ro"), f"montagem de host sem :ro — {montagem}"


def test_codigo_do_cockpit_nao_foi_vendorizado(request):
    """ADR-007: o compose constrói do clone no servidor; o produto não mora aqui."""
    raiz = Path(request.config.rootpath)
    assert not (raiz / "app").exists()
    compose_texto = (raiz / COMPOSE).read_text(encoding="utf-8")
    assert "COCKPIT_SRC" in compose_texto


# --- credenciais ---------------------------------------------------------------------------

def test_env_real_nao_esta_comitado(request):
    raiz = Path(request.config.rootpath)
    assert not (raiz / ENV_REAL).exists()
    assert ENV_REAL in (raiz / ".gitignore").read_text(encoding="utf-8")


def test_exemplo_nao_carrega_credencial_de_verdade(ambiente: dict[str, str]):
    """Um .env.example com senha real é uma senha vazada com passo extra."""
    senha = ambiente.get("BASIC_AUTH_PASS", "")
    assert senha.upper().startswith("TROQUE"), "BASIC_AUTH_PASS deve ser placeholder"
    assert ambiente.get("BASIC_AUTH_USER", "").startswith("troque")


def test_nenhum_arquivo_de_deploy_atribui_segredo(request):
    """Nenhum arquivo versionado atribui valor a uma variável de credencial.

    Este teste NÃO cita a senha de produção. Escrever a string proibida aqui para poder
    procurá-la depois versionaria o segredo dentro do próprio guarda — o erro que o guarda
    existe para impedir. A regra é de FORMA: se uma chave de credencial recebe qualquer coisa
    que não seja placeholder, reprova, seja qual for o valor.
    """
    raiz = Path(request.config.rootpath)
    chaves = re.compile(r"^\s*(?:-\s*)?(\w*(?:PASS|PASSWORD|SECRET|TOKEN|APIKEY|API_KEY)\w*)\s*[:=]\s*(.+)$",
                        re.IGNORECASE | re.MULTILINE)
    for caminho in (raiz / ENV_EXEMPLO, raiz / COMPOSE, raiz / SETUP):
        for chave, valor in chaves.findall(caminho.read_text(encoding="utf-8")):
            limpo = valor.strip().strip('"\'')
            aceito = (
                not limpo                          # vazio
                or limpo.upper().startswith("TROQUE")
                or limpo.startswith("$")           # interpolação, não valor
                or limpo.startswith("/")           # caminho PARA a credencial (ex.: HTPASSWD), não ela
            )
            assert aceito, f"{caminho.name}: {chave} recebe um valor concreto ({limpo[:12]}…)"


# --- alvo ------------------------------------------------------------------------------------

def test_dominio_de_exemplo_nao_e_producao(ambiente: dict[str, str]):
    assert ambiente["DOMAIN"] != HOST_DE_PRODUCAO
    assert ambiente["DOMAIN"].startswith("homolog.")


def test_script_de_ingress_recusa_o_host_de_producao(request):
    """O script publica o upstream de homologação; apontá-lo para produção a sequestraria."""
    texto = (Path(request.config.rootpath) / SETUP).read_text(encoding="utf-8")
    assert HOST_DE_PRODUCAO in texto and 'exit 1' in texto
    assert "docker-cockpit-homolog:8000" in texto
    assert ".htpasswd-homolog" in texto


def test_retencao_curta_para_nao_encher_o_disco_de_producao(ambiente: dict[str, str]):
    """O stack divide o disco com produção; série longa em teste vira incidente lá."""
    assert int(ambiente["RETENTION_RAW_HOURS"]) <= 24
    assert int(ambiente["RETENTION_ROLLUP_DAYS"]) <= 7

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
def compose_texto(request) -> str:
    return (Path(request.config.rootpath) / COMPOSE).read_text(encoding="utf-8")


# A DECLARAÇÃO da bancada mudou de casa na fatia-4 da CP-003. Era
# `business/rules/homologacao.yaml` (RULE-HOMOLOG-001..004); virou a etapa STAGE-DEPLOY em
# `harness/stages.yaml`, com o enunciado de cada invariante preservado na ADR-018. Este arquivo é
# o fiscal dessa etapa, e passou a ler as duas pontas: a etapa, para provar que o elo declaração↔
# fiscal existe; o ADR, para provar que o TEXTO não se perdeu na migração.
ADR = "architecture/adr/ADR-018-bancada-como-etapa-governada.md"


@pytest.fixture(scope="module")
def etapa(request) -> dict:
    doc = yaml.safe_load(
        (Path(request.config.rootpath) / "harness" / "stages.yaml").read_text(encoding="utf-8"))
    for s in doc.get("stages", []):
        if s.get("id") == "STAGE-DEPLOY":
            return s
    raise AssertionError(
        "STAGE-DEPLOY sumiu de harness/stages.yaml — `deploy/` voltou a não pertencer a etapa "
        "alguma, que é exatamente o estado que a ADR-018 recusou")


@pytest.fixture(scope="module")
def adr(request) -> str:
    return (Path(request.config.rootpath) / ADR).read_text(encoding="utf-8")


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
    """ADR-017: o compose constrói do clone no servidor; o produto não mora aqui."""
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


def test_subnet_declarada_e_a_observada_no_servidor(ambiente: dict[str, str]):
    """A subnet do exemplo do repositório do cockpit (172.19.0.0/16) NÃO é a deste servidor.

    Copiar o placeholder faz /api/session/unlock negar com 403 e ninguém entende por quê —
    o valor errado falha silenciosamente, que é o pior modo de falhar.
    """
    assert ambiente["TRUSTED_GATEWAY_CIDR"] == "192.168.32.0/20"


# --- o script de ingress edita config de PRODUÇÃO: precisa de rede de segurança ------------

def test_script_faz_backup_antes_de_editar(request):
    texto = (Path(request.config.rootpath) / SETUP).read_text(encoding="utf-8")
    assert "BACKUP=" in texto and "cp -a" in texto


def test_script_reverte_se_a_config_nao_validar(request):
    """`nginx -t` reprovado tem de restaurar o arquivo: um ingress que não recarrega trava a
    próxima alteração de quem vier depois, mesmo sem derrubar o que já está no ar."""
    texto = (Path(request.config.rootpath) / SETUP).read_text(encoding="utf-8")
    assert "reverter()" in texto
    assert "nginx -t" in texto
    # a reversão escreve no MESMO inode (bind-mount); rename quebraria o mount
    assert 'cat "$BACKUP" > "$INGRESS_CONF"' in texto


def test_script_recusa_credencial_identica_a_de_producao(request):
    texto = (Path(request.config.rootpath) / SETUP).read_text(encoding="utf-8")
    assert "cmp -s" in texto and "/etc/nginx/.htpasswd" in texto


# ---------------------------------------------------------------------------
# tetos de recurso
# ---------------------------------------------------------------------------
# Homologação divide o servidor com produção. Um ambiente de teste sem teto de
# memória pode derrubar o de verdade, e o OOM killer do kernel escolhe a vítima
# por heurística — pode levar o nginx, ou o banco de outra stack, e não o
# ofensor. Com teto, quem morre é o container que estourou, dentro do próprio
# cgroup, e o `restart: unless-stopped` o traz de volta.
#
# Os valores vêm de medição na bancada (42 containers, rajada de 300 requisições
# em 20 vias): 63 MiB de pico contra 512 de teto no app, 3,2 contra 64 no proxy.

@pytest.mark.parametrize("servico", ["app", "docker-socket-proxy"])
def test_todo_servico_tem_teto_de_memoria(compose: dict, servico: str):
    declarado = compose["services"][servico]
    assert declarado.get("mem_limit"), (
        f"{servico} sem mem_limit: um vazamento aqui derruba o servidor de produção")


@pytest.mark.parametrize("servico", ["app", "docker-socket-proxy"])
def test_swap_desligado(compose: dict, servico: str):
    """`memswap_limit` igual ao `mem_limit` desliga swap para o container.

    Sem isso o Docker concede o DOBRO em swap: em vez de bater no teto e morrer
    depressa, o processo que engorda passa a castigar o disco do host — que aqui
    é o mesmo disco de produção.
    """
    declarado = compose["services"][servico]
    assert declarado.get("memswap_limit") == declarado.get("mem_limit"), (
        f"{servico}: swap habilitado transforma estouro de memória em I/O do host")


@pytest.mark.parametrize("servico", ["app", "docker-socket-proxy"])
def test_teto_de_processos(compose: dict, servico: str):
    assert declarado_int(compose["services"][servico].get("pids_limit")) > 0, (
        f"{servico} sem pids_limit: fork descontrolado esgota a tabela do host")


def test_cpu_e_folgada_e_memoria_e_apertada(compose: dict):
    """A assimetria é deliberada, não descuido.

    CPU é recurso RECUPERÁVEL: sob disputa tudo fica mais lento e o escalonador
    resolve. Memória não — quem estoura mata terceiro. Estrangular a CPU do painel
    o deixaria lento exatamente quando o host está em apuros, que é quando alguém
    precisa dele.
    """
    app = compose["services"]["app"]
    assert float(app["cpus"]) >= 1.0, "CPU apertada estrangula o painel na hora do incidente"
    assert app["mem_limit"].endswith("m"), "teto de memória deve ser explícito em MiB"


def declarado_int(valor) -> int:
    return int(valor) if valor is not None else 0


# ---------------------------------------------------------------------------
# o escopo EXATO de "não age sobre a infraestrutura"
# ---------------------------------------------------------------------------
# A invariante 1 chamava-se "Homologação não tem superfície de escrita", e isso
# era FALSO — descoberto ao medir o alvo, não ao ler o compose.
# `POST /api/findings/{id}/ack` e `POST /api/tasks` não passam por
# ENABLE_ACTIONS: existem em qualquer instalação e aceitam escrita com um token
# de destravamento válido.
#
# O nome foi corrigido. Estes casos existem para que a correção não seja
# "consertada" na direção errada por quem ler o nome antigo em algum lugar.

def test_o_escopo_exato_sobreviveu_a_migracao(adr: str):
    """A aposentadoria das RULE-HOMOLOG só é aposentadoria se o TEXTO chegou do
    outro lado. Se este teste falhar, a migração virou apagamento: a exceção do
    `ack`/`tasks` volta a ser surpresa na próxima auditoria, e quem ler o nome
    antigo vai "consertar" o compose na direção errada.

    Nome que promete mais do que a regra entrega é pior que nome vago: ele
    dispensa a leitura do enunciado.
    """
    assert "INFRAESTRUTURA" in adr.upper(), (
        "o enunciado voltou a prometer ausência total de escrita")
    for termo in ("/ack", "/api/tasks", "ENABLE_ACTIONS"):
        assert termo in adr, (
            f"a ADR-018 não cita {termo} — o limite da invariante 1 se perdeu na migração")


def test_a_etapa_declara_um_fiscal_para_cada_invariante(etapa: dict):
    """O elo que faz STAGE-DEPLOY ser etapa governada e não etapa nominal.

    `check_stage_coverage` já confere que cada símbolo EXISTE, por AST. O que
    ele não confere é que os quatro estejam lá: uma etapa com um fiscal só
    resolve, e `deploy/` passaria a ter três invariantes sem vigia — partição
    fechada, evidência perdida, tudo verde. Esse é o defeito que a isenção teria
    tido, chegando por outro caminho.
    """
    simbolos = {e.get("symbol") for e in etapa.get("enforced_by", []) if e.get("symbol")}
    esperados = {
        "test_socket_proxy_nega_escrita_no_daemon",        # não age sobre a infraestrutura
        "test_container_nao_colide_com_producao",           # não colide com produção
        "test_script_recusa_credencial_identica_a_de_producao",  # não reusa a credencial
        "test_script_de_ingress_recusa_o_host_de_producao",      # não publica produção
    }
    assert esperados <= simbolos, f"invariante sem fiscal na etapa: {sorted(esperados - simbolos)}"
    # E os quatro têm de existir NESTE arquivo — a etapa aponta para cá.
    meu = Path(__file__).read_text(encoding="utf-8")
    for s in sorted(esperados):
        assert f"def {s}(" in meu, f"{s} é referenciado por STAGE-DEPLOY e não existe aqui"


def test_a_etapa_cobre_a_bancada_inteira(etapa: dict, request):
    """Artefato que não casa o diretório deixaria arquivo de `deploy/` fora da
    partição — o achado original, de volta pela porta dos fundos."""
    raiz = Path(request.config.rootpath)
    cobertos = {p for art in etapa.get("artifacts", []) for p in raiz.glob(f"{art}/**/*")}
    faltam = [p for p in raiz.glob("deploy/**/*") if p.is_file() and p not in cobertos]
    assert not faltam, f"arquivo de deploy/ fora dos artefatos da etapa: {faltam}"


def test_o_compose_nao_promete_ausencia_de_escrita(compose_texto: str):
    assert "superfície de escrita não deveria existir" not in compose_texto, (
        "voltou a afirmação que a medição desmentiu")


def test_a_declaracao_antiga_nao_ressuscitou(request):
    """Aposentadoria com migração tem um modo de falha próprio: alguém recria o
    arquivo de regras "para não perder o texto", e as invariantes passam a viver
    em dois lugares. Duas fontes de verdade divergem no primeiro PR que toca uma
    só — e a que ninguém lê é a que fica errada."""
    assert not (Path(request.config.rootpath) / "business/rules/homologacao.yaml").exists(), (
        "business/rules/homologacao.yaml voltou. O enunciado mora na ADR-018 e a mordida em "
        "STAGE-DEPLOY; recriar o arquivo restaura a segunda fonte de verdade que a fatia-4 tirou")


def test_a_excecao_esta_documentada_onde_o_operador_le(request):
    """No doc de subida, não só na regra: quem sobe o ambiente lê o passo a passo."""
    doc = (Path(request.config.rootpath) / "docs" / "HOMOLOGACAO.md").read_text(encoding="utf-8")
    assert "/ack" in doc and "/api/tasks" in doc, (
        "a exceção some do doc e vira surpresa na próxima auditoria")

# Subir a homologação do Docker Cockpit

Passo a passo para pôr no ar o alvo que esta harness tem permissão de auditar. Tudo roda **no
servidor** — nada aqui é executado pelo CI, e nada aqui toca produção.

Decisão de arquitetura por trás disto: [ADR-007](../architecture/adr/ADR-007-stack-de-homologacao-no-consumidor.md).
Regras que o ambiente precisa satisfazer: [`business/rules/homologacao.yaml`](../business/rules/homologacao.yaml),
fiscalizadas por [`tests/integration/test_homologacao.py`](../tests/integration/test_homologacao.py).

## O que muda em relação a produção

| | produção | homologação |
|---|---|---|
| container | `docker-cockpit` | `docker-cockpit-homolog` |
| socket-proxy | `docker-cockpit-proxy` (POST/DELETE **1**) | `docker-cockpit-proxy-homolog` (POST/DELETE **0**) |
| `ENABLE_ACTIONS` | `"1"` (pin deliberado) | `"0"` (pin oposto, também deliberado) |
| volume | `cockpit-data` | `cockpit-data-homolog` |
| basic auth | `.htpasswd` | `.htpasswd-homolog`, **credencial diferente** |
| retenção | 24h raw / 30d rollup | 6h raw / 7d rollup |

Homologação nasce **mais travada** que produção. É onde a régua cutuca, e ali não se mexe na
infraestrutura.

O que `ENABLE_ACTIONS` **não** cobre, e vale saber antes de auditar: `POST /api/findings/{id}/ack`
e `POST /api/tasks` existem em qualquer instalação e aceitam escrita com destravamento válido.
Elas gravam o estado do próprio painel — reconhecer um achado, abrir um cartão — no banco de
homologação, separado do de produção. É deliberado: triagem é leitura qualificada, e um ambiente
que não pode reconhecer um achado não exercita o fluxo que ele existe para exercitar.

## 1. DNS

Crie um registro **A** para `homolog.docker.danzeroum.com` apontando para o mesmo IP do
servidor. Espere propagar:

```bash
host homolog.docker.danzeroum.com
```

## 2. Credencial própria do basic auth — e a pegadinha do bind-mount

**Não reuse a de produção.** Se as duas forem iguais, o ambiente de teste vira uma segunda porta
para o mesmo servidor: quem obtiver a senha "de teste" entra na produção (RULE-HOMOLOG-003).

O obstáculo real, observado no servidor:

```
/opt/btv/ingress/.htpasswd -> /etc/nginx/.htpasswd     ← bind-mount de ARQUIVO
```

Bind-mount de arquivo **não traz vizinhos**. Criar `/opt/btv/ingress/.htpasswd-homolog` no host
não faz o arquivo existir dentro do container; `/etc/nginx/` lá dentro é o do próprio image.
Há duas saídas, e elas custam coisas diferentes:

### Opção A — montar um diretório (correta, exige recriar o ingress)

```bash
mkdir -p /opt/btv/ingress/htpasswd.d
cp -a /opt/btv/ingress/.htpasswd /opt/btv/ingress/htpasswd.d/producao
htpasswd -B -c /opt/btv/ingress/htpasswd.d/homolog qa-homolog   # senha NOVA
```

Depois, no compose do global-ingress, troque o mount de arquivo por um de diretório
(`/opt/btv/ingress/htpasswd.d:/etc/nginx/htpasswd.d:ro`), ajuste o `auth_basic_user_file` do
bloco de produção para `/etc/nginx/htpasswd.d/producao`, e recrie o container.

- **Custo:** segundos de indisponibilidade em **tudo** que o ingress serve — o cockpit,
  `docs-site`, a demo de governança, o portfólio e o educacional.
- **Ganho:** persistente. Sobrevive a `docker compose up -d`, a reboot e a recriação.

Depois de recriar, rode o script com o caminho novo:

```bash
HTPASSWD_HOMOLOG=/etc/nginx/htpasswd.d/homolog \
  bash deploy/homologacao/setup-ingress-homolog.sh homolog.docker.danzeroum.com
```

### Opção B — `docker cp` (sem indisponibilidade, mas efêmera)

```bash
htpasswd -B -c /opt/btv/ingress/.htpasswd-homolog qa-homolog    # senha NOVA
docker cp /opt/btv/ingress/.htpasswd-homolog btv-nginx-prod:/etc/nginx/.htpasswd-homolog
docker exec btv-nginx-prod test -f /etc/nginx/.htpasswd-homolog && echo "presente"
```

- **Custo:** o arquivo vive na camada gravável do container. **Some na primeira recriação do
  `btv-nginx-prod`** — e aí o `nginx.conf` passa a referenciar um `auth_basic_user_file`
  inexistente, o que faz `nginx -t` reprovar e **bloquear o próximo reload de produção**.
- **Quando serve:** para validar a homologação hoje, com a Opção A agendada para a próxima
  janela de manutenção.

> **O que NÃO fazer:** apontar a homologação para o `.htpasswd` de produção. É a saída fácil, e
> o script recusa — ele compara os dois arquivos e aborta se forem idênticos. Mudar isso exige
> mudar RULE-HOMOLOG-003 e a ADR-007, não um `-f`.

## 3. Ambiente

```bash
cd /opt/btv/projectCockpitDocker      # este repositório, no servidor
cp deploy/homologacao/.env.example deploy/homologacao/.env
$EDITOR deploy/homologacao/.env       # DOMAIN, BASIC_AUTH_*, TRUSTED_GATEWAY_CIDR, COCKPIT_SRC
```

`TRUSTED_GATEWAY_CIDR` é a subnet real da rede do ingress — sem ela, ou com ela errada, o unlock
nega com 403 (fail-closed, por desenho) e nada na tela explica o motivo:

```bash
docker network inspect btv-prod-net --format '{{range .IPAM.Config}}{{.Subnet}}{{end}}'
# observado em 2026-08-04: 192.168.32.0/20
```

> O `.env.example` do repositório do cockpit traz `172.19.0.0/16`. **Não é o valor deste
> servidor.** O `.example` daqui já vem com o observado, e um teste de integração trava a
> regressão — mas confirme mesmo assim: a subnet muda se a rede for recriada.

`COCKPIT_SRC` aponta para o clone de `danzeroum/docker` no servidor (padrão `/opt/btv/docker`).
O código do cockpit **não** vive neste repositório — o compose constrói a partir de lá.

> O `.env` real está no `.gitignore`. Se ele aparecer num `git status`, algo está errado.

## 4. Subir

```bash
docker compose -f deploy/homologacao/compose.yml --env-file deploy/homologacao/.env up -d
docker compose -f deploy/homologacao/compose.yml ps        # os dois healthy
docker exec docker-cockpit-homolog python3 -c \
  "import urllib.request;print(urllib.request.urlopen('http://localhost:8000/health').status)"
```

Depois publique no ingress (o script recusa o host de produção e exige o `.htpasswd` separado):

```bash
bash deploy/homologacao/setup-ingress-homolog.sh homolog.docker.danzeroum.com
```

## 5. Fechar `INCOMPLETE:target_url`

Com o ambiente no ar, a adoção sai do estado fail-closed. Duas mudanças:

**a) apontar o alvo** — em `tests/qa/config.yaml`:

```yaml
target:
  base_url: "https://homolog.docker.danzeroum.com"
  environment: staging
```

**b) autorizar o escopo** — o arquivo real **nunca** é comitado. Gere-o a partir do
`.example` e cadastre o conteúdo como o segredo `WEBQA_ESCOPO_AUTORIZADO` do repositório
(Settings → Secrets → Actions). O `qa.yml` já o monta no runner do job segregado.

```yaml
authorized: true
scope:
  hosts: ["homolog.docker.danzeroum.com"]
  paths_in_scope: ["/", "/api/*"]
  paths_excluded: ["/api/session/*"]
proof_of_possession:
  method: dns-txt
  reference: "webqa-ownership=<hash>"
authorization_expires: "2027-08-03"
```

Conferência:

```bash
python -m cockpit_harness pendencias   # deve não imprimir nada
python -m cockpit_harness alvo         # https://homolog.docker.danzeroum.com
```

Sem saída em `pendencias`, o job `inventory-and-passive` deixa de pular a auditoria e passa a
medir o alvo de verdade.

## 6. Conferir que as travas pegaram

```bash
# rotas de mutação não existem (404, não 403 — a diferença importa:
# 403 confirmaria que a rota existe e só falta credencial)
curl -u qa-homolog:SENHA -o /dev/null -w '%{http_code}\n' \
  -X POST https://homolog.docker.danzeroum.com/api/containers/x/restart

# o daemon nega escrita na origem, mesmo que a flag fosse ligada
docker exec docker-cockpit-homolog python3 -c \
  "import urllib.request as u; \
   print(u.urlopen(u.Request('http://docker-cockpit-proxy-homolog:2375/containers/x/restart', \
   method='POST')).status)"   # esperado: erro 403 do proxy
```

## 7. Derrubar

```bash
docker compose -f deploy/homologacao/compose.yml down       # mantém o banco
docker compose -f deploy/homologacao/compose.yml down -v    # apaga o banco DE HOMOLOGAÇÃO
```

O `-v` aqui é seguro justamente porque o volume é próprio (`cockpit-data-homolog`). Em produção
o mesmo comando apagaria 30 dias de série histórica.

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

Homologação nasce **mais travada** que produção. É onde a régua cutuca — superfície de escrita
ali não deveria existir.

## 1. DNS

Crie um registro **A** para `homolog.docker.danzeroum.com` apontando para o mesmo IP do
servidor. Espere propagar:

```bash
host homolog.docker.danzeroum.com
```

## 2. Credencial própria do basic auth

**Não reuse a de produção.** Se as duas forem iguais, o ambiente de teste vira uma segunda porta
para o mesmo servidor.

```bash
# no servidor
SENHA=$(openssl rand -base64 24); echo "guarde: $SENHA"
htpasswd -B -c /opt/btv/ingress/nginx/.htpasswd-homolog qa-homolog
# monte o arquivo no btv-nginx-prod como /etc/nginx/.htpasswd-homolog
docker exec btv-nginx-prod test -f /etc/nginx/.htpasswd-homolog && echo "montado"
```

## 3. Ambiente

```bash
cd /opt/btv/projectCockpitDocker      # este repositório, no servidor
cp deploy/homologacao/.env.example deploy/homologacao/.env
$EDITOR deploy/homologacao/.env       # DOMAIN, BASIC_AUTH_*, TRUSTED_GATEWAY_CIDR, COCKPIT_SRC
```

`TRUSTED_GATEWAY_CIDR` é a subnet real da rede do ingress — sem ela o unlock nega com 403
(fail-closed, por desenho):

```bash
docker network inspect btv-prod-net --format '{{range .IPAM.Config}}{{.Subnet}}{{end}}'
```

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

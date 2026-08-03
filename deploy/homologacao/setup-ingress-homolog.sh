#!/usr/bin/env bash
# setup-ingress-homolog.sh
#
# Emite o certificado TLS do host de HOMOLOGAÇÃO e acrescenta o bloco server{} no nginx do
# global-ingress (btv-nginx-prod), apontando para o upstream de homologação.
#
# Derivado de scripts/setup-ingress.sh de danzeroum/docker (commit 89ce0ae). Existe separado
# porque o script original fixa `proxy_pass http://docker-cockpit:8000` — o upstream de
# PRODUÇÃO. Reusá-lo publicaria o host de homologação servindo o cockpit de produção, com
# TLS válido e tudo: o pior tipo de erro, porque parece que funcionou.
#
# Uso: bash deploy/homologacao/setup-ingress-homolog.sh homolog.docker.danzeroum.com
# Pré-requisito: DNS A do domínio já apontando para este servidor, e o stack no ar.

set -euo pipefail

DOMAIN="${1:-}"
UPSTREAM="http://docker-cockpit-homolog:8000"
HTPASSWD="/etc/nginx/.htpasswd-homolog"
INGRESS_CONF="/opt/btv/ingress/nginx/nginx.conf"
CERTBOT_WWW="/var/www/certbot"
CERTBOT_CONF="/etc/letsencrypt"
EMAIL="${EMAIL:-admin@buildtovalue.cloud}"

if [[ -z "$DOMAIN" ]]; then
  echo "Uso: $0 <dominio-de-homologacao>   ex: $0 homolog.docker.danzeroum.com"
  exit 2
fi

# Trava de destino. Este script escreve um bloco que aponta para o upstream de homologação;
# rodá-lo com o host de produção sequestraria docker.danzeroum.com para o stack de teste.
if [[ "$DOMAIN" == "docker.danzeroum.com" ]]; then
  echo "ERRO: $DOMAIN é PRODUÇÃO. Este script publica o upstream de homologação."
  echo "      Para produção use scripts/setup-ingress.sh do repositório danzeroum/docker."
  exit 1
fi

echo "[1/5] Verificando DNS para $DOMAIN..."
if ! host "$DOMAIN" > /dev/null 2>&1; then
  echo "ERRO: DNS NXDOMAIN para $DOMAIN. Aponte um registro A para o IP deste servidor antes."
  exit 1
fi
echo "  OK: $(host "$DOMAIN" | head -1)"

echo "[2/5] Conferindo o upstream de homologação..."
if ! docker inspect docker-cockpit-homolog >/dev/null 2>&1; then
  echo "ERRO: container docker-cockpit-homolog não existe. Suba o stack antes:"
  echo "      docker compose -f deploy/homologacao/compose.yml --env-file deploy/homologacao/.env up -d"
  exit 1
fi
echo "  OK: docker-cockpit-homolog no ar."

echo "[3/5] Conferindo credencial própria em $HTPASSWD..."
if ! docker exec btv-nginx-prod test -f "$HTPASSWD" 2>/dev/null; then
  echo "ERRO: $HTPASSWD não existe dentro de btv-nginx-prod."
  echo "      Homologação NÃO reusa o .htpasswd de produção. Crie o arquivo com uma"
  echo "      credencial nova (htpasswd -B -c <arquivo> <usuario>) e monte-o no ingress."
  exit 1
fi
echo "  OK: credencial de homologação separada da de produção."

echo "[4/5] Emitindo certificado via certbot (webroot)..."
docker run --rm \
  -v "${CERTBOT_CONF}:/etc/letsencrypt" \
  -v "${CERTBOT_WWW}:/var/www/certbot" \
  certbot/certbot certonly \
    --webroot \
    --webroot-path /var/www/certbot \
    --non-interactive \
    --agree-tos \
    --email "$EMAIL" \
    -d "$DOMAIN"

echo "[5/5] Acrescentando bloco server{} em $INGRESS_CONF..."
if grep -q "server_name ${DOMAIN}" "$INGRESS_CONF"; then
  echo "  Bloco para $DOMAIN já existe — não vou reescrever."
  echo "  Confira à mão que o proxy_pass aponta para ${UPSTREAM}."
else
  TMPBLOCK=$(mktemp)
  cat > "$TMPBLOCK" <<NGINX

    # ---- docker-cockpit HOMOLOGACAO (${DOMAIN}) ----
    # Alvo autorizado da WebQA Suite. Upstream e .htpasswd SEPARADOS de producao.
    server {
        listen 80;
        server_name ${DOMAIN};
        location /.well-known/acme-challenge/ { root /var/www/certbot; }
        location / { return 301 https://\$host\$request_uri; }
    }
    server {
        listen 443 ssl;
        server_name ${DOMAIN};
        ssl_certificate     /etc/letsencrypt/live/${DOMAIN}/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/${DOMAIN}/privkey.pem;
        add_header Strict-Transport-Security "max-age=63072000" always;

        # Fora dos buscadores: um ambiente de teste indexado e um convite.
        add_header X-Robots-Tag "noindex, nofollow" always;

        auth_basic "Docker Cockpit (homologacao)";
        auth_basic_user_file ${HTPASSWD};

        location ~* (wp-login|\.git|\.env) { return 444; }
        location / {
            set \$upstream "${UPSTREAM}";
            proxy_pass \$upstream;

            proxy_set_header Host              \$host;
            proxy_set_header X-Real-IP         \$remote_addr;
            proxy_set_header X-Forwarded-For   \$proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto \$scheme;
            proxy_set_header Remote-User       \$remote_user;

            # SSE de /events: sem isto o stream morre a cada 60s e o proprio cockpit
            # dispara o achado stream_timeout contra si mesmo.
            proxy_http_version 1.1;
            proxy_set_header Connection "";
            proxy_buffering off;
            proxy_cache off;
            proxy_read_timeout 3600s;
            proxy_send_timeout 3600s;
        }
    }
NGINX

  python3 - "$INGRESS_CONF" "$TMPBLOCK" <<'PYEOF'
import sys, pathlib
conf_path = pathlib.Path(sys.argv[1])
block_path = pathlib.Path(sys.argv[2])
content = conf_path.read_text()
block = block_path.read_text()
conf_path.write_text(content.rstrip().rstrip('}').rstrip() + '\n' + block + '\n}\n')
print('  Bloco inserido em nginx.conf')
PYEOF

  rm -f "$TMPBLOCK"
fi

docker exec btv-nginx-prod nginx -t
docker exec btv-nginx-prod nginx -s reload

echo ""
echo "Pronto! Homologação em https://${DOMAIN}"
echo ""
echo "Próximo passo, no projectCockpitDocker: apontar tests/qa/config.yaml para este host"
echo "e injetar o escopo autorizado como segredo do CI. Ver docs/HOMOLOGACAO.md §5."

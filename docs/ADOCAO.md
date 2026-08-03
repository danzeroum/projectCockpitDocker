# Adoção do Docker Cockpit sob a harness padrão

Registro do que foi feito, contra o quê, e o que ficou pendente. Segue o playbook
`docs/COMO-ADOTAR.md` do molde (`danzeroum/project`), passo a passo.

## 0. As três fronteiras

| Papel | Repositório | Commit observado | O que é dono da verdade |
|---|---|---|---|
| **Padrão** (régua) | `danzeroum/qa-suite` @ `v1.0.0` | `305be2a587051b03be707690bbebfbe0da21a2f0` | motor, `checks/`, lista curada, gates |
| **Molde** (casca) | `danzeroum/project` | `319e533ae98cb678fa0be725e4ac00a7cd4ad291` | forma da harness |
| **Alvo** (negócio) | `danzeroum/docker` | `89ce0aed62dd870fb259b3c7a0b768524fcfea4e` | comportamento do Docker Cockpit |
| **Consumidor** | este repositório | — | alvo, thresholds, autorização, evidência |

O **código** do alvo não foi copiado para cá (ADR-007, que manteve essa parte da ADR-005); o
**stack de homologação**, sim — `deploy/homologacao/`, ver `docs/HOMOLOGACAO.md`. A régua **não**
foi copiada para cá (ADR-001, invariante 1).

## 1. Reconhecimento do alvo

`danzeroum/docker` — "Docker Cockpit": dashboard somente-leitura de containers.

- **Stack:** Python + FastAPI em `app/` (22 routers), frontend em `app/static/js/screens/`
  (10 telas), SQLite para série temporal, `docker-socket-proxy` no meio do caminho até o daemon.
- **Testes:** sim, 66 arquivos em `tests/` (`test_api.py`, `test_backend.py`,
  `test_acessibilidade.py`, …), CI própria em `.github/workflows/ci.yml` com Python 3.12 + Node 22.
- **App web publicada:** sim — servida por HTTPS pelo `global-ingress`, com basic auth.
- **Homologação:** **não existe**. O único host declarado é `docker.danzeroum.com`
  (`DOMAIN` no `.env.example`), que é produção. `grep -i 'homolog\|staging\|hml'` no repositório
  não retorna nada.
- **Domínios de negócio:** containers/imagens, armazenamento, capacidade, ingress/certificados,
  achados de segurança, resumo executivo, eventos e logs.

Consequência direta: **Trabalho B (inventário) habilitado; Trabalho A (auditoria) bloqueado** —
ver §5.

## 2. Casca copiada do molde

```
harness/                     plano de controle (harness.yaml, policies/, agents/, schemas/, prompts/)
tests/qa/                    config.yaml · campanha.yaml · escopo-autorizado.yaml.example
requirements-qa.txt          declara a régua (§4)
.github/workflows/qa.yml     inventário automático; carga/sondagem segregados
```

Também foi adotada a **camada de governança** (opcional no playbook, recomendada aqui porque o
cockpit evolui por agentes): `project.yaml`, `business/`, `architecture/`, `design/`,
`governance/`, `ci/validate_metadata.py`, `ci/generate_graph.py` e
`.github/workflows/validate-metadata.yml`.

Uma correção foi necessária em `harness/schemas/report.schema.json`: o schema herdava
`provenance.schema.json` por `allOf`, e como o bloco de procedência é `additionalProperties:
false`, nenhum laudo com `result`/`findings` passava. As referências agora são por propriedade.
A nota está no próprio arquivo.

## 3. O software desta adoção

O que vive em `src/cockpit_harness/` é o plano de controle, não o produto e não a régua:

| Módulo | Responsabilidade |
|---|---|
| `contrato.py` | pin exato, espelho, fronteira da régua, alvo e escopo (contrato §1-§3) |
| `plano.py` | quem dispara qual modo, higiene de ambiente (contrato §4) |
| `procedencia.py` | envelope do laudo e comparabilidade (contrato §5 e §7) |
| `codigos.py` | tabela de códigos de saída (contrato §6) |
| `cli.py` | `checar`, `versao`, `alvo`, `pendencias`, `modo`, `laudo` |

## 4. Versão da régua — descoberta e declarada

A versão foi lida da fonte real, não presumida:

```bash
grep -m1 '^version' qa-suite/webqa-suite/pyproject.toml   # version = "1.0.0"
```

E fixada em `requirements-qa.txt` (`webqa-suite==1.0.0`), com o espelho em
`tests/qa/config.yaml → standard_version`. O número **não** aparece em mais nenhum lugar: o CI
lê a versão com `python -m cockpit_harness versao`.

Realidade da instalação — **os dois caminhos estão fechados hoje**, e o primeiro run do CI provou
isso em vez de supor:

1. **PyPI:** a v1.0.0 não está publicada, e o `pyproject.toml` da suíte não declara
   `[build-system]` nem pacotes. `pip install -r requirements-qa.txt` responde
   `No matching distribution found for webqa-suite==1.0.0`.
2. **Git na tag exata:** `danzeroum/qa-suite` **não publica tag nenhuma** —
   `git ls-remote --tags` volta vazio, e o clone falha com
   `fatal: Remote branch v1.0.0 not found in upstream origin`. A versão 1.0.0 é real (está no
   `pyproject.toml` da suíte), mas ainda não é alcançável por ref.

O `qa.yml` trata isso como `suite_not_installed` (código 20) e **não** cai para `main`: uma régua
sem pin mede o alvo com uma fita que muda sozinha, e dois laudos deixariam de ser comparáveis sem
que ninguém percebesse. Fechar isso é **REQ-008**.

**Commit alvo da tag: `305be2a5`.** A régua andou durante a adoção (`090b7b43 → 305be2a5`), e a
diferença foi verificada antes de escolher: os dois commits declaram `version = "1.0.0"`, o hash
da lista curada é idêntico (`fadb9fd7…`) e `checks/`, `webqa/` e `data/` não têm diferença
nenhuma — mudou só `scripts/cockpit.py` e seu teste, a tela do relatório. A **superfície de
medição é byte a byte a mesma**; o que muda é o commit, e a fingerprint do contrato §7 inclui o
commit. Por isso este laudo foi regerado contra `305be2a5`: quando a tag for publicada, o que
`v1.0.0` resolve e o que o laudo carimba são o mesmo objeto.

Enquanto a ref não existir, o que ancora a régua é o **commit observado**, não a tag.

Isto não bloqueia nada hoje: o modo passivo já está recusado por `INCOMPLETE:target_url`, então a
indisponibilidade da régua só se torna operante depois que houver alvo.

## 5. Alvo — `INCOMPLETE:target_url`

**Ainda não há URL de homologação no ar para o Docker Cockpit.** Ver ADR-006. O que existe agora
é a bancada pronta para subir — `deploy/homologacao/` (ADR-007) e o passo a passo em
`docs/HOMOLOGACAO.md`; falta executá-lo no servidor (REQ-009). Até lá a configuração segue
fail-closed: `base_url` sob `.invalid` (RFC 2606), `python -m cockpit_harness pendencias` imprime

```
INCOMPLETE:target_url
INCOMPLETE:escopo-autorizado
```

e todo modo de rede é recusado com `SCOPE_MISSING` (12). Para fechar: `CP-001` em
`harness/change-proposals/` e REQ-005/006/007 no backlog.

## 6. Autorização

`tests/qa/escopo-autorizado.yaml.example` é versionado; o arquivo **real** está no `.gitignore` e
é montado no runner a partir do segredo `WEBQA_ESCOPO_AUTORIZADO`, só no job segregado.

## 7. Metadados

`business/capabilities.yaml`, `architecture/components.yaml`, `interfaces.yaml`,
`business/requirements/backlog.yaml`, `business/rules/*.yaml`, `governance/risk-register.yaml`,
`design/*` e `architecture/adr/` estão preenchidos e cruzados pelo fiscal. O mapa está em
`docs/metadata-graph.md` (derivado; `python ci/generate_graph.py --check` prova que está em dia).

## 8. Como rodar

```bash
# Trabalho B — INVENTÁRIO (sempre; sem rede, sem autorização)
pip install -e ".[dev]"
pytest -q
python -m cockpit_harness checar

# Governança
python ci/validate_metadata.py && python ci/generate_graph.py --check

# Trabalho A — PASSIVO (hoje recusado: sem alvo). Quando houver homologação e escopo:
git clone --depth 1 --branch "v$(python -m cockpit_harness versao)" \
  https://github.com/danzeroum/qa-suite /tmp/qa-suite
pip install -r /tmp/qa-suite/webqa-suite/requirements.txt
WEBQA_TARGET_URL="$(python -m cockpit_harness alvo)" \
  pytest -m "(backend or frontend or ux or seguranca or lgpd) and not load and not browser" \
  -c /tmp/qa-suite/webqa-suite/pytest.ini

# Métricas de renderização (FCP/LCP/CLS) — precisam de Chromium real: container da suíte
docker compose -f /tmp/qa-suite/docker/compose.yml run --rm campanha
```

Marcadores da régua: `backend, frontend, ux, functional, acceptance, lgpd, seguranca, browser,
load`.

## 9. Modos pesados

`load` e `active_discovery` existem só como job `workflow_dispatch` em `qa.yml`, com confirmação
textual (`confirmo`), `environment: production` (revisores obrigatórios) e os gates `WEBQA_*`
montados **apenas** naquele job. Nenhum agente e nenhum CI automático chega lá.

## 10. Evidência

`docs/laudo-adocao.json` (máquina) e `docs/laudo-adocao.md` (leitura) carimbam a procedência
deste run de inventário. Cada run do CI arquiva o seu em `harness/reports/` (gitignored).

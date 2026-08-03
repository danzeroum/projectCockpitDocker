# projectCockpitDocker

**Docker Cockpit sob a harness padrão.** Este repositório é o *consumidor*: ele declara a régua de
qualidade, autoriza (ou recusa) modos de execução e carimba a procedência de cada laudo produzido
sobre o [Docker Cockpit](https://github.com/danzeroum/docker).

O ponto de partida da arquitetura, em uma frase:

> **O projeto declara configuração e autorização; o padrão fornece o motor e as verificações.**

E o corolário que justifica tudo:

> **Uma trava que o vigiado pode desligar em silêncio não é uma trava.**

## As quatro fronteiras de confiança

| Camada | Onde vive | Dona da verdade | Contém |
|---|---|---|---|
| **Padrão — WebQA Suite** | `danzeroum/qa-suite` @ `v1.0.0` | julgamento de segurança | motor, `checks/`, lista curada, gates fail-closed |
| **Molde — harness** | `danzeroum/project` | forma da harness | casca declarativa, schemas, políticas |
| **Alvo — Docker Cockpit** | `danzeroum/docker` | comportamento do produto | FastAPI em `app/`, telas, testes próprios |
| **Consumidor** | **este repositório** | autorização + configuração | alvo, thresholds, escopo, versão exata da régua |

`webqa/`, `checks/` e `data/caminhos-sensiveis.yaml` **nunca** existem aqui: a régua é declarada
por versão, não copiada. O código do cockpit também não é vendorizado (ADR-005) — este repositório
é o plano de controle da adoção, não um fork do produto.

## Estado atual: fail-closed, por falta de alvo

```console
$ python -m cockpit_harness pendencias
INCOMPLETE:target_url
INCOMPLETE:escopo-autorizado
```

O Docker Cockpit publica um único host — `docker.danzeroum.com`, que é **produção**. Enquanto não
houver uma URL de homologação declarada, nenhum modo de rede roda: `passive`, `load` e
`active_discovery` são recusados com `SCOPE_MISSING` (12). O inventário (Trabalho B), esse sim,
roda sempre. Ver [ADR-006](architecture/adr/ADR-006-pendencia-em-vez-de-alvo-inventado.md) e
[`CP-001`](harness/change-proposals/CP-001-declarar-alvo-de-homologacao.yaml).

A bancada para destravar já está pronta em [`deploy/homologacao/`](deploy/homologacao/) — falta
subi-la no servidor. Passo a passo: [`docs/HOMOLOGACAO.md`](docs/HOMOLOGACAO.md).

## Os dois trabalhos

| Trabalho | Objeto | Rede | Autorização | Agente pode disparar |
|---|---|---|---|---|
| **B — Inventário** | o código deste repositório | não | não | ✅ sim |
| **A — Auditoria** | o cockpit publicado | sim | sim, conforme o modo | ⚠️ só passivo, com alvo já configurado |

## Layout

```
projectCockpitDocker/
├── project.yaml            identidade, criticidade, donos, governança
├── business/               visão + capacidades + rules/ + requirements/
├── architecture/           componentes + interfaces + adr/
├── design/                 sistema de design e superfícies de UI do ALVO
├── governance/             registro de riscos
├── deploy/homologacao/     a bancada: compose + ingress do alvo que a régua pode auditar
├── src/cockpit_harness/    o software desta adoção (contrato, plano, procedência, CLI)
├── tests/
│   ├── unit/ integration/ e2e/   os quatro níveis — entrada do inventário
│   └── qa/                 config.yaml · campanha.yaml · escopo-autorizado.yaml.example
├── harness/                plano de controle (policies, agents, schemas, prompts)
├── ci/                     fiscais executáveis (metadados + diagrama derivado)
├── requirements-qa.txt     FONTE ÚNICA da versão da régua
└── docs/                   ADOCAO.md · laudo-adocao.{md,json} · metadata-graph.md
```

## Rodar

```bash
pip install -e ".[dev]"
pytest -q                                   # inventário: os quatro níveis
python -m cockpit_harness checar            # verificação do contrato de consumo
python ci/validate_metadata.py              # fiscal dos metadados
python ci/generate_graph.py --check         # diagrama derivado em dia
```

A auditoria contra o alvo publicado está descrita em [`docs/ADOCAO.md`](docs/ADOCAO.md) §8 — e
hoje é recusada, por desenho.

## Leitura

- [`docs/ADOCAO.md`](docs/ADOCAO.md) — o que foi adotado, contra o quê, e o que ficou pendente.
- [`docs/laudo-adocao.md`](docs/laudo-adocao.md) — o laudo, com procedência carimbada.
- [`WEBQA_CONSUMER_CONTRACT.md`](WEBQA_CONSUMER_CONTRACT.md) — o contrato normativo com a suíte.
- [`architecture/adr/`](architecture/adr/) — as decisões e por que elas custam o que custam.

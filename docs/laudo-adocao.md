# Laudo da adoção — inventário (Trabalho B)

> Leitura humana do artefato de máquina `docs/laudo-adocao.json`, que é a fonte. Regenerar com:
> `python -m cockpit_harness laudo --modo inventory --runner ci --regua <clone-da-suite> --saida docs/laudo-adocao.json`

## Procedência — qual régua produziu estes números

| Campo | Valor |
|---|---|
| `standard.name` | `webqa-suite` |
| `standard.version` | `1.0.0` — lida de `requirements-qa.txt` (fonte única) |
| `standard.commit` | `090b7b4336e513a327d33713ea9bb2272262faa1` |
| `standard.sensitive_paths_hash` | `sha256:fadb9fd75759537ea924df49f7b18938bd69c5b7e6dad562a1190d2b755400f3` |
| `consumer_project.repository` | `danzeroum/projectCockpitDocker` |
| `consumer_project.commit` | commit do HEAD quando o inventário rodou — anterior ao commit da adoção, porque o laudo é gerado antes de ser versionado |
| `execution.run_id` | `2026-08-03T22-40-00Z` |
| `execution.mode` | `inventory` |
| `execution.network_used` | `false` |
| `execution.active_gates` | `[]` |
| `result` | `ok` |

O `sensitive_paths_hash` é o SHA-256 de `webqa-suite/data/caminhos-sensiveis.yaml` no commit
acima. Ele entra; a lista não. Dois laudos com a mesma versão e hashes diferentes provam que
alguém editou a régua — e a agregação responde `not_comparable` (31) em vez de somar.

## O que foi medido

Inventário: os testes deste repositório, sem rede e sem autorização.

| Nível | Arquivos | O que cobre |
|---|---|---|
| Unidade | `tests/unit/` (3) | limites do contrato, matriz de modos, procedência |
| Integração | `tests/integration/` (3) | repositório real, workflows do CI, fiscal de metadados |
| Sistema | `tests/e2e/test_cli_laudo.py` | códigos de saída da CLI, ponta a ponta |
| Aceitação | `tests/e2e/test_checklist_adocao.py` | o checklist de "pronto" do playbook, item por item |

**113 testes, 113 passando.** `ci/validate_metadata.py` sai 0; `ci/generate_graph.py --check`
confirma o diagrama em dia.

## O que NÃO foi medido, e por quê

Nada do Docker Cockpit publicado. Nenhuma requisição foi emitida — `network_used: false`.

| Pendência | Consequência |
|---|---|
| `INCOMPLETE:target_url` | `danzeroum/docker` só publica `docker.danzeroum.com` (produção). Sem host de homologação, os modos `passive`, `load` e `active_discovery` são recusados com `SCOPE_MISSING` (12). |
| `INCOMPLETE:escopo-autorizado` | O escopo real não é comitado; ele é injetado como segredo do CI e ainda não existe. |

Isto é resultado, não omissão: um laudo passivo apontado para produção mediria o servidor real —
o cockpit fala com o daemon Docker através do socket-proxy. Ver ADR-006 e `CP-001`.

## Verificação da fronteira

| Invariante | Estado |
|---|---|
| `webqa/`, `checks/`, `data/caminhos-sensiveis.yaml` ausentes | ✅ (`test_a_regua_nao_foi_copiada`) |
| Pin exato `==` igual ao `standard_version` | ✅ `1.0.0` == `1.0.0` |
| Versão em fonte única (nenhum outro arquivo restata o número) | ✅ (`test_plano_referencia_o_arquivo_de_pin_sem_restatar_a_versao`) |
| `escopo-autorizado.yaml` real não comitado, e no `.gitignore` | ✅ |
| `load`/`active_discovery` só em `workflow_dispatch` | ✅ (`test_modo_pesado_nunca_e_automatico`) |
| Ambiente do agente sem `WEBQA_*`, abortando se houver | ✅ (`DENIED_ENV` = 10) |

> Nota sobre o grep textual: procurar as *strings* `webqa/`, `checks/` ou
> `data/caminhos-sensiveis.yaml` neste repositório retorna resultados — em comentários, nas
> políticas e no passo de guarda do `qa.yml`, que precisa nomear o que recusa. O que a invariante
> proíbe é a **existência dos caminhos**, verificada com `test -e` no CI e por
> `contrato.regua_copiada()` no inventário. Ambos vazios.

## Comparabilidade

Este é o laudo-base. O próximo run só é comparável a ele se a fingerprint
`(name, version, commit, sensitive_paths_hash, schema_version)` for idêntica. Subir a régua de
versão é um PR próprio, com o laudo anterior e o novo lado a lado
(`harness/policies/dependency-updates.md`).

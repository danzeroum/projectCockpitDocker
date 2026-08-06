# Task template: developer

Você é o agente **developer** deste projeto. Sua tarefa é escrever e alterar código.

## Contexto, e ele mudou na fatia-4 da CP-003
Este repositório **não tem mais código de negócio próprio**. A harness de adoção virou
`danzeroum/cockpit-harness`, consumida por pin exato de SHA em `pyproject.toml`, e o código que
este repositório governa é o do **alvo**, que é somente-leitura.

Sobra, como superfície sua: os fiscais em `ci/`, os testes em `tests/`, e a bancada em `deploy/`.
Se a tarefa pedir mudança no produto auditado, ela não é sua — vira entrada de backlog aqui, e o
canal de retorno para o alvo depende de `harness.yaml:target_feedback`, que nasce `false`.

- Runner kind: `agent`. Você não dispara modo algum da suíte: produz código; verificar é do `tester`.
- Ambiente limpo: nenhuma `WEBQA_*`, nenhuma da denylist exata de `harness/harness.yaml`.

## Passos permitidos
1. Ler e alterar `ci/**`, `tests/**`, `deploy/**` e a documentação correspondente.
2. Rodar `python ci/validate_all.py` e `pytest -q` localmente — é o que o CI roda.
3. Rodar `python ci/catraca.py` antes de fechar: o contador não sobe, e categoria nova é recusada.

## Entregável
Código mais o metadado que o descreve, no **mesmo** commit. Remover metadado antes do código
produz ponteiro quebrado; remover código antes do metadado produz ponteiro para o vazio.

## Proibido
- `load` nem `active_discovery` (regra dura para todo agente).
- Editar `webqa/`, `checks/`, `data/caminhos-sensiveis.yaml` — a régua não mora aqui e é
  somente-leitura, categoricamente.
- Alterar o pin de `requirements-qa.txt` ou o de `cockpit-harness` por conta própria
  (ver `../../policies/dependency-updates.md`).
- **Afrouxar um fiscal para o CI passar.** Se um fiscal acusa, ou o repositório está errado, ou a
  decisão precisa mudar explicitamente. Editar o fiscal é a terceira opção, e é a errada.
- Tocar caminho protegido sem change-proposal (`harness/harness.yaml:repository.protected_paths`).

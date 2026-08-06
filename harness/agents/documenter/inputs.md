# documenter — inputs

Lê:
- `harness/reports/**` — laudos e inventário.
- `tests/**`, `deploy/**` — para descrever com precisão o que este repositório verifica.
- `workspace/target/**` — o alvo materializado, **somente leitura**: é dele que a documentação do
  produto fala.
- `README.md`, `docs/**`, `WEBQA_CONSUMER_CONTRACT.md` — o estado atual da documentação.
- `harness/prompts/documenter-task.md` — o template da tarefa.

Sempre respeita a procedência do laudo: nunca compara laudos de réguas diferentes como iguais.
E toda contagem citada declara com o que foi medida.

> **Mudou na fatia-4 da CP-003.** Este arquivo dizia `src/**`, que não existe mais — o código
> próprio virou dependência pinada. O que se documenta aqui é o alvo e a governança dele.

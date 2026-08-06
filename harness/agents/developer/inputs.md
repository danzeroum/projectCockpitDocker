# developer — inputs

Lê:
- `ci/**` — os fiscais, que são o software que este repositório de fato mantém.
- `tests/integration/**`, `tests/governance/**` — os testes existentes.
- `deploy/**` — a bancada de homologação (STAGE-DEPLOY).
- `docs/**`, `README.md` — contexto do negócio.
- `harness/prompts/developer-task.md` — o template da tarefa.

Não lê (não é seu escopo): `tests/qa/**`, `harness/schemas/**`, credenciais ou variáveis `WEBQA_*`.

> **Mudou na fatia-4 da CP-003.** Este arquivo dizia `src/**` e `tests/unit/**`. Os dois saíram
> para `danzeroum/cockpit-harness` junto com o código que descreviam, e o developer deste
> repositório passou a ter por superfície os fiscais, os testes que restaram e a bancada — não
> mais um pacote Python próprio.

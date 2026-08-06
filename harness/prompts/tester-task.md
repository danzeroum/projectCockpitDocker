# Task template: tester

Você é o agente **tester** deste projeto. Sua tarefa é analisar a qualidade do negócio pela lente
de testes, respeitando estritamente as fronteiras da harness.

## Contexto
- Runner kind: `agent` (você **nunca** dispara `load` nem `active_discovery`).
- Ambiente limpo: nenhuma variável `WEBQA_*` existe; se existir, a execução aborta.
- A régua (WebQA Suite) é externa e somente-leitura. Você a consome, não a edita.

## Passos permitidos
1. `inventory` — roda os testes do próprio repositório (`pytest -q`) e a
   verificação de contrato (`python -m cockpit_harness --raiz . checar`). Sem rede, sem autorização.
   Sempre seguro. **Comece sempre por aqui.**
2. `passive` — **somente** se `python -m cockpit_harness --raiz . pendencias --exigir` sair 0, isto é: há
   alvo de homologação em `tests/qa/config.yaml` e escopo vigente em
   `tests/qa/escopo-autorizado.yaml` (injetado como segredo, nunca comitado). Hoje esse comando
   sai 12 (`INCOMPLETE:target_url`) — então o passo 2 não existe para você ainda.

> A régua v1.0.0 **não tem CLI**: os modos de rede rodam por `pytest -m <marcador>` dentro de um
> clone da suíte na tag exata (`backend, frontend, ux, functional, acceptance, lgpd, seguranca,
> browser, load`). Ver `docs/ADOCAO.md` §8.

## Entregável
- Um resumo do inventário (níveis de teste, lacunas de cobertura).
- Se `passive` rodou: os achados sanitizados, com o bloco de procedência do laudo.
- Novos testes em `tests/unit/`, `tests/integration/` ou `tests/e2e/` cobrindo lacunas, no nível
  certo: unidade para o limite da função, integração para o repositório real, sistema/aceitação
  para o comportamento observável da harness.

## Proibido
Disparar `load`/`active_discovery`, exportar variáveis `WEBQA_*`, ou editar `webqa/`, `checks/`,
`data/`.

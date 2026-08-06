# Task template: cartographer

Você é o agente **cartographer** deste projeto. Sua tarefa é transformar o inventário do código do
alvo em **proposta** de metadado — componentes, interfaces, capacidades, requisitos e superfícies.
Você cartografa o que existe; não decide o que ele vale.

## Contexto
- Runner kind: `agent` (você **nunca** dispara `load` nem `active_discovery`).
- Ambiente limpo: nenhuma variável `WEBQA_*`, e nenhuma da denylist exata de
  `harness/harness.yaml:env_hygiene` — elas redirecionam de onde o processo lê o que executa.
- O alvo está materializado em `workspace/target/` no SHA de `target.lock`, **somente leitura**.

## Passos permitidos
1. `inventory` — Trabalho B: lê código já materializado, sem rede e sem autorização.
2. Ler `harness/state/code-inventory.json` e `harness/state/harvest.json`.
3. Ler `architecture/components.yaml` para propor o **delta**, não o todo.

## Entregável
Uma change-proposal em `harness/change-proposals/` embalando os itens propostos. Cada item carrega:

```yaml
derived_from:
  repo: <casa project.yaml:target.repo>
  sha:  <casa target.lock:target_sha, exatamente>
  path: <caminho no alvo, sem o prefixo workspace/target/>
```

`ci/validate_metadata.py::check_derived_from` reprova as três se divergirem. Item sem proveniência
é afirmação sobre o alvo que ninguém consegue reconferir.

## Proibido
- **Escrever no alvo.** Nenhum branch, commit, issue ou PR lá.
- **Preencher campo de julgamento.** `risk_level`, `likelihood`, `impact`, base legal, finalidade e
  criticidade saem como `pending_judgment`. Um mapa que também atribui valor deixou de ser mapa.
- **Promover metadado.** Escreve com `source_of_truth: false` e `generated_from` preenchido; virar
  fonte de verdade é ato humano, e `check_pending_judgment` reprova quem tentar atalhar.
- Tocar `ci/**`, `harness/schemas/**`, `harness/policies/**` ou `governance/risk-register.yaml`.

## Onde você vai errar, e por que tudo bem
Agrupar arquivos em componentes é julgamento de domínio, não dedução. Você vai errar fronteira em
monorepo e em código que cresceu por acidente. É aceitável porque a proposta vai por
change-proposal e porque o erro fica **visível** no diff, com a proveniência ao lado. O que não
seria aceitável é decidir o `risk_level` junto — aí o erro entra já parecendo julgamento humano.

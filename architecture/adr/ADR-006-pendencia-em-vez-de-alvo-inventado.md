# ADR-006 — Sem homologação declarada, a saída é uma pendência; nunca produção

- **Status:** accepted
- **Data:** 2026-08-03
- **Capacidades relacionadas:** CAP-ALVO, CAP-CONTRATO
- **Riscos relacionados:** RISK-ALVO-001, RISK-SEGREDO-001

## Contexto

O reconhecimento de `danzeroum/docker` (commit `89ce0ae`) mostrou uma app publicada, mas **uma só
URL**: `docker.danzeroum.com`, declarada como `DOMAIN` no `.env.example` — produção. Não há host de
homologação em lugar nenhum do repositório (`grep -i 'homolog\|staging\|hml'` não retorna nada).

Faltando o alvo, existem três saídas possíveis e duas delas são ruins:

1. apontar a auditoria para produção "porque era a URL que existia";
2. deixar `base_url` com um valor qualquer e seguir como se estivesse configurado;
3. declarar a pendência e recusar todo modo de rede até que alguém preencha.

A primeira transforma um teste em incidente — o cockpit fala com o daemon Docker de um servidor real.
A segunda é pior que a primeira: cria um alvo silenciosamente errado, e o laudo passa a medir outra
coisa sem dizer.

## Decisão

`tests/qa/config.yaml` declara `base_url` sob o TLD reservado `.invalid` (RFC 2606 — nunca resolve).
`cockpit_harness.contrato` trata qualquer host `.invalid` como **ausência de alvo**, e a situação do
consumidor passa a listar a pendência textual `INCOMPLETE:target_url`.

Enquanto a pendência existir:

- `passive`, `load` e `active_discovery` são recusados com `SCOPE_MISSING` (12) — fail-closed;
- só o inventário (Trabalho B, sem rede) roda;
- o laudo committado registra a pendência no bloco `summary`, em vez de omiti-la.

O `escopo-autorizado.yaml` **real** nunca é comitado: o repositório versiona apenas o `.example`, e o
`.gitignore` recusa o arquivo real. A autorização entra como segredo do CI.

## Consequências

- "Não medido, e eis por quê" é um resultado legítimo — melhor que um número sem objeto.
- Preencher o alvo é um PR pequeno e explícito: trocar a `base_url`, injetar o escopo, remover a
  pendência. O teste de aceitação passa a exigir `environment != production`.
- Custo: nenhum dado de qualidade do cockpit sai desta adoção até que a homologação exista. É o
  preço de não auditar produção por automação.

## Fiscal

`src/cockpit_harness/contrato.py::situacao` (pendência) e `::exigir_rede_liberada` (recusa 12);
`tests/e2e/test_checklist_adocao.py` (alvo de homologação ou pendência declarada; segredo não
comitado); `tests/e2e/test_cli_laudo.py` (laudo passivo recusado sem alvo).

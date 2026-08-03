# ADR-005 — O alvo auditado mora em `danzeroum/docker`; este repositório é o plano de controle

- **Status:** accepted
- **Data:** 2026-08-03
- **Capacidades relacionadas:** CAP-ALVO
- **Riscos relacionados:** RISK-ALVO-001

## Contexto

A adoção tem três repositórios com donos da verdade diferentes:

| Papel | Repositório | Dono da verdade |
|---|---|---|
| **Padrão** (régua) | `danzeroum/qa-suite` @ `v1.0.0` | julgamento de segurança |
| **Molde** (casca) | `danzeroum/project` | forma da harness |
| **Alvo** (negócio) | `danzeroum/docker` — o Docker Cockpit, FastAPI em `app/` | comportamento do produto |

Este repositório (`danzeroum/projectCockpitDocker`) é o **consumidor**: ele declara a régua, autoriza
modos e arquiva evidência sobre o Docker Cockpit. A tentação óbvia é copiar o cockpit para cá "para o
inventário ter o que catalogar".

## Decisão

O código do Docker Cockpit **não é vendorizado**. Ele permanece em `danzeroum/docker`, e este
repositório referencia o alvo por (a) `base_url` em `tests/qa/config.yaml`, para os modos de rede, e
(b) prosa versionada em `docs/ADOCAO.md`, que registra o commit observado no reconhecimento.

O software que vive aqui é o da própria adoção: verificação do contrato de consumo, roteamento de
modo e procedência de laudo (`src/cockpit_harness/`). É ele que o inventário cataloga.

## Consequências

- Uma cópia do cockpit envelheceria em silêncio: o laudo mediria um código que já não é o publicado.
- O inventário deste repositório é honesto e pequeno — cataloga o plano de controle, não o produto.
- Custo: a rastreabilidade `capacidade → código` do cockpit fica no repositório dele; aqui as
  capacidades declaradas com `source_paths` são as da adoção. `CAP-ALVO` fica `planned` porque, deste
  lado, ela é auditoria a executar — não código a manter.
- Se um dia o cockpit adotar a harness dentro do próprio repositório, esta ADR é substituída, não
  contornada.

## Fiscal

`ci/validate_metadata.py` (só exige `source_paths`/`test_paths` físicos para capacidade
`implemented`/`verified`, e recusa caminho de código fora de `src/`);
`tests/e2e/test_checklist_adocao.py::test_a_regua_nao_foi_copiada`.

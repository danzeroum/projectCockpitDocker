<!-- GENERATED: não editar; rodar ci/alignment_report.py -->
<!-- O --check do CI contradiz qualquer edição manual: edita-se a FONTE, não o derivado. -->
# Alinhamento entre departamentos

Matriz derivada do metadado declarado. Ela responde a pergunta que os demais fiscais não
fazem: **o que ficou de fora?**

## Cobertura de risco por capacidade

| Capacidade | risk_level | Riscos que a cobrem |
|---|---|---|
| `CAP-AGIR` | high | `RISK-ALVO-002`, `RISK-SOCKET-001` |
| `CAP-DIAGNOSTICAR` | high | `RISK-DIAG-001` |
| `CAP-NARRAR` | medium | — |
| `CAP-OBSERVAR` | medium | — |
| `CAP-SUSTENTAR` | medium | — |

## Componentes

| Componente | Status | Capacidade | Implementa | Coberto por risco |
|---|---|---|---|---|
| `CMP-ACHADOS` | verified | `CAP-DIAGNOSTICAR` | REQ-004, REQ-014 | não |
| `CMP-APP` | verified | `CAP-SUSTENTAR` | — | não |
| `CMP-ATUALIZACOES` | verified | `CAP-DIAGNOSTICAR` | REQ-008 | não |
| `CMP-BARREIRA-ACOES` | verified | `CAP-AGIR` | — | não |
| `CMP-CERTS` | verified | `CAP-DIAGNOSTICAR` | REQ-006 | não |
| `CMP-CONTAINERS` | verified | `CAP-OBSERVAR` | REQ-001, REQ-002 | não |
| `CMP-DRIFT` | verified | `CAP-DIAGNOSTICAR` | REQ-007 | não |
| `CMP-EMPACOTAMENTO` | implemented | `CAP-SUSTENTAR` | — | não |
| `CMP-EVENTOS` | verified | `CAP-NARRAR` | REQ-015 | não |
| `CMP-INGRESS` | verified | `CAP-DIAGNOSTICAR` | REQ-009 | não |
| `CMP-INVENTARIO-HOST` | verified | `CAP-OBSERVAR` | REQ-003 | não |
| `CMP-LOGS-BUSCA` | verified | `CAP-NARRAR` | REQ-027 | não |
| `CMP-MASCARAMENTO` | verified | `CAP-SUSTENTAR` | — | não |
| `CMP-NOTIFICACOES` | verified | `CAP-NARRAR` | REQ-018 | não |
| `CMP-OPERACOES` | verified | `CAP-AGIR` | REQ-010, REQ-011, REQ-013 | não |
| `CMP-PERSISTENCIA` | verified | `CAP-SUSTENTAR` | — | não |
| `CMP-POLITICA-RESPOSTA` | verified | `CAP-SUSTENTAR` | — | não |
| `CMP-PROXY` | verified | `CAP-OBSERVAR` | — | não |
| `CMP-REGRAS-ACHADO` | verified | `CAP-DIAGNOSTICAR` | REQ-005 | não |
| `CMP-RESUMO` | verified | `CAP-NARRAR` | REQ-017 | não |
| `CMP-SERIES` | verified | `CAP-NARRAR` | REQ-016, REQ-025 | não |
| `CMP-SESSAO` | verified | `CAP-AGIR` | REQ-012 | não |
| `CMP-TELA-ATENCAO` | implemented | `CAP-NARRAR` | REQ-018, REQ-020 | não |
| `CMP-TELA-AUDITORIA` | implemented | `CAP-NARRAR` | REQ-020 | não |
| `CMP-TELA-BACKEND` | implemented | `CAP-NARRAR` | REQ-024 | não |
| `CMP-TELA-CAPACIDADE` | implemented | `CAP-NARRAR` | REQ-016 | não |
| `CMP-TELA-EXECUTIVO` | implemented | `CAP-NARRAR` | REQ-017 | não |
| `CMP-TELA-INGRESS` | implemented | `CAP-NARRAR` | REQ-020 | não |
| `CMP-TELA-PLANTAO` | implemented | `CAP-NARRAR` | REQ-022 | não |
| `CMP-TELA-PROJETOS` | implemented | `CAP-NARRAR` | REQ-020 | não |
| `CMP-TELA-TAREFAS` | implemented | `CAP-NARRAR` | REQ-020 | não |
| `CMP-TELA-TOPOLOGIA` | implemented | `CAP-NARRAR` | REQ-020 | não |
| `CMP-UI-CASCA` | implemented | `CAP-NARRAR` | REQ-023, REQ-026 | não |
| `CMP-UI-INFRA` | implemented | `CAP-NARRAR` | REQ-018, REQ-020 | não |
| `CMP-UI-KERNEL` | implemented | `CAP-NARRAR` | REQ-020, REQ-021 | não |
| `CMP-UI-MODULOS-INLINE` | implemented | `CAP-NARRAR` | REQ-020, REQ-021 | não |

## Riscos por área

| Área | Total | Abertos |
|---|---|---|
| access | 4 | 2 |
| availability | 2 | 2 |
| dependencies | 1 | 0 |
| governance | 5 | 2 |
| webqa | 1 | 0 |

## Pendências de alinhamento

Nenhuma. Todo ativo relevante está coberto ou tem isenção declarada.

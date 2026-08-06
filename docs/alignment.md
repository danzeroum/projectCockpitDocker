<!-- GENERATED: não editar; rodar ci/alignment_report.py -->
<!-- O --check do CI contradiz qualquer edição manual: edita-se a FONTE, não o derivado. -->
# Alinhamento entre departamentos

Matriz derivada do metadado declarado. Ela responde a pergunta que os demais fiscais não
fazem: **o que ficou de fora?**

## Cobertura de risco por capacidade

| Capacidade | risk_level | Riscos que a cobrem |
|---|---|---|
| `CAP-AGIR` | high | — |
| `CAP-DIAGNOSTICAR` | high | — |
| `CAP-NARRAR` | medium | — |
| `CAP-OBSERVAR` | medium | — |
| `CAP-SUSTENTAR` | medium | — |

## Componentes

| Componente | Status | Capacidade | Implementa | Coberto por risco |
|---|---|---|---|---|
| `CMP-ACHADOS` | verified | `CAP-DIAGNOSTICAR` | — | não |
| `CMP-APP` | verified | `CAP-SUSTENTAR` | — | não |
| `CMP-ATUALIZACOES` | verified | `CAP-DIAGNOSTICAR` | — | não |
| `CMP-BARREIRA-ACOES` | verified | `CAP-AGIR` | — | não |
| `CMP-CERTS` | verified | `CAP-DIAGNOSTICAR` | — | não |
| `CMP-CONTAINERS` | verified | `CAP-OBSERVAR` | — | não |
| `CMP-DRIFT` | verified | `CAP-DIAGNOSTICAR` | — | não |
| `CMP-EMPACOTAMENTO` | implemented | `CAP-SUSTENTAR` | — | não |
| `CMP-EVENTOS` | verified | `CAP-NARRAR` | — | não |
| `CMP-INGRESS` | verified | `CAP-DIAGNOSTICAR` | — | não |
| `CMP-INVENTARIO-HOST` | verified | `CAP-OBSERVAR` | — | não |
| `CMP-LOGS-BUSCA` | verified | `CAP-NARRAR` | — | não |
| `CMP-MASCARAMENTO` | verified | `CAP-SUSTENTAR` | — | não |
| `CMP-NOTIFICACOES` | verified | `CAP-NARRAR` | — | não |
| `CMP-OPERACOES` | verified | `CAP-AGIR` | — | não |
| `CMP-PERSISTENCIA` | verified | `CAP-SUSTENTAR` | — | não |
| `CMP-POLITICA-RESPOSTA` | verified | `CAP-SUSTENTAR` | — | não |
| `CMP-PROXY` | verified | `CAP-OBSERVAR` | — | não |
| `CMP-REGRAS-ACHADO` | verified | `CAP-DIAGNOSTICAR` | — | não |
| `CMP-RESUMO` | verified | `CAP-NARRAR` | — | não |
| `CMP-SERIES` | verified | `CAP-NARRAR` | — | não |
| `CMP-SESSAO` | verified | `CAP-AGIR` | — | não |
| `CMP-TELA-ATENCAO` | implemented | `CAP-NARRAR` | — | não |
| `CMP-TELA-AUDITORIA` | implemented | `CAP-NARRAR` | — | não |
| `CMP-TELA-BACKEND` | implemented | `CAP-NARRAR` | — | não |
| `CMP-TELA-CAPACIDADE` | implemented | `CAP-NARRAR` | — | não |
| `CMP-TELA-EXECUTIVO` | implemented | `CAP-NARRAR` | — | não |
| `CMP-TELA-INGRESS` | implemented | `CAP-NARRAR` | — | não |
| `CMP-TELA-PLANTAO` | implemented | `CAP-NARRAR` | — | não |
| `CMP-TELA-PROJETOS` | implemented | `CAP-NARRAR` | — | não |
| `CMP-TELA-TAREFAS` | implemented | `CAP-NARRAR` | — | não |
| `CMP-TELA-TOPOLOGIA` | implemented | `CAP-NARRAR` | — | não |
| `CMP-UI-CASCA` | implemented | `CAP-NARRAR` | — | não |
| `CMP-UI-INFRA` | implemented | `CAP-NARRAR` | — | não |
| `CMP-UI-KERNEL` | implemented | `CAP-NARRAR` | — | não |
| `CMP-UI-MODULOS-INLINE` | implemented | `CAP-NARRAR` | — | não |

## Riscos por área

| Área | Total | Abertos |
|---|---|---|
| access | 4 | 2 |
| availability | 1 | 1 |
| dependencies | 1 | 0 |
| governance | 5 | 2 |
| webqa | 1 | 0 |

## Pendências de alinhamento

- **[high]** `FIND-ALIGN-R1-CAP-AGIR` — CAP-AGIR é risk_level 'high' e nenhum RISK-* a referencia em 'related' — risco reconhecido em campo e invisível na governança.
- **[high]** `FIND-ALIGN-R1-CAP-DIAGNOSTICAR` — CAP-DIAGNOSTICAR é risk_level 'high' e nenhum RISK-* a referencia em 'related' — risco reconhecido em campo e invisível na governança.
- **[medium]** `FIND-ALIGN-R3-UI-COCKPIT-EXECUTIVO` — UI-COCKPIT-EXECUTIVO não satisfaz requisito algum — ou o requisito sumiu, ou a tela não deveria existir. As duas respostas são acionáveis; o silêncio não.
- **[medium]** `FIND-ALIGN-R3-UI-COCKPIT-PAINEL` — UI-COCKPIT-PAINEL não satisfaz requisito algum — ou o requisito sumiu, ou a tela não deveria existir. As duas respostas são acionáveis; o silêncio não.
- **[medium]** `FIND-ALIGN-R4-CMP-ACHADOS` — CMP-ACHADOS está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-APP` — CMP-APP está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-ATUALIZACOES` — CMP-ATUALIZACOES está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-BARREIRA-ACOES` — CMP-BARREIRA-ACOES está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-CERTS` — CMP-CERTS está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-CONTAINERS` — CMP-CONTAINERS está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-DRIFT` — CMP-DRIFT está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-EMPACOTAMENTO` — CMP-EMPACOTAMENTO está 'implemented' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-EVENTOS` — CMP-EVENTOS está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-INGRESS` — CMP-INGRESS está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-INVENTARIO-HOST` — CMP-INVENTARIO-HOST está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-LOGS-BUSCA` — CMP-LOGS-BUSCA está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-MASCARAMENTO` — CMP-MASCARAMENTO está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-NOTIFICACOES` — CMP-NOTIFICACOES está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-OPERACOES` — CMP-OPERACOES está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-PERSISTENCIA` — CMP-PERSISTENCIA está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-POLITICA-RESPOSTA` — CMP-POLITICA-RESPOSTA está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-PROXY` — CMP-PROXY está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-REGRAS-ACHADO` — CMP-REGRAS-ACHADO está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-RESUMO` — CMP-RESUMO está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-SERIES` — CMP-SERIES está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-SESSAO` — CMP-SESSAO está 'verified' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-TELA-ATENCAO` — CMP-TELA-ATENCAO está 'implemented' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-TELA-AUDITORIA` — CMP-TELA-AUDITORIA está 'implemented' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-TELA-BACKEND` — CMP-TELA-BACKEND está 'implemented' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-TELA-CAPACIDADE` — CMP-TELA-CAPACIDADE está 'implemented' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-TELA-EXECUTIVO` — CMP-TELA-EXECUTIVO está 'implemented' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-TELA-INGRESS` — CMP-TELA-INGRESS está 'implemented' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-TELA-PLANTAO` — CMP-TELA-PLANTAO está 'implemented' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-TELA-PROJETOS` — CMP-TELA-PROJETOS está 'implemented' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-TELA-TAREFAS` — CMP-TELA-TAREFAS está 'implemented' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-TELA-TOPOLOGIA` — CMP-TELA-TOPOLOGIA está 'implemented' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-UI-CASCA` — CMP-UI-CASCA está 'implemented' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-UI-INFRA` — CMP-UI-INFRA está 'implemented' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-UI-KERNEL` — CMP-UI-KERNEL está 'implemented' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.
- **[medium]** `FIND-ALIGN-R4-CMP-UI-MODULOS-INLINE` — CMP-UI-MODULOS-INLINE está 'implemented' e não implementa requisito nem é coberto por regra verificada da sua capacidade — código maduro cuja razão de existir ninguém registrou.

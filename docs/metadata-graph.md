# Mapa de relacionamento dos metadados

> **Gerado** por `ci/generate_graph.py` a partir dos metadados reais. Não editar à mão —
> regenerar com `python ci/generate_graph.py`. É um artefato derivado, não fonte de verdade.

Legenda: azul-escuro = projeto · azul = capacidade (`CAP-`) · ciano = componente (`CMP-`) ·
roxo = interface (`IFC-`) · verde = regra (`RULE-`) · rosa = superfície de UI (`UI-`) ·
amarelo = ADR · vermelho = risco (`RISK-`).

```mermaid
graph TD
  PROJ_danzeroum_projectcockpitdocker["danzeroum-projectcockpitdocker"]
  TEST_tests_e2e_test_checklist_adocao_py{{"test_checklist_adocao.py"}}
  TEST_tests_e2e_test_cli_laudo_py{{"test_cli_laudo.py"}}
  TEST_tests_integration_test_repositorio_py{{"test_repositorio.py"}}
  TEST_tests_integration_test_workflows_py{{"test_workflows.py"}}
  TEST_tests_unit_test_contrato_py{{"test_contrato.py"}}
  TEST_tests_unit_test_plano_py{{"test_plano.py"}}
  TEST_tests_unit_test_procedencia_py{{"test_procedencia.py"}}
  CAP_ALVO["CAP-ALVO<br/>Auditoria do Docker Cockpit publicado"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_ALVO
  CAP_CONTRATO["CAP-CONTRATO<br/>Conformidade com o contrato de consumo"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_CONTRATO
  CAP_MODOS["CAP-MODOS<br/>Roteamento de modo e higiene de ambiente"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_MODOS
  CAP_PROCEDENCIA["CAP-PROCEDENCIA<br/>Procedência e comparabilidade do laudo"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_PROCEDENCIA
  CMP_CLI["CMP-CLI<br/>cli.py"]
  CMP_CLI -->|realiza| CAP_PROCEDENCIA
  CMP_CLI -->|depende| CMP_CONTRATO
  CMP_CLI -->|depende| CMP_PLANO
  CMP_CLI -->|depende| CMP_PROCEDENCIA
  CMP_CLI -.->|implementa| REQ_003
  CMP_CLI -.->|testa| TEST_tests_e2e_test_cli_laudo_py
  CMP_CONTRATO["CMP-CONTRATO<br/>contrato.py"]
  CMP_CONTRATO -->|realiza| CAP_CONTRATO
  CMP_CONTRATO -.->|implementa| REQ_001
  CMP_CONTRATO -.->|testa| TEST_tests_integration_test_repositorio_py
  CMP_CONTRATO -.->|testa| TEST_tests_unit_test_contrato_py
  CMP_PLANO["CMP-PLANO<br/>plano.py"]
  CMP_PLANO -->|realiza| CAP_MODOS
  CMP_PLANO -->|depende| CMP_CONTRATO
  CMP_PLANO -.->|implementa| REQ_002
  CMP_PLANO -.->|implementa| REQ_004
  CMP_PLANO -.->|testa| TEST_tests_integration_test_workflows_py
  CMP_PLANO -.->|testa| TEST_tests_unit_test_plano_py
  CMP_PROCEDENCIA["CMP-PROCEDENCIA<br/>procedencia.py"]
  CMP_PROCEDENCIA -->|realiza| CAP_PROCEDENCIA
  CMP_PROCEDENCIA -->|depende| CMP_CONTRATO
  CMP_PROCEDENCIA -.->|implementa| REQ_003
  CMP_PROCEDENCIA -.->|testa| TEST_tests_unit_test_procedencia_py
  IFC_CLI(["IFC-CLI<br/>Porta de linha de comando da harness"])
  CMP_CLI -.->|provê| IFC_CLI
  IFC_CONTRATO(["IFC-CONTRATO<br/>Situação verificada do consumidor"])
  CMP_CONTRATO -.->|provê| IFC_CONTRATO
  IFC_CONTRATO -.->|consome| CMP_CLI
  IFC_CONTRATO -.->|consome| CMP_PLANO
  IFC_CONTRATO -.->|consome| CMP_PROCEDENCIA
  IFC_PLANO(["IFC-PLANO<br/>Roteamento de modo por runner-kind"])
  CMP_PLANO -.->|provê| IFC_PLANO
  IFC_PLANO -.->|consome| CMP_CLI
  IFC_PROCEDENCIA(["IFC-PROCEDENCIA<br/>Envelope de laudo com procedência"])
  CMP_PROCEDENCIA -.->|provê| IFC_PROCEDENCIA
  IFC_PROCEDENCIA -.->|consome| CMP_CLI
  RULE_CONTRATO_001["RULE-CONTRATO-001"]
  CAP_CONTRATO -->|regra| RULE_CONTRATO_001
  RULE_CONTRATO_001 -.->|verifica| TEST_tests_integration_test_repositorio_py
  RULE_CONTRATO_001 -.->|verifica| TEST_tests_unit_test_contrato_py
  RULE_CONTRATO_002["RULE-CONTRATO-002"]
  CAP_CONTRATO -->|regra| RULE_CONTRATO_002
  RULE_CONTRATO_002 -.->|verifica| TEST_tests_unit_test_contrato_py
  RULE_CONTRATO_003["RULE-CONTRATO-003"]
  CAP_CONTRATO -->|regra| RULE_CONTRATO_003
  RULE_CONTRATO_003 -.->|verifica| TEST_tests_e2e_test_checklist_adocao_py
  RULE_CONTRATO_003 -.->|verifica| TEST_tests_unit_test_contrato_py
  RULE_CONTRATO_004["RULE-CONTRATO-004"]
  CAP_CONTRATO -->|regra| RULE_CONTRATO_004
  RULE_CONTRATO_004 -.->|verifica| TEST_tests_e2e_test_checklist_adocao_py
  RULE_CONTRATO_004 -.->|verifica| TEST_tests_unit_test_contrato_py
  RULE_CONTRATO_005["RULE-CONTRATO-005"]
  CAP_CONTRATO -->|regra| RULE_CONTRATO_005
  RULE_CONTRATO_005 -.->|verifica| TEST_tests_unit_test_contrato_py
  RULE_MODOS_001["RULE-MODOS-001"]
  CAP_MODOS -->|regra| RULE_MODOS_001
  RULE_MODOS_001 -.->|verifica| TEST_tests_unit_test_plano_py
  RULE_MODOS_002["RULE-MODOS-002"]
  CAP_MODOS -->|regra| RULE_MODOS_002
  RULE_MODOS_002 -.->|verifica| TEST_tests_e2e_test_cli_laudo_py
  RULE_MODOS_002 -.->|verifica| TEST_tests_integration_test_workflows_py
  RULE_MODOS_002 -.->|verifica| TEST_tests_unit_test_plano_py
  RULE_MODOS_003["RULE-MODOS-003"]
  CAP_MODOS -->|regra| RULE_MODOS_003
  RULE_MODOS_003 -.->|verifica| TEST_tests_e2e_test_cli_laudo_py
  RULE_MODOS_003 -.->|verifica| TEST_tests_unit_test_plano_py
  RULE_MODOS_004["RULE-MODOS-004"]
  CAP_MODOS -->|regra| RULE_MODOS_004
  RULE_MODOS_004 -.->|verifica| TEST_tests_integration_test_repositorio_py
  RULE_PROCEDENCIA_001["RULE-PROCEDENCIA-001"]
  CAP_PROCEDENCIA -->|regra| RULE_PROCEDENCIA_001
  RULE_PROCEDENCIA_001 -.->|verifica| TEST_tests_e2e_test_checklist_adocao_py
  RULE_PROCEDENCIA_001 -.->|verifica| TEST_tests_unit_test_procedencia_py
  RULE_PROCEDENCIA_002["RULE-PROCEDENCIA-002"]
  CAP_PROCEDENCIA -->|regra| RULE_PROCEDENCIA_002
  RULE_PROCEDENCIA_002 -.->|verifica| TEST_tests_unit_test_procedencia_py
  RULE_PROCEDENCIA_003["RULE-PROCEDENCIA-003"]
  CAP_PROCEDENCIA -->|regra| RULE_PROCEDENCIA_003
  RULE_PROCEDENCIA_003 -.->|verifica| TEST_tests_unit_test_procedencia_py
  RULE_PROCEDENCIA_004["RULE-PROCEDENCIA-004"]
  CAP_PROCEDENCIA -->|regra| RULE_PROCEDENCIA_004
  RULE_PROCEDENCIA_004 -.->|verifica| TEST_tests_unit_test_procedencia_py
  UI_COCKPIT_EXECUTIVO["UI-COCKPIT-EXECUTIVO"]
  UI_COCKPIT_EXECUTIVO -->|experiência| CAP_ALVO
  UI_COCKPIT_PAINEL["UI-COCKPIT-PAINEL"]
  UI_COCKPIT_PAINEL -->|experiência| CAP_ALVO
  MET_COMPARAVEL[["MET-COMPARAVEL"]]
  MET_FRONTEIRA[["MET-FRONTEIRA"]]
  MET_PENDENCIA[["MET-PENDENCIA"]]
  REQ_001["REQ-001<br/>done"]
  REQ_001 -->|requisito| CAP_CONTRATO
  REQ_001 ==>|move| MET_COMPARAVEL
  REQ_001 -.->|regido por| RULE_CONTRATO_001
  REQ_001 -.->|regido por| RULE_CONTRATO_002
  REQ_001 -.->|validado por| TEST_tests_integration_test_repositorio_py
  REQ_001 -.->|validado por| TEST_tests_unit_test_contrato_py
  REQ_002["REQ-002<br/>done"]
  REQ_002 -->|requisito| CAP_MODOS
  REQ_002 -.->|regido por| RULE_MODOS_001
  REQ_002 -.->|regido por| RULE_MODOS_002
  REQ_002 -.->|validado por| TEST_tests_integration_test_workflows_py
  REQ_002 -.->|validado por| TEST_tests_unit_test_plano_py
  REQ_003["REQ-003<br/>done"]
  REQ_003 -->|requisito| CAP_PROCEDENCIA
  REQ_003 ==>|move| MET_COMPARAVEL
  REQ_003 -.->|regido por| RULE_PROCEDENCIA_001
  REQ_003 -.->|regido por| RULE_PROCEDENCIA_002
  REQ_003 -.->|regido por| RULE_PROCEDENCIA_003
  REQ_003 -.->|validado por| TEST_tests_e2e_test_cli_laudo_py
  REQ_003 -.->|validado por| TEST_tests_unit_test_procedencia_py
  REQ_004["REQ-004<br/>done"]
  REQ_004 -->|requisito| CAP_MODOS
  REQ_004 -.->|regido por| RULE_MODOS_003
  REQ_004 -.->|validado por| TEST_tests_e2e_test_cli_laudo_py
  REQ_004 -.->|validado por| TEST_tests_unit_test_plano_py
  REQ_005["REQ-005<br/>proposed"]
  REQ_005 -->|requisito| CAP_ALVO
  REQ_005 ==>|move| MET_PENDENCIA
  REQ_006["REQ-006<br/>proposed"]
  REQ_006 -->|requisito| CAP_ALVO
  REQ_006 -.->|depende| REQ_005
  REQ_006 ==>|move| MET_PENDENCIA
  REQ_007["REQ-007<br/>proposed"]
  REQ_007 -->|requisito| CAP_ALVO
  REQ_007 -.->|depende| REQ_005
  REQ_007 -.->|depende| REQ_006
  REQ_007 ==>|move| MET_PENDENCIA
  REQ_008["REQ-008<br/>proposed"]
  REQ_008 -->|requisito| CAP_CONTRATO
  REQ_008 ==>|move| MET_COMPARAVEL
  REQ_008 -.->|regido por| RULE_CONTRATO_002
  RISK_ALVO_001["RISK-ALVO-001"]
  RISK_CHANGE_001["RISK-CHANGE-001"]
  RISK_DEP_001["RISK-DEP-001"]
  RISK_META_001["RISK-META-001"]
  RISK_SEGREDO_001["RISK-SEGREDO-001"]
  RISK_WEBQA_001["RISK-WEBQA-001"]
  ADR_001["ADR-001"]
  ADR_001 -->|decide| CAP_CONTRATO
  ADR_001 -->|mitiga| RISK_WEBQA_001
  ADR_002["ADR-002"]
  ADR_002 -->|mitiga| RISK_META_001
  ADR_003["ADR-003"]
  ADR_003 -->|decide| CAP_CONTRATO
  ADR_003 -->|decide| CAP_PROCEDENCIA
  ADR_003 -->|decide| CMP_CONTRATO
  ADR_003 -->|decide| CMP_PROCEDENCIA
  ADR_003 -->|mitiga| RISK_DEP_001
  ADR_004["ADR-004"]
  ADR_004 -->|mitiga| RISK_CHANGE_001
  ADR_005["ADR-005"]
  ADR_005 -->|decide| CAP_ALVO
  ADR_005 -->|mitiga| RISK_ALVO_001
  ADR_006["ADR-006"]
  ADR_006 -->|decide| CAP_ALVO
  ADR_006 -->|decide| CAP_CONTRATO
  ADR_006 -->|decide| CMP_CONTRATO
  ADR_006 -->|mitiga| RISK_ALVO_001
  ADR_006 -->|mitiga| RISK_SEGREDO_001
  classDef project fill:#1f2937,stroke:#111827,color:#fff;
  class PROJ_danzeroum_projectcockpitdocker project;
  classDef cap fill:#2563eb,stroke:#1e40af,color:#fff;
  class CAP_ALVO,CAP_CONTRATO,CAP_MODOS,CAP_PROCEDENCIA cap;
  classDef cmp fill:#0891b2,stroke:#0e7490,color:#fff;
  class CMP_CLI,CMP_CONTRATO,CMP_PLANO,CMP_PROCEDENCIA cmp;
  classDef ifc fill:#7c3aed,stroke:#5b21b6,color:#fff;
  class IFC_CLI,IFC_CONTRATO,IFC_PLANO,IFC_PROCEDENCIA ifc;
  classDef rule fill:#16a34a,stroke:#15803d,color:#fff;
  class RULE_CONTRATO_001,RULE_CONTRATO_002,RULE_CONTRATO_003,RULE_CONTRATO_004,RULE_CONTRATO_005,RULE_MODOS_001,RULE_MODOS_002,RULE_MODOS_003,RULE_MODOS_004,RULE_PROCEDENCIA_001,RULE_PROCEDENCIA_002,RULE_PROCEDENCIA_003,RULE_PROCEDENCIA_004 rule;
  classDef ui fill:#db2777,stroke:#9d174d,color:#fff;
  class UI_COCKPIT_EXECUTIVO,UI_COCKPIT_PAINEL ui;
  classDef req fill:#0d9488,stroke:#0f766e,color:#fff;
  class REQ_001,REQ_002,REQ_003,REQ_004,REQ_005,REQ_006,REQ_007,REQ_008 req;
  classDef met fill:#ea580c,stroke:#c2410c,color:#fff;
  class MET_COMPARAVEL,MET_FRONTEIRA,MET_PENDENCIA met;
  classDef test fill:#57534e,stroke:#44403c,color:#fff;
  class TEST_tests_e2e_test_checklist_adocao_py,TEST_tests_e2e_test_cli_laudo_py,TEST_tests_integration_test_repositorio_py,TEST_tests_integration_test_workflows_py,TEST_tests_unit_test_contrato_py,TEST_tests_unit_test_plano_py,TEST_tests_unit_test_procedencia_py test;
  classDef adr fill:#ca8a04,stroke:#a16207,color:#fff;
  class ADR_001,ADR_002,ADR_003,ADR_004,ADR_005,ADR_006 adr;
  classDef risk fill:#dc2626,stroke:#991b1b,color:#fff;
  class RISK_ALVO_001,RISK_CHANGE_001,RISK_DEP_001,RISK_META_001,RISK_SEGREDO_001,RISK_WEBQA_001 risk;
```

<!-- GENERATED: não editar; rodar ci/generate_graph.py -->
# Mapa de relacionamento dos metadados

> Artefato DERIVADO dos metadados reais, não fonte de verdade. Editar aqui é trabalho
> perdido: o `--check` do CI contradiz a edição na hora mais cara.

Legenda: azul-escuro = projeto · azul = capacidade (`CAP-`) · ciano = componente (`CMP-`) ·
roxo = interface (`IFC-`) · verde = regra (`RULE-`) · rosa = superfície de UI (`UI-`) ·
amarelo = ADR · vermelho = risco (`RISK-`).

```mermaid
graph TD
  PROJ_danzeroum_projectcockpitdocker["danzeroum-projectcockpitdocker"]
  TEST_tests_e2e_test_checklist_adocao_py{{"test_checklist_adocao.py"}}
  TEST_tests_e2e_test_cli_laudo_py{{"test_cli_laudo.py"}}
  TEST_tests_integration_test_fase_c_py{{"test_fase_c.py"}}
  TEST_tests_integration_test_homologacao_py{{"test_homologacao.py"}}
  TEST_tests_integration_test_repositorio_py{{"test_repositorio.py"}}
  TEST_tests_integration_test_workflows_py{{"test_workflows.py"}}
  TEST_tests_unit_test_contrato_py{{"test_contrato.py"}}
  TEST_tests_unit_test_escopo_regua_py{{"test_escopo_regua.py"}}
  TEST_tests_unit_test_plano_py{{"test_plano.py"}}
  TEST_tests_unit_test_procedencia_py{{"test_procedencia.py"}}
  TEST_tests_unit_test_veredito_py{{"test_veredito.py"}}
  TEST_workspace_target_tests_test_acessibilidade_py{{"test_acessibilidade.py"}}
  TEST_workspace_target_tests_test_ack_audit_py{{"test_ack_audit.py"}}
  TEST_workspace_target_tests_test_api_py{{"test_api.py"}}
  TEST_workspace_target_tests_test_cabecalhos_seguranca_py{{"test_cabecalhos_seguranca.py"}}
  TEST_workspace_target_tests_test_cache_py{{"test_cache.py"}}
  TEST_workspace_target_tests_test_cache_http_py{{"test_cache_http.py"}}
  TEST_workspace_target_tests_test_capacidade_cards_py{{"test_capacidade_cards.py"}}
  TEST_workspace_target_tests_test_capacidade_serie_curta_py{{"test_capacidade_serie_curta.py"}}
  TEST_workspace_target_tests_test_certs_sprint5_py{{"test_certs_sprint5.py"}}
  TEST_workspace_target_tests_test_ciclo_acao_sintetico_py{{"test_ciclo_acao_sintetico.py"}}
  TEST_workspace_target_tests_test_config_ingress_path_py{{"test_config_ingress_path.py"}}
  TEST_workspace_target_tests_test_container_history_py{{"test_container_history.py"}}
  TEST_workspace_target_tests_test_db_py{{"test_db.py"}}
  TEST_workspace_target_tests_test_deploy_credencial_py{{"test_deploy_credencial.py"}}
  TEST_workspace_target_tests_test_drift_b8_py{{"test_drift_b8.py"}}
  TEST_workspace_target_tests_test_events_rota_py{{"test_events_rota.py"}}
  TEST_workspace_target_tests_test_events_v11_py{{"test_events_v11.py"}}
  TEST_workspace_target_tests_test_executive_py{{"test_executive.py"}}
  TEST_workspace_target_tests_test_f6_palette_py{{"test_f6_palette.py"}}
  TEST_workspace_target_tests_test_findings_py{{"test_findings.py"}}
  TEST_workspace_target_tests_test_frescor_amostra_py{{"test_frescor_amostra.py"}}
  TEST_workspace_target_tests_test_guarda_docs_registro_py{{"test_guarda_docs_registro.py"}}
  TEST_workspace_target_tests_test_guarda_schema_literal_py{{"test_guarda_schema_literal.py"}}
  TEST_workspace_target_tests_test_hardening_b11_py{{"test_hardening_b11.py"}}
  TEST_workspace_target_tests_test_history_route_py{{"test_history_route.py"}}
  TEST_workspace_target_tests_test_ingress_parser_py{{"test_ingress_parser.py"}}
  TEST_workspace_target_tests_test_kernel_cockpit_py{{"test_kernel_cockpit.py"}}
  TEST_workspace_target_tests_test_logs_fts_v13_py{{"test_logs_fts_v13.py"}}
  TEST_workspace_target_tests_test_logs_texto_py{{"test_logs_texto.py"}}
  TEST_workspace_target_tests_test_metrics_py{{"test_metrics.py"}}
  TEST_workspace_target_tests_test_metrics_prom_py{{"test_metrics_prom.py"}}
  TEST_workspace_target_tests_test_migration_py{{"test_migration.py"}}
  TEST_workspace_target_tests_test_no_backup_py{{"test_no_backup.py"}}
  TEST_workspace_target_tests_test_notify_v15_py{{"test_notify_v15.py"}}
  TEST_workspace_target_tests_test_offline_py{{"test_offline.py"}}
  TEST_workspace_target_tests_test_projects_security_py{{"test_projects_security.py"}}
  TEST_workspace_target_tests_test_prune_sintetico_py{{"test_prune_sintetico.py"}}
  TEST_workspace_target_tests_test_prune_v12_py{{"test_prune_v12.py"}}
  TEST_workspace_target_tests_test_regras_container_parado_py{{"test_regras_container_parado.py"}}
  TEST_workspace_target_tests_test_render_vivo_py{{"test_render_vivo.py"}}
  TEST_workspace_target_tests_test_rotas_rail_py{{"test_rotas_rail.py"}}
  TEST_workspace_target_tests_test_sampler_py{{"test_sampler.py"}}
  TEST_workspace_target_tests_test_session_py{{"test_session.py"}}
  TEST_workspace_target_tests_test_sinais_de_maturidade_py{{"test_sinais_de_maturidade.py"}}
  TEST_workspace_target_tests_test_storage_py{{"test_storage.py"}}
  TEST_workspace_target_tests_test_summary_py{{"test_summary.py"}}
  TEST_workspace_target_tests_test_tasks_py{{"test_tasks.py"}}
  TEST_workspace_target_tests_test_tasks_api_py{{"test_tasks_api.py"}}
  TEST_workspace_target_tests_test_telas_renderizam_py{{"test_telas_renderizam.py"}}
  TEST_workspace_target_tests_test_telas_topologia_plantao_py{{"test_telas_topologia_plantao.py"}}
  TEST_workspace_target_tests_test_unlock_v8_py{{"test_unlock_v8.py"}}
  TEST_workspace_target_tests_test_updates_ui_py{{"test_updates_ui.py"}}
  TEST_workspace_target_tests_test_updates_v14_py{{"test_updates_v14.py"}}
  CAP_AGIR["CAP-AGIR<br/>Executar mutação operacional sob barreira e auditoria"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_AGIR
  CAP_ALVO["CAP-ALVO<br/>Auditoria do Docker Cockpit publicado"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_ALVO
  CAP_CONTRATO["CAP-CONTRATO<br/>Conformidade com o contrato de consumo"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_CONTRATO
  CAP_DIAGNOSTICAR["CAP-DIAGNOSTICAR<br/>Transformar o estado observado em achados acionáveis"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_DIAGNOSTICAR
  CAP_MODOS["CAP-MODOS<br/>Roteamento de modo e higiene de ambiente"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_MODOS
  CAP_NARRAR["CAP-NARRAR<br/>Entregar o estado ao operador: fluxo, séries e notificação"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_NARRAR
  CAP_OBSERVAR["CAP-OBSERVAR<br/>Observar o estado do daemon Docker de um host"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_OBSERVAR
  CAP_PROCEDENCIA["CAP-PROCEDENCIA<br/>Procedência e comparabilidade do laudo"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_PROCEDENCIA
  CAP_SUSTENTAR["CAP-SUSTENTAR<br/>Servir a aplicação com política declarada de resposta e dados"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_SUSTENTAR
  CMP_ACHADOS["CMP-ACHADOS<br/>__init__.py"]
  CMP_ACHADOS -->|realiza| CAP_DIAGNOSTICAR
  CMP_ACHADOS -->|depende| CMP_PERSISTENCIA
  CMP_ACHADOS -->|depende| CMP_PROXY
  CMP_ACHADOS -->|depende| CMP_SERIES
  CMP_ACHADOS -->|depende| CMP_SESSAO
  CMP_ACHADOS -.->|testa| TEST_workspace_target_tests_test_f6_palette_py
  CMP_ACHADOS -.->|testa| TEST_workspace_target_tests_test_findings_py
  CMP_ACHADOS -.->|testa| TEST_workspace_target_tests_test_guarda_schema_literal_py
  CMP_ACHADOS -.->|testa| TEST_workspace_target_tests_test_regras_container_parado_py
  CMP_ACHADOS -.->|testa| TEST_workspace_target_tests_test_telas_topologia_plantao_py
  CMP_APP["CMP-APP<br/>app.py"]
  CMP_APP -->|realiza| CAP_SUSTENTAR
  CMP_APP -->|depende| CMP_ACHADOS
  CMP_APP -->|depende| CMP_ATUALIZACOES
  CMP_APP -->|depende| CMP_CERTS
  CMP_APP -->|depende| CMP_CONTAINERS
  CMP_APP -->|depende| CMP_DRIFT
  CMP_APP -->|depende| CMP_EVENTOS
  CMP_APP -->|depende| CMP_INGRESS
  CMP_APP -->|depende| CMP_INVENTARIO_HOST
  CMP_APP -->|depende| CMP_LOGS_BUSCA
  CMP_APP -->|depende| CMP_NOTIFICACOES
  CMP_APP -->|depende| CMP_OPERACOES
  CMP_APP -->|depende| CMP_PERSISTENCIA
  CMP_APP -->|depende| CMP_POLITICA_RESPOSTA
  CMP_APP -->|depende| CMP_PROXY
  CMP_APP -->|depende| CMP_RESUMO
  CMP_APP -->|depende| CMP_SERIES
  CMP_APP -->|depende| CMP_SESSAO
  CMP_APP -.->|testa| TEST_workspace_target_tests_test_api_py
  CMP_APP -.->|testa| TEST_workspace_target_tests_test_offline_py
  CMP_APP -.->|testa| TEST_workspace_target_tests_test_telas_renderizam_py
  CMP_ATUALIZACOES["CMP-ATUALIZACOES<br/>updates.py"]
  CMP_ATUALIZACOES -->|realiza| CAP_DIAGNOSTICAR
  CMP_ATUALIZACOES -->|depende| CMP_PERSISTENCIA
  CMP_ATUALIZACOES -->|depende| CMP_PROXY
  CMP_ATUALIZACOES -.->|testa| TEST_workspace_target_tests_test_updates_ui_py
  CMP_ATUALIZACOES -.->|testa| TEST_workspace_target_tests_test_updates_v14_py
  CMP_BARREIRA_ACOES["CMP-BARREIRA-ACOES<br/>actions.py"]
  CMP_BARREIRA_ACOES -->|realiza| CAP_AGIR
  CMP_BARREIRA_ACOES -.->|testa| TEST_workspace_target_tests_test_no_backup_py
  CMP_BARREIRA_ACOES -.->|testa| TEST_workspace_target_tests_test_prune_v12_py
  CMP_BARREIRA_ACOES -.->|testa| TEST_workspace_target_tests_test_summary_py
  CMP_CERTS["CMP-CERTS<br/>certs.py"]
  CMP_CERTS -->|realiza| CAP_DIAGNOSTICAR
  CMP_CERTS -->|depende| CMP_POLITICA_RESPOSTA
  CMP_CERTS -.->|testa| TEST_workspace_target_tests_test_certs_sprint5_py
  CMP_CLI["CMP-CLI<br/>cli.py"]
  CMP_CLI -->|realiza| CAP_PROCEDENCIA
  CMP_CLI -->|depende| CMP_CONTRATO
  CMP_CLI -->|depende| CMP_PLANO
  CMP_CLI -->|depende| CMP_PROCEDENCIA
  CMP_CLI -.->|implementa| REQ_003
  CMP_CLI -.->|testa| TEST_tests_e2e_test_cli_laudo_py
  CMP_CONTAINERS["CMP-CONTAINERS<br/>containers.py"]
  CMP_CONTAINERS -->|realiza| CAP_OBSERVAR
  CMP_CONTAINERS -->|depende| CMP_BARREIRA_ACOES
  CMP_CONTAINERS -->|depende| CMP_MASCARAMENTO
  CMP_CONTAINERS -->|depende| CMP_PERSISTENCIA
  CMP_CONTAINERS -->|depende| CMP_POLITICA_RESPOSTA
  CMP_CONTAINERS -->|depende| CMP_PROXY
  CMP_CONTAINERS -->|depende| CMP_RESUMO
  CMP_CONTAINERS -->|depende| CMP_SERIES
  CMP_CONTAINERS -->|depende| CMP_SESSAO
  CMP_CONTAINERS -.->|testa| TEST_workspace_target_tests_test_api_py
  CMP_CONTAINERS -.->|testa| TEST_workspace_target_tests_test_container_history_py
  CMP_CONTAINERS -.->|testa| TEST_workspace_target_tests_test_history_route_py
  CMP_CONTAINERS -.->|testa| TEST_workspace_target_tests_test_logs_texto_py
  CMP_CONTAINERS -.->|testa| TEST_workspace_target_tests_test_telas_renderizam_py
  CMP_CONTRATO["CMP-CONTRATO<br/>contrato.py"]
  CMP_CONTRATO -->|realiza| CAP_CONTRATO
  CMP_CONTRATO -.->|implementa| REQ_001
  CMP_CONTRATO -.->|testa| TEST_tests_integration_test_repositorio_py
  CMP_CONTRATO -.->|testa| TEST_tests_unit_test_contrato_py
  CMP_DRIFT["CMP-DRIFT<br/>drift.py"]
  CMP_DRIFT -->|realiza| CAP_DIAGNOSTICAR
  CMP_DRIFT -->|depende| CMP_MASCARAMENTO
  CMP_DRIFT -->|depende| CMP_POLITICA_RESPOSTA
  CMP_DRIFT -->|depende| CMP_SERIES
  CMP_DRIFT -.->|testa| TEST_workspace_target_tests_test_drift_b8_py
  CMP_DRIFT -.->|testa| TEST_workspace_target_tests_test_guarda_docs_registro_py
  CMP_DRIFT -.->|testa| TEST_workspace_target_tests_test_kernel_cockpit_py
  CMP_DRIFT -.->|testa| TEST_workspace_target_tests_test_render_vivo_py
  CMP_EVENTOS["CMP-EVENTOS<br/>events.py"]
  CMP_EVENTOS -->|realiza| CAP_NARRAR
  CMP_EVENTOS -->|depende| CMP_NOTIFICACOES
  CMP_EVENTOS -->|depende| CMP_PERSISTENCIA
  CMP_EVENTOS -->|depende| CMP_POLITICA_RESPOSTA
  CMP_EVENTOS -->|depende| CMP_PROXY
  CMP_EVENTOS -.->|testa| TEST_workspace_target_tests_test_cabecalhos_seguranca_py
  CMP_EVENTOS -.->|testa| TEST_workspace_target_tests_test_events_rota_py
  CMP_EVENTOS -.->|testa| TEST_workspace_target_tests_test_events_v11_py
  CMP_FASE_C["CMP-FASE-C<br/>escopo_regua.py"]
  CMP_FASE_C -->|realiza| CAP_ALVO
  CMP_FASE_C -->|depende| CMP_CONTRATO
  CMP_FASE_C -.->|testa| TEST_tests_integration_test_fase_c_py
  CMP_FASE_C -.->|testa| TEST_tests_unit_test_escopo_regua_py
  CMP_FASE_C -.->|testa| TEST_tests_unit_test_veredito_py
  CMP_INGRESS["CMP-INGRESS<br/>parser.py"]
  CMP_INGRESS -->|realiza| CAP_DIAGNOSTICAR
  CMP_INGRESS -.->|testa| TEST_workspace_target_tests_test_config_ingress_path_py
  CMP_INGRESS -.->|testa| TEST_workspace_target_tests_test_ingress_parser_py
  CMP_INGRESS -.->|testa| TEST_workspace_target_tests_test_rotas_rail_py
  CMP_INVENTARIO_HOST["CMP-INVENTARIO-HOST<br/>system.py"]
  CMP_INVENTARIO_HOST -->|realiza| CAP_OBSERVAR
  CMP_INVENTARIO_HOST -->|depende| CMP_BARREIRA_ACOES
  CMP_INVENTARIO_HOST -->|depende| CMP_PERSISTENCIA
  CMP_INVENTARIO_HOST -->|depende| CMP_POLITICA_RESPOSTA
  CMP_INVENTARIO_HOST -->|depende| CMP_PROXY
  CMP_INVENTARIO_HOST -->|depende| CMP_SERIES
  CMP_INVENTARIO_HOST -->|depende| CMP_SESSAO
  CMP_INVENTARIO_HOST -.->|testa| TEST_workspace_target_tests_test_projects_security_py
  CMP_INVENTARIO_HOST -.->|testa| TEST_workspace_target_tests_test_session_py
  CMP_LOGS_BUSCA["CMP-LOGS-BUSCA<br/>logs_ingest.py"]
  CMP_LOGS_BUSCA -->|realiza| CAP_NARRAR
  CMP_LOGS_BUSCA -->|depende| CMP_PERSISTENCIA
  CMP_LOGS_BUSCA -->|depende| CMP_PROXY
  CMP_LOGS_BUSCA -.->|testa| TEST_workspace_target_tests_test_logs_fts_v13_py
  CMP_LOGS_BUSCA -.->|testa| TEST_workspace_target_tests_test_notify_v15_py
  CMP_MASCARAMENTO["CMP-MASCARAMENTO<br/>masking.py"]
  CMP_MASCARAMENTO -->|realiza| CAP_SUSTENTAR
  CMP_MASCARAMENTO -.->|testa| TEST_workspace_target_tests_test_api_py
  CMP_NOTIFICACOES["CMP-NOTIFICACOES<br/>notify.py"]
  CMP_NOTIFICACOES -->|realiza| CAP_NARRAR
  CMP_NOTIFICACOES -->|depende| CMP_CERTS
  CMP_NOTIFICACOES -->|depende| CMP_PERSISTENCIA
  CMP_NOTIFICACOES -->|depende| CMP_POLITICA_RESPOSTA
  CMP_NOTIFICACOES -->|depende| CMP_SERIES
  CMP_NOTIFICACOES -.->|testa| TEST_workspace_target_tests_test_notify_v15_py
  CMP_OPERACOES["CMP-OPERACOES<br/>prune.py"]
  CMP_OPERACOES -->|realiza| CAP_AGIR
  CMP_OPERACOES -->|depende| CMP_BARREIRA_ACOES
  CMP_OPERACOES -->|depende| CMP_PERSISTENCIA
  CMP_OPERACOES -->|depende| CMP_POLITICA_RESPOSTA
  CMP_OPERACOES -->|depende| CMP_PROXY
  CMP_OPERACOES -->|depende| CMP_RESUMO
  CMP_OPERACOES -->|depende| CMP_SESSAO
  CMP_OPERACOES -.->|testa| TEST_workspace_target_tests_test_ack_audit_py
  CMP_OPERACOES -.->|testa| TEST_workspace_target_tests_test_ciclo_acao_sintetico_py
  CMP_OPERACOES -.->|testa| TEST_workspace_target_tests_test_prune_sintetico_py
  CMP_OPERACOES -.->|testa| TEST_workspace_target_tests_test_prune_v12_py
  CMP_OPERACOES -.->|testa| TEST_workspace_target_tests_test_tasks_py
  CMP_OPERACOES -.->|testa| TEST_workspace_target_tests_test_tasks_api_py
  CMP_PERSISTENCIA["CMP-PERSISTENCIA<br/>db.py"]
  CMP_PERSISTENCIA -->|realiza| CAP_SUSTENTAR
  CMP_PERSISTENCIA -.->|testa| TEST_workspace_target_tests_test_container_history_py
  CMP_PERSISTENCIA -.->|testa| TEST_workspace_target_tests_test_db_py
  CMP_PERSISTENCIA -.->|testa| TEST_workspace_target_tests_test_events_v11_py
  CMP_PERSISTENCIA -.->|testa| TEST_workspace_target_tests_test_migration_py
  CMP_PERSISTENCIA -.->|testa| TEST_workspace_target_tests_test_no_backup_py
  CMP_PLANO["CMP-PLANO<br/>plano.py"]
  CMP_PLANO -->|realiza| CAP_MODOS
  CMP_PLANO -->|depende| CMP_CONTRATO
  CMP_PLANO -.->|implementa| REQ_002
  CMP_PLANO -.->|implementa| REQ_004
  CMP_PLANO -.->|testa| TEST_tests_integration_test_workflows_py
  CMP_PLANO -.->|testa| TEST_tests_unit_test_plano_py
  CMP_POLITICA_RESPOSTA["CMP-POLITICA-RESPOSTA<br/>cache.py"]
  CMP_POLITICA_RESPOSTA -->|realiza| CAP_SUSTENTAR
  CMP_POLITICA_RESPOSTA -.->|testa| TEST_workspace_target_tests_test_acessibilidade_py
  CMP_POLITICA_RESPOSTA -.->|testa| TEST_workspace_target_tests_test_cabecalhos_seguranca_py
  CMP_POLITICA_RESPOSTA -.->|testa| TEST_workspace_target_tests_test_cache_py
  CMP_POLITICA_RESPOSTA -.->|testa| TEST_workspace_target_tests_test_cache_http_py
  CMP_POLITICA_RESPOSTA -.->|testa| TEST_workspace_target_tests_test_capacidade_cards_py
  CMP_POLITICA_RESPOSTA -.->|testa| TEST_workspace_target_tests_test_sinais_de_maturidade_py
  CMP_PROCEDENCIA["CMP-PROCEDENCIA<br/>procedencia.py"]
  CMP_PROCEDENCIA -->|realiza| CAP_PROCEDENCIA
  CMP_PROCEDENCIA -->|depende| CMP_CONTRATO
  CMP_PROCEDENCIA -.->|implementa| REQ_003
  CMP_PROCEDENCIA -.->|testa| TEST_tests_unit_test_procedencia_py
  CMP_PROXY["CMP-PROXY<br/>_proxy.py"]
  CMP_PROXY -->|realiza| CAP_OBSERVAR
  CMP_PROXY -.->|testa| TEST_workspace_target_tests_test_projects_security_py
  CMP_PROXY -.->|testa| TEST_workspace_target_tests_test_updates_v14_py
  CMP_REGRAS_ACHADO["CMP-REGRAS-ACHADO<br/>__init__.py"]
  CMP_REGRAS_ACHADO -->|realiza| CAP_DIAGNOSTICAR
  CMP_REGRAS_ACHADO -.->|testa| TEST_workspace_target_tests_test_findings_py
  CMP_REGRAS_ACHADO -.->|testa| TEST_workspace_target_tests_test_no_backup_py
  CMP_REGRAS_ACHADO -.->|testa| TEST_workspace_target_tests_test_regras_container_parado_py
  CMP_RESUMO["CMP-RESUMO<br/>summary.py"]
  CMP_RESUMO -->|realiza| CAP_NARRAR
  CMP_RESUMO -->|depende| CMP_ACHADOS
  CMP_RESUMO -->|depende| CMP_BARREIRA_ACOES
  CMP_RESUMO -->|depende| CMP_CERTS
  CMP_RESUMO -->|depende| CMP_DRIFT
  CMP_RESUMO -->|depende| CMP_INGRESS
  CMP_RESUMO -->|depende| CMP_PERSISTENCIA
  CMP_RESUMO -->|depende| CMP_POLITICA_RESPOSTA
  CMP_RESUMO -->|depende| CMP_PROXY
  CMP_RESUMO -->|depende| CMP_SERIES
  CMP_RESUMO -.->|testa| TEST_workspace_target_tests_test_executive_py
  CMP_RESUMO -.->|testa| TEST_workspace_target_tests_test_kernel_cockpit_py
  CMP_RESUMO -.->|testa| TEST_workspace_target_tests_test_offline_py
  CMP_RESUMO -.->|testa| TEST_workspace_target_tests_test_storage_py
  CMP_RESUMO -.->|testa| TEST_workspace_target_tests_test_summary_py
  CMP_SERIES["CMP-SERIES<br/>sampler.py"]
  CMP_SERIES -->|realiza| CAP_NARRAR
  CMP_SERIES -->|depende| CMP_CONTAINERS
  CMP_SERIES -->|depende| CMP_PERSISTENCIA
  CMP_SERIES -->|depende| CMP_PROXY
  CMP_SERIES -->|depende| CMP_SESSAO
  CMP_SERIES -.->|testa| TEST_workspace_target_tests_test_capacidade_serie_curta_py
  CMP_SERIES -.->|testa| TEST_workspace_target_tests_test_frescor_amostra_py
  CMP_SERIES -.->|testa| TEST_workspace_target_tests_test_metrics_py
  CMP_SERIES -.->|testa| TEST_workspace_target_tests_test_metrics_prom_py
  CMP_SERIES -.->|testa| TEST_workspace_target_tests_test_sampler_py
  CMP_SESSAO["CMP-SESSAO<br/>auth.py"]
  CMP_SESSAO -->|realiza| CAP_AGIR
  CMP_SESSAO -->|depende| CMP_NOTIFICACOES
  CMP_SESSAO -->|depende| CMP_PERSISTENCIA
  CMP_SESSAO -.->|testa| TEST_workspace_target_tests_test_deploy_credencial_py
  CMP_SESSAO -.->|testa| TEST_workspace_target_tests_test_hardening_b11_py
  CMP_SESSAO -.->|testa| TEST_workspace_target_tests_test_session_py
  CMP_SESSAO -.->|testa| TEST_workspace_target_tests_test_unlock_v8_py
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
  RULE_HOMOLOG_001["RULE-HOMOLOG-001"]
  CAP_ALVO -->|regra| RULE_HOMOLOG_001
  RULE_HOMOLOG_001 -.->|verifica| TEST_tests_integration_test_homologacao_py
  RULE_HOMOLOG_002["RULE-HOMOLOG-002"]
  CAP_ALVO -->|regra| RULE_HOMOLOG_002
  RULE_HOMOLOG_002 -.->|verifica| TEST_tests_integration_test_homologacao_py
  RULE_HOMOLOG_003["RULE-HOMOLOG-003"]
  CAP_ALVO -->|regra| RULE_HOMOLOG_003
  RULE_HOMOLOG_003 -.->|verifica| TEST_tests_integration_test_homologacao_py
  RULE_HOMOLOG_004["RULE-HOMOLOG-004"]
  CAP_ALVO -->|regra| RULE_HOMOLOG_004
  RULE_HOMOLOG_004 -.->|verifica| TEST_tests_integration_test_homologacao_py
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
  REQ_005 -.->|depende| REQ_009
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
  REQ_009["REQ-009<br/>proposed"]
  REQ_009 -->|requisito| CAP_ALVO
  REQ_009 ==>|move| MET_PENDENCIA
  REQ_009 -.->|regido por| RULE_HOMOLOG_001
  REQ_009 -.->|regido por| RULE_HOMOLOG_002
  REQ_009 -.->|regido por| RULE_HOMOLOG_003
  REQ_009 -.->|regido por| RULE_HOMOLOG_004
  RISK_ALVO_001["RISK-ALVO-001"]
  RISK_CHANGE_001["RISK-CHANGE-001"]
  RISK_DEP_001["RISK-DEP-001"]
  RISK_HOMOLOG_001["RISK-HOMOLOG-001"]
  RISK_META_001["RISK-META-001"]
  RISK_MOLDE_001["RISK-MOLDE-001"]
  RISK_SEGREDO_001["RISK-SEGREDO-001"]
  RISK_SOCKET_001["RISK-SOCKET-001"]
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
  ADR_015["ADR-015"]
  ADR_015 -->|decide| CAP_ALVO
  ADR_015 -->|mitiga| RISK_ALVO_001
  ADR_016["ADR-016"]
  ADR_016 -->|decide| CAP_ALVO
  ADR_016 -->|decide| CAP_CONTRATO
  ADR_016 -->|decide| CMP_CONTRATO
  ADR_016 -->|mitiga| RISK_ALVO_001
  ADR_016 -->|mitiga| RISK_SEGREDO_001
  ADR_017["ADR-017"]
  ADR_017 -->|decide| CAP_ALVO
  ADR_017 -->|mitiga| RISK_ALVO_001
  ADR_017 -->|mitiga| RISK_HOMOLOG_001
  classDef project fill:#1f2937,stroke:#111827,color:#fff;
  class PROJ_danzeroum_projectcockpitdocker project;
  classDef cap fill:#2563eb,stroke:#1e40af,color:#fff;
  class CAP_AGIR,CAP_ALVO,CAP_CONTRATO,CAP_DIAGNOSTICAR,CAP_MODOS,CAP_NARRAR,CAP_OBSERVAR,CAP_PROCEDENCIA,CAP_SUSTENTAR cap;
  classDef cmp fill:#0891b2,stroke:#0e7490,color:#fff;
  class CMP_ACHADOS,CMP_APP,CMP_ATUALIZACOES,CMP_BARREIRA_ACOES,CMP_CERTS,CMP_CLI,CMP_CONTAINERS,CMP_CONTRATO,CMP_DRIFT,CMP_EVENTOS,CMP_FASE_C,CMP_INGRESS,CMP_INVENTARIO_HOST,CMP_LOGS_BUSCA,CMP_MASCARAMENTO,CMP_NOTIFICACOES,CMP_OPERACOES,CMP_PERSISTENCIA,CMP_PLANO,CMP_POLITICA_RESPOSTA,CMP_PROCEDENCIA,CMP_PROXY,CMP_REGRAS_ACHADO,CMP_RESUMO,CMP_SERIES,CMP_SESSAO cmp;
  classDef ifc fill:#7c3aed,stroke:#5b21b6,color:#fff;
  class IFC_CLI,IFC_CONTRATO,IFC_PLANO,IFC_PROCEDENCIA ifc;
  classDef rule fill:#16a34a,stroke:#15803d,color:#fff;
  class RULE_CONTRATO_001,RULE_CONTRATO_002,RULE_CONTRATO_003,RULE_CONTRATO_004,RULE_CONTRATO_005,RULE_HOMOLOG_001,RULE_HOMOLOG_002,RULE_HOMOLOG_003,RULE_HOMOLOG_004,RULE_MODOS_001,RULE_MODOS_002,RULE_MODOS_003,RULE_MODOS_004,RULE_PROCEDENCIA_001,RULE_PROCEDENCIA_002,RULE_PROCEDENCIA_003,RULE_PROCEDENCIA_004 rule;
  classDef ui fill:#db2777,stroke:#9d174d,color:#fff;
  class UI_COCKPIT_EXECUTIVO,UI_COCKPIT_PAINEL ui;
  classDef req fill:#0d9488,stroke:#0f766e,color:#fff;
  class REQ_001,REQ_002,REQ_003,REQ_004,REQ_005,REQ_006,REQ_007,REQ_008,REQ_009 req;
  classDef met fill:#ea580c,stroke:#c2410c,color:#fff;
  class MET_COMPARAVEL,MET_FRONTEIRA,MET_PENDENCIA met;
  classDef test fill:#57534e,stroke:#44403c,color:#fff;
  class TEST_tests_e2e_test_checklist_adocao_py,TEST_tests_e2e_test_cli_laudo_py,TEST_tests_integration_test_fase_c_py,TEST_tests_integration_test_homologacao_py,TEST_tests_integration_test_repositorio_py,TEST_tests_integration_test_workflows_py,TEST_tests_unit_test_contrato_py,TEST_tests_unit_test_escopo_regua_py,TEST_tests_unit_test_plano_py,TEST_tests_unit_test_procedencia_py,TEST_tests_unit_test_veredito_py,TEST_workspace_target_tests_test_acessibilidade_py,TEST_workspace_target_tests_test_ack_audit_py,TEST_workspace_target_tests_test_api_py,TEST_workspace_target_tests_test_cabecalhos_seguranca_py,TEST_workspace_target_tests_test_cache_py,TEST_workspace_target_tests_test_cache_http_py,TEST_workspace_target_tests_test_capacidade_cards_py,TEST_workspace_target_tests_test_capacidade_serie_curta_py,TEST_workspace_target_tests_test_certs_sprint5_py,TEST_workspace_target_tests_test_ciclo_acao_sintetico_py,TEST_workspace_target_tests_test_config_ingress_path_py,TEST_workspace_target_tests_test_container_history_py,TEST_workspace_target_tests_test_db_py,TEST_workspace_target_tests_test_deploy_credencial_py,TEST_workspace_target_tests_test_drift_b8_py,TEST_workspace_target_tests_test_events_rota_py,TEST_workspace_target_tests_test_events_v11_py,TEST_workspace_target_tests_test_executive_py,TEST_workspace_target_tests_test_f6_palette_py,TEST_workspace_target_tests_test_findings_py,TEST_workspace_target_tests_test_frescor_amostra_py,TEST_workspace_target_tests_test_guarda_docs_registro_py,TEST_workspace_target_tests_test_guarda_schema_literal_py,TEST_workspace_target_tests_test_hardening_b11_py,TEST_workspace_target_tests_test_history_route_py,TEST_workspace_target_tests_test_ingress_parser_py,TEST_workspace_target_tests_test_kernel_cockpit_py,TEST_workspace_target_tests_test_logs_fts_v13_py,TEST_workspace_target_tests_test_logs_texto_py,TEST_workspace_target_tests_test_metrics_py,TEST_workspace_target_tests_test_metrics_prom_py,TEST_workspace_target_tests_test_migration_py,TEST_workspace_target_tests_test_no_backup_py,TEST_workspace_target_tests_test_notify_v15_py,TEST_workspace_target_tests_test_offline_py,TEST_workspace_target_tests_test_projects_security_py,TEST_workspace_target_tests_test_prune_sintetico_py,TEST_workspace_target_tests_test_prune_v12_py,TEST_workspace_target_tests_test_regras_container_parado_py,TEST_workspace_target_tests_test_render_vivo_py,TEST_workspace_target_tests_test_rotas_rail_py,TEST_workspace_target_tests_test_sampler_py,TEST_workspace_target_tests_test_session_py,TEST_workspace_target_tests_test_sinais_de_maturidade_py,TEST_workspace_target_tests_test_storage_py,TEST_workspace_target_tests_test_summary_py,TEST_workspace_target_tests_test_tasks_py,TEST_workspace_target_tests_test_tasks_api_py,TEST_workspace_target_tests_test_telas_renderizam_py,TEST_workspace_target_tests_test_telas_topologia_plantao_py,TEST_workspace_target_tests_test_unlock_v8_py,TEST_workspace_target_tests_test_updates_ui_py,TEST_workspace_target_tests_test_updates_v14_py test;
  classDef adr fill:#ca8a04,stroke:#a16207,color:#fff;
  class ADR_001,ADR_002,ADR_003,ADR_004,ADR_015,ADR_016,ADR_017 adr;
  classDef risk fill:#dc2626,stroke:#991b1b,color:#fff;
  class RISK_ALVO_001,RISK_CHANGE_001,RISK_DEP_001,RISK_HOMOLOG_001,RISK_META_001,RISK_MOLDE_001,RISK_SEGREDO_001,RISK_SOCKET_001,RISK_WEBQA_001 risk;
```

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
  TEST_workspace_target_tests_fixtures_exercita_kernel_mjs{{"exercita_kernel.mjs"}}
  TEST_workspace_target_tests_fixtures_exercita_notificacoes_mjs{{"exercita_notificacoes.mjs"}}
  TEST_workspace_target_tests_fixtures_exercita_render_vivo_mjs{{"exercita_render_vivo.mjs"}}
  TEST_workspace_target_tests_fixtures_exercita_rotas_mjs{{"exercita_rotas.mjs"}}
  TEST_workspace_target_tests_fixtures_exercita_telas_mjs{{"exercita_telas.mjs"}}
  TEST_workspace_target_tests_fixtures_exercita_updates_mjs{{"exercita_updates.mjs"}}
  TEST_workspace_target_tests_fixtures_renderiza_capacidade_mjs{{"renderiza_capacidade.mjs"}}
  TEST_workspace_target_tests_fixtures_renderiza_telas_mjs{{"renderiza_telas.mjs"}}
  TEST_workspace_target_tests_test_acessibilidade_py{{"test_acessibilidade.py"}}
  TEST_workspace_target_tests_test_ack_audit_py{{"test_ack_audit.py"}}
  TEST_workspace_target_tests_test_api_py{{"test_api.py"}}
  TEST_workspace_target_tests_test_backend_py{{"test_backend.py"}}
  TEST_workspace_target_tests_test_cabecalhos_seguranca_py{{"test_cabecalhos_seguranca.py"}}
  TEST_workspace_target_tests_test_cache_py{{"test_cache.py"}}
  TEST_workspace_target_tests_test_cache_http_py{{"test_cache_http.py"}}
  TEST_workspace_target_tests_test_capacidade_cards_py{{"test_capacidade_cards.py"}}
  TEST_workspace_target_tests_test_capacidade_serie_curta_py{{"test_capacidade_serie_curta.py"}}
  TEST_workspace_target_tests_test_certs_sprint5_py{{"test_certs_sprint5.py"}}
  TEST_workspace_target_tests_test_ciclo_acao_sintetico_py{{"test_ciclo_acao_sintetico.py"}}
  TEST_workspace_target_tests_test_config_ingress_path_py{{"test_config_ingress_path.py"}}
  TEST_workspace_target_tests_test_container_history_py{{"test_container_history.py"}}
  TEST_workspace_target_tests_test_contraste_severidade_py{{"test_contraste_severidade.py"}}
  TEST_workspace_target_tests_test_db_py{{"test_db.py"}}
  TEST_workspace_target_tests_test_deploy_credencial_py{{"test_deploy_credencial.py"}}
  TEST_workspace_target_tests_test_drift_b8_py{{"test_drift_b8.py"}}
  TEST_workspace_target_tests_test_events_rota_py{{"test_events_rota.py"}}
  TEST_workspace_target_tests_test_events_v11_py{{"test_events_v11.py"}}
  TEST_workspace_target_tests_test_executive_py{{"test_executive.py"}}
  TEST_workspace_target_tests_test_f6_palette_py{{"test_f6_palette.py"}}
  TEST_workspace_target_tests_test_findings_py{{"test_findings.py"}}
  TEST_workspace_target_tests_test_frescor_amostra_py{{"test_frescor_amostra.py"}}
  TEST_workspace_target_tests_test_frontend_modulos_py{{"test_frontend_modulos.py"}}
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
  TEST_workspace_target_tests_test_notificacoes_ui_py{{"test_notificacoes_ui.py"}}
  TEST_workspace_target_tests_test_notify_v15_py{{"test_notify_v15.py"}}
  TEST_workspace_target_tests_test_offline_py{{"test_offline.py"}}
  TEST_workspace_target_tests_test_projects_security_py{{"test_projects_security.py"}}
  TEST_workspace_target_tests_test_prune_sintetico_py{{"test_prune_sintetico.py"}}
  TEST_workspace_target_tests_test_prune_v12_py{{"test_prune_v12.py"}}
  TEST_workspace_target_tests_test_regras_container_parado_py{{"test_regras_container_parado.py"}}
  TEST_workspace_target_tests_test_render_vivo_py{{"test_render_vivo.py"}}
  TEST_workspace_target_tests_test_rotas_rail_py{{"test_rotas_rail.py"}}
  TEST_workspace_target_tests_test_sampler_py{{"test_sampler.py"}}
  TEST_workspace_target_tests_test_security_py{{"test_security.py"}}
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
  CAP_DIAGNOSTICAR["CAP-DIAGNOSTICAR<br/>Transformar o estado observado em achados acionáveis"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_DIAGNOSTICAR
  CAP_NARRAR["CAP-NARRAR<br/>Entregar o estado ao operador: fluxo, séries e notificação"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_NARRAR
  CAP_OBSERVAR["CAP-OBSERVAR<br/>Observar o estado do daemon Docker de um host"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_OBSERVAR
  CAP_SUSTENTAR["CAP-SUSTENTAR<br/>Servir a aplicação com política declarada de resposta e dados"]
  PROJ_danzeroum_projectcockpitdocker -->|capacidade| CAP_SUSTENTAR
  CMP_ACHADOS["CMP-ACHADOS<br/>__init__.py"]
  CMP_ACHADOS -->|realiza| CAP_DIAGNOSTICAR
  CMP_ACHADOS -->|depende| CMP_PERSISTENCIA
  CMP_ACHADOS -->|depende| CMP_PROXY
  CMP_ACHADOS -->|depende| CMP_SERIES
  CMP_ACHADOS -->|depende| CMP_SESSAO
  CMP_ACHADOS -.->|implementa| REQ_004
  CMP_ACHADOS -.->|implementa| REQ_014
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
  CMP_ATUALIZACOES -.->|implementa| REQ_008
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
  CMP_CERTS -.->|implementa| REQ_006
  CMP_CERTS -.->|testa| TEST_workspace_target_tests_test_certs_sprint5_py
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
  CMP_CONTAINERS -.->|implementa| REQ_001
  CMP_CONTAINERS -.->|implementa| REQ_002
  CMP_CONTAINERS -.->|testa| TEST_workspace_target_tests_test_api_py
  CMP_CONTAINERS -.->|testa| TEST_workspace_target_tests_test_container_history_py
  CMP_CONTAINERS -.->|testa| TEST_workspace_target_tests_test_history_route_py
  CMP_CONTAINERS -.->|testa| TEST_workspace_target_tests_test_logs_texto_py
  CMP_CONTAINERS -.->|testa| TEST_workspace_target_tests_test_telas_renderizam_py
  CMP_DRIFT["CMP-DRIFT<br/>drift.py"]
  CMP_DRIFT -->|realiza| CAP_DIAGNOSTICAR
  CMP_DRIFT -->|depende| CMP_MASCARAMENTO
  CMP_DRIFT -->|depende| CMP_POLITICA_RESPOSTA
  CMP_DRIFT -->|depende| CMP_SERIES
  CMP_DRIFT -.->|implementa| REQ_007
  CMP_DRIFT -.->|testa| TEST_workspace_target_tests_test_drift_b8_py
  CMP_DRIFT -.->|testa| TEST_workspace_target_tests_test_guarda_docs_registro_py
  CMP_DRIFT -.->|testa| TEST_workspace_target_tests_test_kernel_cockpit_py
  CMP_DRIFT -.->|testa| TEST_workspace_target_tests_test_render_vivo_py
  CMP_EMPACOTAMENTO["CMP-EMPACOTAMENTO<br/>Dockerfile"]
  CMP_EMPACOTAMENTO -->|realiza| CAP_SUSTENTAR
  CMP_EMPACOTAMENTO -.->|testa| TEST_workspace_target_tests_test_config_ingress_path_py
  CMP_EMPACOTAMENTO -.->|testa| TEST_workspace_target_tests_test_deploy_credencial_py
  CMP_EVENTOS["CMP-EVENTOS<br/>events.py"]
  CMP_EVENTOS -->|realiza| CAP_NARRAR
  CMP_EVENTOS -->|depende| CMP_NOTIFICACOES
  CMP_EVENTOS -->|depende| CMP_PERSISTENCIA
  CMP_EVENTOS -->|depende| CMP_POLITICA_RESPOSTA
  CMP_EVENTOS -->|depende| CMP_PROXY
  CMP_EVENTOS -.->|implementa| REQ_015
  CMP_EVENTOS -.->|testa| TEST_workspace_target_tests_test_cabecalhos_seguranca_py
  CMP_EVENTOS -.->|testa| TEST_workspace_target_tests_test_events_rota_py
  CMP_EVENTOS -.->|testa| TEST_workspace_target_tests_test_events_v11_py
  CMP_INGRESS["CMP-INGRESS<br/>parser.py"]
  CMP_INGRESS -->|realiza| CAP_DIAGNOSTICAR
  CMP_INGRESS -.->|implementa| REQ_009
  CMP_INGRESS -.->|testa| TEST_workspace_target_tests_fixtures_exercita_rotas_mjs
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
  CMP_INVENTARIO_HOST -.->|implementa| REQ_003
  CMP_INVENTARIO_HOST -.->|testa| TEST_workspace_target_tests_test_projects_security_py
  CMP_INVENTARIO_HOST -.->|testa| TEST_workspace_target_tests_test_session_py
  CMP_LOGS_BUSCA["CMP-LOGS-BUSCA<br/>logs_ingest.py"]
  CMP_LOGS_BUSCA -->|realiza| CAP_NARRAR
  CMP_LOGS_BUSCA -->|depende| CMP_PERSISTENCIA
  CMP_LOGS_BUSCA -->|depende| CMP_PROXY
  CMP_LOGS_BUSCA -.->|implementa| REQ_027
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
  CMP_NOTIFICACOES -.->|implementa| REQ_018
  CMP_NOTIFICACOES -.->|testa| TEST_workspace_target_tests_test_notify_v15_py
  CMP_OPERACOES["CMP-OPERACOES<br/>prune.py"]
  CMP_OPERACOES -->|realiza| CAP_AGIR
  CMP_OPERACOES -->|depende| CMP_BARREIRA_ACOES
  CMP_OPERACOES -->|depende| CMP_PERSISTENCIA
  CMP_OPERACOES -->|depende| CMP_POLITICA_RESPOSTA
  CMP_OPERACOES -->|depende| CMP_PROXY
  CMP_OPERACOES -->|depende| CMP_RESUMO
  CMP_OPERACOES -->|depende| CMP_SESSAO
  CMP_OPERACOES -.->|implementa| REQ_010
  CMP_OPERACOES -.->|implementa| REQ_011
  CMP_OPERACOES -.->|implementa| REQ_013
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
  CMP_POLITICA_RESPOSTA["CMP-POLITICA-RESPOSTA<br/>cache.py"]
  CMP_POLITICA_RESPOSTA -->|realiza| CAP_SUSTENTAR
  CMP_POLITICA_RESPOSTA -.->|testa| TEST_workspace_target_tests_test_acessibilidade_py
  CMP_POLITICA_RESPOSTA -.->|testa| TEST_workspace_target_tests_test_cabecalhos_seguranca_py
  CMP_POLITICA_RESPOSTA -.->|testa| TEST_workspace_target_tests_test_cache_py
  CMP_POLITICA_RESPOSTA -.->|testa| TEST_workspace_target_tests_test_cache_http_py
  CMP_POLITICA_RESPOSTA -.->|testa| TEST_workspace_target_tests_test_capacidade_cards_py
  CMP_POLITICA_RESPOSTA -.->|testa| TEST_workspace_target_tests_test_sinais_de_maturidade_py
  CMP_PROXY["CMP-PROXY<br/>_proxy.py"]
  CMP_PROXY -->|realiza| CAP_OBSERVAR
  CMP_PROXY -.->|testa| TEST_workspace_target_tests_test_projects_security_py
  CMP_PROXY -.->|testa| TEST_workspace_target_tests_test_updates_v14_py
  CMP_REGRAS_ACHADO["CMP-REGRAS-ACHADO<br/>__init__.py"]
  CMP_REGRAS_ACHADO -->|realiza| CAP_DIAGNOSTICAR
  CMP_REGRAS_ACHADO -.->|implementa| REQ_005
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
  CMP_RESUMO -.->|implementa| REQ_017
  CMP_RESUMO -.->|testa| TEST_workspace_target_tests_test_backend_py
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
  CMP_SERIES -.->|implementa| REQ_016
  CMP_SERIES -.->|implementa| REQ_025
  CMP_SERIES -.->|testa| TEST_workspace_target_tests_test_capacidade_serie_curta_py
  CMP_SERIES -.->|testa| TEST_workspace_target_tests_test_frescor_amostra_py
  CMP_SERIES -.->|testa| TEST_workspace_target_tests_test_metrics_py
  CMP_SERIES -.->|testa| TEST_workspace_target_tests_test_metrics_prom_py
  CMP_SERIES -.->|testa| TEST_workspace_target_tests_test_sampler_py
  CMP_SESSAO["CMP-SESSAO<br/>auth.py"]
  CMP_SESSAO -->|realiza| CAP_AGIR
  CMP_SESSAO -->|depende| CMP_NOTIFICACOES
  CMP_SESSAO -->|depende| CMP_PERSISTENCIA
  CMP_SESSAO -.->|implementa| REQ_012
  CMP_SESSAO -.->|testa| TEST_workspace_target_tests_test_deploy_credencial_py
  CMP_SESSAO -.->|testa| TEST_workspace_target_tests_test_hardening_b11_py
  CMP_SESSAO -.->|testa| TEST_workspace_target_tests_test_session_py
  CMP_SESSAO -.->|testa| TEST_workspace_target_tests_test_unlock_v8_py
  CMP_TELA_ATENCAO["CMP-TELA-ATENCAO<br/>atencao.js"]
  CMP_TELA_ATENCAO -->|realiza| CAP_NARRAR
  CMP_TELA_ATENCAO -->|depende| CMP_UI_INFRA
  CMP_TELA_ATENCAO -->|depende| CMP_UI_KERNEL
  CMP_TELA_ATENCAO -.->|implementa| REQ_018
  CMP_TELA_ATENCAO -.->|implementa| REQ_020
  CMP_TELA_ATENCAO -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_AUDITORIA["CMP-TELA-AUDITORIA<br/>auditoria.js"]
  CMP_TELA_AUDITORIA -->|realiza| CAP_NARRAR
  CMP_TELA_AUDITORIA -->|depende| CMP_UI_INFRA
  CMP_TELA_AUDITORIA -->|depende| CMP_UI_KERNEL
  CMP_TELA_AUDITORIA -.->|implementa| REQ_020
  CMP_TELA_AUDITORIA -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_BACKEND["CMP-TELA-BACKEND<br/>backend.js"]
  CMP_TELA_BACKEND -->|realiza| CAP_NARRAR
  CMP_TELA_BACKEND -->|depende| CMP_UI_INFRA
  CMP_TELA_BACKEND -->|depende| CMP_UI_KERNEL
  CMP_TELA_BACKEND -.->|implementa| REQ_024
  CMP_TELA_BACKEND -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_CAPACIDADE["CMP-TELA-CAPACIDADE<br/>capacidade.js"]
  CMP_TELA_CAPACIDADE -->|realiza| CAP_NARRAR
  CMP_TELA_CAPACIDADE -->|depende| CMP_UI_INFRA
  CMP_TELA_CAPACIDADE -->|depende| CMP_UI_KERNEL
  CMP_TELA_CAPACIDADE -.->|implementa| REQ_016
  CMP_TELA_CAPACIDADE -.->|testa| TEST_workspace_target_tests_fixtures_renderiza_capacidade_mjs
  CMP_TELA_CAPACIDADE -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_EXECUTIVO["CMP-TELA-EXECUTIVO<br/>executivo.js"]
  CMP_TELA_EXECUTIVO -->|realiza| CAP_NARRAR
  CMP_TELA_EXECUTIVO -->|depende| CMP_UI_INFRA
  CMP_TELA_EXECUTIVO -->|depende| CMP_UI_KERNEL
  CMP_TELA_EXECUTIVO -.->|implementa| REQ_017
  CMP_TELA_EXECUTIVO -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_INGRESS["CMP-TELA-INGRESS<br/>ingress.js"]
  CMP_TELA_INGRESS -->|realiza| CAP_NARRAR
  CMP_TELA_INGRESS -->|depende| CMP_UI_INFRA
  CMP_TELA_INGRESS -->|depende| CMP_UI_KERNEL
  CMP_TELA_INGRESS -.->|implementa| REQ_020
  CMP_TELA_INGRESS -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_PLANTAO["CMP-TELA-PLANTAO<br/>plantao.js"]
  CMP_TELA_PLANTAO -->|realiza| CAP_NARRAR
  CMP_TELA_PLANTAO -->|depende| CMP_UI_INFRA
  CMP_TELA_PLANTAO -->|depende| CMP_UI_KERNEL
  CMP_TELA_PLANTAO -.->|implementa| REQ_022
  CMP_TELA_PLANTAO -.->|testa| TEST_workspace_target_tests_fixtures_exercita_telas_mjs
  CMP_TELA_PLANTAO -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_PROJETOS["CMP-TELA-PROJETOS<br/>projetos.js"]
  CMP_TELA_PROJETOS -->|realiza| CAP_NARRAR
  CMP_TELA_PROJETOS -->|depende| CMP_UI_INFRA
  CMP_TELA_PROJETOS -->|depende| CMP_UI_KERNEL
  CMP_TELA_PROJETOS -.->|implementa| REQ_020
  CMP_TELA_PROJETOS -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_TAREFAS["CMP-TELA-TAREFAS<br/>tarefas.js"]
  CMP_TELA_TAREFAS -->|realiza| CAP_NARRAR
  CMP_TELA_TAREFAS -->|depende| CMP_UI_INFRA
  CMP_TELA_TAREFAS -->|depende| CMP_UI_KERNEL
  CMP_TELA_TAREFAS -.->|implementa| REQ_020
  CMP_TELA_TAREFAS -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_TOPOLOGIA["CMP-TELA-TOPOLOGIA<br/>topologia.js"]
  CMP_TELA_TOPOLOGIA -->|realiza| CAP_NARRAR
  CMP_TELA_TOPOLOGIA -->|depende| CMP_UI_INFRA
  CMP_TELA_TOPOLOGIA -->|depende| CMP_UI_KERNEL
  CMP_TELA_TOPOLOGIA -.->|implementa| REQ_020
  CMP_TELA_TOPOLOGIA -.->|testa| TEST_workspace_target_tests_fixtures_exercita_telas_mjs
  CMP_TELA_TOPOLOGIA -.->|testa| TEST_workspace_target_tests_fixtures_renderiza_telas_mjs
  CMP_TELA_TOPOLOGIA -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_UI_CASCA["CMP-UI-CASCA<br/>index.html"]
  CMP_UI_CASCA -->|realiza| CAP_NARRAR
  CMP_UI_CASCA -.->|implementa| REQ_023
  CMP_UI_CASCA -.->|implementa| REQ_026
  CMP_UI_CASCA -.->|testa| TEST_workspace_target_tests_test_acessibilidade_py
  CMP_UI_CASCA -.->|testa| TEST_workspace_target_tests_test_contraste_severidade_py
  CMP_UI_INFRA["CMP-UI-INFRA<br/>commands.js"]
  CMP_UI_INFRA -->|realiza| CAP_NARRAR
  CMP_UI_INFRA -->|depende| CMP_UI_KERNEL
  CMP_UI_INFRA -.->|implementa| REQ_018
  CMP_UI_INFRA -.->|implementa| REQ_020
  CMP_UI_INFRA -.->|testa| TEST_workspace_target_tests_fixtures_exercita_notificacoes_mjs
  CMP_UI_INFRA -.->|testa| TEST_workspace_target_tests_fixtures_exercita_updates_mjs
  CMP_UI_INFRA -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_UI_INFRA -.->|testa| TEST_workspace_target_tests_test_notificacoes_ui_py
  CMP_UI_KERNEL["CMP-UI-KERNEL<br/>app.js"]
  CMP_UI_KERNEL -->|realiza| CAP_NARRAR
  CMP_UI_KERNEL -->|depende| CMP_UI_INFRA
  CMP_UI_KERNEL -->|depende| CMP_UI_MODULOS_INLINE
  CMP_UI_KERNEL -.->|implementa| REQ_020
  CMP_UI_KERNEL -.->|implementa| REQ_021
  CMP_UI_KERNEL -.->|testa| TEST_workspace_target_tests_fixtures_exercita_kernel_mjs
  CMP_UI_KERNEL -.->|testa| TEST_workspace_target_tests_fixtures_exercita_render_vivo_mjs
  CMP_UI_KERNEL -.->|testa| TEST_workspace_target_tests_test_contraste_severidade_py
  CMP_UI_KERNEL -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_UI_MODULOS_INLINE["CMP-UI-MODULOS-INLINE<br/>armazenamento.js"]
  CMP_UI_MODULOS_INLINE -->|realiza| CAP_NARRAR
  CMP_UI_MODULOS_INLINE -->|depende| CMP_TELA_ATENCAO
  CMP_UI_MODULOS_INLINE -->|depende| CMP_TELA_AUDITORIA
  CMP_UI_MODULOS_INLINE -->|depende| CMP_TELA_BACKEND
  CMP_UI_MODULOS_INLINE -->|depende| CMP_TELA_CAPACIDADE
  CMP_UI_MODULOS_INLINE -->|depende| CMP_TELA_EXECUTIVO
  CMP_UI_MODULOS_INLINE -->|depende| CMP_TELA_INGRESS
  CMP_UI_MODULOS_INLINE -->|depende| CMP_TELA_PLANTAO
  CMP_UI_MODULOS_INLINE -->|depende| CMP_TELA_PROJETOS
  CMP_UI_MODULOS_INLINE -->|depende| CMP_TELA_TAREFAS
  CMP_UI_MODULOS_INLINE -->|depende| CMP_TELA_TOPOLOGIA
  CMP_UI_MODULOS_INLINE -->|depende| CMP_UI_INFRA
  CMP_UI_MODULOS_INLINE -->|depende| CMP_UI_KERNEL
  CMP_UI_MODULOS_INLINE -.->|implementa| REQ_020
  CMP_UI_MODULOS_INLINE -.->|implementa| REQ_021
  CMP_UI_MODULOS_INLINE -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_UI_MODULOS_INLINE -.->|testa| TEST_workspace_target_tests_test_notificacoes_ui_py
  RULE_AGIR_001["RULE-AGIR-001"]
  CAP_AGIR -->|regra| RULE_AGIR_001
  RULE_AGIR_001 -.->|verifica| TEST_workspace_target_tests_test_no_backup_py
  RULE_AGIR_001 -.->|verifica| TEST_workspace_target_tests_test_prune_v12_py
  RULE_AGIR_001 -.->|verifica| TEST_workspace_target_tests_test_summary_py
  RULE_AGIR_002["RULE-AGIR-002"]
  CAP_AGIR -->|regra| RULE_AGIR_002
  RULE_AGIR_002 -.->|verifica| TEST_workspace_target_tests_test_ack_audit_py
  RULE_AGIR_002 -.->|verifica| TEST_workspace_target_tests_test_ciclo_acao_sintetico_py
  RULE_AGIR_002 -.->|verifica| TEST_workspace_target_tests_test_deploy_credencial_py
  RULE_AGIR_002 -.->|verifica| TEST_workspace_target_tests_test_hardening_b11_py
  RULE_AGIR_002 -.->|verifica| TEST_workspace_target_tests_test_prune_sintetico_py
  RULE_AGIR_002 -.->|verifica| TEST_workspace_target_tests_test_rotas_rail_py
  RULE_AGIR_002 -.->|verifica| TEST_workspace_target_tests_test_session_py
  RULE_AGIR_002 -.->|verifica| TEST_workspace_target_tests_test_unlock_v8_py
  RULE_DIAG_001["RULE-DIAG-001"]
  CAP_DIAGNOSTICAR -->|regra| RULE_DIAG_001
  RULE_DIAG_001 -.->|verifica| TEST_workspace_target_tests_test_certs_sprint5_py
  RULE_DIAG_001 -.->|verifica| TEST_workspace_target_tests_test_config_ingress_path_py
  RULE_DIAG_001 -.->|verifica| TEST_workspace_target_tests_test_drift_b8_py
  RULE_DIAG_001 -.->|verifica| TEST_workspace_target_tests_test_f6_palette_py
  RULE_DIAG_001 -.->|verifica| TEST_workspace_target_tests_test_findings_py
  RULE_DIAG_001 -.->|verifica| TEST_workspace_target_tests_test_guarda_schema_literal_py
  RULE_DIAG_001 -.->|verifica| TEST_workspace_target_tests_test_ingress_parser_py
  RULE_DIAG_001 -.->|verifica| TEST_workspace_target_tests_test_no_backup_py
  RULE_DIAG_001 -.->|verifica| TEST_workspace_target_tests_test_regras_container_parado_py
  RULE_DIAG_001 -.->|verifica| TEST_workspace_target_tests_test_telas_topologia_plantao_py
  RULE_DIAG_001 -.->|verifica| TEST_workspace_target_tests_test_updates_ui_py
  RULE_NARRAR_001["RULE-NARRAR-001"]
  CAP_NARRAR -->|regra| RULE_NARRAR_001
  RULE_NARRAR_001 -.->|verifica| TEST_workspace_target_tests_fixtures_exercita_kernel_mjs
  RULE_NARRAR_001 -.->|verifica| TEST_workspace_target_tests_fixtures_exercita_notificacoes_mjs
  RULE_NARRAR_001 -.->|verifica| TEST_workspace_target_tests_fixtures_exercita_render_vivo_mjs
  RULE_NARRAR_001 -.->|verifica| TEST_workspace_target_tests_fixtures_exercita_updates_mjs
  RULE_NARRAR_001 -.->|verifica| TEST_workspace_target_tests_test_acessibilidade_py
  RULE_NARRAR_001 -.->|verifica| TEST_workspace_target_tests_test_contraste_severidade_py
  RULE_NARRAR_001 -.->|verifica| TEST_workspace_target_tests_test_frontend_modulos_py
  RULE_NARRAR_001 -.->|verifica| TEST_workspace_target_tests_test_kernel_cockpit_py
  RULE_NARRAR_001 -.->|verifica| TEST_workspace_target_tests_test_notificacoes_ui_py
  RULE_NARRAR_001 -.->|verifica| TEST_workspace_target_tests_test_render_vivo_py
  RULE_NARRAR_001 -.->|verifica| TEST_workspace_target_tests_test_telas_renderizam_py
  RULE_OBSERVAR_001["RULE-OBSERVAR-001"]
  CAP_OBSERVAR -->|regra| RULE_OBSERVAR_001
  RULE_OBSERVAR_001 -.->|verifica| TEST_workspace_target_tests_test_projects_security_py
  RULE_OBSERVAR_001 -.->|verifica| TEST_workspace_target_tests_test_updates_v14_py
  RULE_SUSTENTAR_001["RULE-SUSTENTAR-001"]
  CAP_SUSTENTAR -->|regra| RULE_SUSTENTAR_001
  RULE_SUSTENTAR_001 -.->|verifica| TEST_workspace_target_tests_test_container_history_py
  RULE_SUSTENTAR_001 -.->|verifica| TEST_workspace_target_tests_test_db_py
  RULE_SUSTENTAR_001 -.->|verifica| TEST_workspace_target_tests_test_events_v11_py
  RULE_SUSTENTAR_001 -.->|verifica| TEST_workspace_target_tests_test_migration_py
  RULE_SUSTENTAR_001 -.->|verifica| TEST_workspace_target_tests_test_no_backup_py
  RULE_SUSTENTAR_002["RULE-SUSTENTAR-002"]
  CAP_SUSTENTAR -->|regra| RULE_SUSTENTAR_002
  RULE_SUSTENTAR_002 -.->|verifica| TEST_workspace_target_tests_test_cabecalhos_seguranca_py
  RULE_SUSTENTAR_002 -.->|verifica| TEST_workspace_target_tests_test_cache_py
  RULE_SUSTENTAR_002 -.->|verifica| TEST_workspace_target_tests_test_cache_http_py
  RULE_SUSTENTAR_002 -.->|verifica| TEST_workspace_target_tests_test_capacidade_cards_py
  RULE_SUSTENTAR_002 -.->|verifica| TEST_workspace_target_tests_test_security_py
  RULE_SUSTENTAR_002 -.->|verifica| TEST_workspace_target_tests_test_sinais_de_maturidade_py
  RULE_SUSTENTAR_003["RULE-SUSTENTAR-003"]
  CAP_SUSTENTAR -->|regra| RULE_SUSTENTAR_003
  RULE_SUSTENTAR_003 -.->|verifica| TEST_workspace_target_tests_test_api_py
  RULE_SUSTENTAR_004["RULE-SUSTENTAR-004"]
  CAP_SUSTENTAR -->|regra| RULE_SUSTENTAR_004
  RULE_SUSTENTAR_004 -.->|verifica| TEST_workspace_target_tests_test_config_ingress_path_py
  RULE_SUSTENTAR_004 -.->|verifica| TEST_workspace_target_tests_test_deploy_credencial_py
  UI_COCKPIT_EXECUTIVO["UI-COCKPIT-EXECUTIVO"]
  UI_COCKPIT_EXECUTIVO -->|experiência| CAP_NARRAR
  UI_COCKPIT_EXECUTIVO -.->|satisfaz| REQ_017
  UI_COCKPIT_PAINEL["UI-COCKPIT-PAINEL"]
  UI_COCKPIT_PAINEL -->|experiência| CAP_NARRAR
  UI_COCKPIT_PAINEL -.->|satisfaz| REQ_020
  UI_COCKPIT_PAINEL -.->|satisfaz| REQ_026
  MET_ACAO_AUDITADA[["MET-ACAO-AUDITADA"]]
  MET_ATENCAO[["MET-ATENCAO"]]
  MET_COMPARAVEL[["MET-COMPARAVEL"]]
  MET_FRONTEIRA[["MET-FRONTEIRA"]]
  MET_LEITURA_ESTAVEL[["MET-LEITURA-ESTAVEL"]]
  MET_PENDENCIA[["MET-PENDENCIA"]]
  MET_SUPERFICIE[["MET-SUPERFICIE"]]
  REQ_001["REQ-001<br/>done"]
  REQ_001 -->|requisito| CAP_OBSERVAR
  REQ_001 ==>|move| MET_SUPERFICIE
  REQ_001 -.->|validado por| TEST_workspace_target_tests_test_api_py
  REQ_002["REQ-002<br/>done"]
  REQ_002 -->|requisito| CAP_OBSERVAR
  REQ_002 ==>|move| MET_ATENCAO
  REQ_002 -.->|validado por| TEST_workspace_target_tests_test_logs_texto_py
  REQ_003["REQ-003<br/>done"]
  REQ_003 -->|requisito| CAP_OBSERVAR
  REQ_003 ==>|move| MET_ATENCAO
  REQ_003 -.->|validado por| TEST_workspace_target_tests_test_api_py
  REQ_004["REQ-004<br/>done"]
  REQ_004 -->|requisito| CAP_DIAGNOSTICAR
  REQ_004 ==>|move| MET_ATENCAO
  REQ_004 -.->|validado por| TEST_workspace_target_tests_test_findings_py
  REQ_004 -.->|validado por| TEST_workspace_target_tests_test_telas_topologia_plantao_py
  REQ_005["REQ-005<br/>done"]
  REQ_005 -->|requisito| CAP_DIAGNOSTICAR
  REQ_005 ==>|move| MET_ATENCAO
  REQ_005 -.->|regido por| RULE_DIAG_001
  REQ_005 -.->|validado por| TEST_workspace_target_tests_test_findings_py
  REQ_005 -.->|validado por| TEST_workspace_target_tests_test_regras_container_parado_py
  REQ_006["REQ-006<br/>done"]
  REQ_006 -->|requisito| CAP_DIAGNOSTICAR
  REQ_006 ==>|move| MET_ATENCAO
  REQ_006 -.->|validado por| TEST_workspace_target_tests_test_certs_sprint5_py
  REQ_007["REQ-007<br/>done"]
  REQ_007 -->|requisito| CAP_DIAGNOSTICAR
  REQ_007 ==>|move| MET_ATENCAO
  REQ_007 -.->|validado por| TEST_workspace_target_tests_test_drift_b8_py
  REQ_008["REQ-008<br/>done"]
  REQ_008 -->|requisito| CAP_DIAGNOSTICAR
  REQ_008 ==>|move| MET_ATENCAO
  REQ_008 -.->|validado por| TEST_workspace_target_tests_test_updates_ui_py
  REQ_008 -.->|validado por| TEST_workspace_target_tests_test_updates_v14_py
  REQ_009["REQ-009<br/>done"]
  REQ_009 -->|requisito| CAP_DIAGNOSTICAR
  REQ_009 ==>|move| MET_ATENCAO
  REQ_009 -.->|validado por| TEST_workspace_target_tests_test_ingress_parser_py
  REQ_009 -.->|validado por| TEST_workspace_target_tests_test_telas_topologia_plantao_py
  REQ_010["REQ-010<br/>done"]
  REQ_010 -->|requisito| CAP_AGIR
  REQ_010 ==>|move| MET_ACAO_AUDITADA
  REQ_010 -.->|regido por| RULE_AGIR_001
  REQ_010 -.->|validado por| TEST_workspace_target_tests_test_ciclo_acao_sintetico_py
  REQ_010 -.->|validado por| TEST_workspace_target_tests_test_prune_sintetico_py
  REQ_011["REQ-011<br/>done"]
  REQ_011 -->|requisito| CAP_AGIR
  REQ_011 ==>|move| MET_ACAO_AUDITADA
  REQ_011 -.->|regido por| RULE_AGIR_001
  REQ_011 -.->|validado por| TEST_workspace_target_tests_test_ciclo_acao_sintetico_py
  REQ_012["REQ-012<br/>done"]
  REQ_012 -->|requisito| CAP_AGIR
  REQ_012 ==>|move| MET_ACAO_AUDITADA
  REQ_012 -.->|regido por| RULE_AGIR_002
  REQ_012 -.->|validado por| TEST_workspace_target_tests_test_hardening_b11_py
  REQ_012 -.->|validado por| TEST_workspace_target_tests_test_session_py
  REQ_012 -.->|validado por| TEST_workspace_target_tests_test_unlock_v8_py
  REQ_013["REQ-013<br/>done"]
  REQ_013 -->|requisito| CAP_AGIR
  REQ_013 ==>|move| MET_ACAO_AUDITADA
  REQ_013 -.->|regido por| RULE_AGIR_002
  REQ_013 -.->|validado por| TEST_workspace_target_tests_test_ack_audit_py
  REQ_014["REQ-014<br/>done"]
  REQ_014 -->|requisito| CAP_DIAGNOSTICAR
  REQ_014 ==>|move| MET_ACAO_AUDITADA
  REQ_014 -.->|validado por| TEST_workspace_target_tests_test_findings_py
  REQ_015["REQ-015<br/>done"]
  REQ_015 -->|requisito| CAP_NARRAR
  REQ_015 ==>|move| MET_ATENCAO
  REQ_015 -.->|validado por| TEST_workspace_target_tests_test_events_rota_py
  REQ_015 -.->|validado por| TEST_workspace_target_tests_test_events_v11_py
  REQ_016["REQ-016<br/>done"]
  REQ_016 -->|requisito| CAP_NARRAR
  REQ_016 ==>|move| MET_LEITURA_ESTAVEL
  REQ_016 -.->|validado por| TEST_workspace_target_tests_fixtures_renderiza_capacidade_mjs
  REQ_016 -.->|validado por| TEST_workspace_target_tests_test_capacidade_serie_curta_py
  REQ_017["REQ-017<br/>done"]
  REQ_017 -->|requisito| CAP_NARRAR
  REQ_017 ==>|move| MET_ATENCAO
  REQ_017 -.->|validado por| TEST_workspace_target_tests_test_executive_py
  REQ_017 -.->|validado por| TEST_workspace_target_tests_test_summary_py
  REQ_018["REQ-018<br/>done"]
  REQ_018 -->|requisito| CAP_NARRAR
  REQ_018 ==>|move| MET_ATENCAO
  REQ_018 -.->|validado por| TEST_workspace_target_tests_test_notificacoes_ui_py
  REQ_018 -.->|validado por| TEST_workspace_target_tests_test_notify_v15_py
  REQ_019["REQ-019<br/>done"]
  REQ_019 -->|requisito| CAP_AGIR
  REQ_019 ==>|move| MET_ACAO_AUDITADA
  REQ_019 -.->|validado por| TEST_workspace_target_tests_test_tasks_py
  REQ_019 -.->|validado por| TEST_workspace_target_tests_test_tasks_api_py
  REQ_020["REQ-020<br/>done"]
  REQ_020 -->|requisito| CAP_NARRAR
  REQ_020 ==>|move| MET_LEITURA_ESTAVEL
  REQ_020 -.->|regido por| RULE_NARRAR_001
  REQ_020 -.->|validado por| TEST_workspace_target_tests_fixtures_exercita_render_vivo_mjs
  REQ_020 -.->|validado por| TEST_workspace_target_tests_test_frontend_modulos_py
  REQ_021["REQ-021<br/>done"]
  REQ_021 -->|requisito| CAP_NARRAR
  REQ_021 ==>|move| MET_LEITURA_ESTAVEL
  REQ_021 -.->|validado por| TEST_workspace_target_tests_fixtures_exercita_kernel_mjs
  REQ_021 -.->|validado por| TEST_workspace_target_tests_test_kernel_cockpit_py
  REQ_022["REQ-022<br/>done"]
  REQ_022 -->|requisito| CAP_NARRAR
  REQ_022 ==>|move| MET_ATENCAO
  REQ_022 -.->|validado por| TEST_workspace_target_tests_fixtures_exercita_telas_mjs
  REQ_022 -.->|validado por| TEST_workspace_target_tests_fixtures_renderiza_telas_mjs
  REQ_023["REQ-023<br/>done"]
  REQ_023 -->|requisito| CAP_NARRAR
  REQ_023 ==>|move| MET_LEITURA_ESTAVEL
  REQ_023 -.->|validado por| TEST_workspace_target_tests_test_frescor_amostra_py
  REQ_023 -.->|validado por| TEST_workspace_target_tests_test_offline_py
  REQ_024["REQ-024<br/>done"]
  REQ_024 -->|requisito| CAP_NARRAR
  REQ_024 ==>|move| MET_LEITURA_ESTAVEL
  REQ_024 -.->|validado por| TEST_workspace_target_tests_test_backend_py
  REQ_025["REQ-025<br/>done"]
  REQ_025 -->|requisito| CAP_NARRAR
  REQ_025 ==>|move| MET_COMPARAVEL
  REQ_025 -.->|validado por| TEST_workspace_target_tests_test_metrics_py
  REQ_025 -.->|validado por| TEST_workspace_target_tests_test_metrics_prom_py
  REQ_026["REQ-026<br/>done"]
  REQ_026 -->|requisito| CAP_NARRAR
  REQ_026 ==>|move| MET_LEITURA_ESTAVEL
  REQ_026 -.->|validado por| TEST_workspace_target_tests_test_acessibilidade_py
  REQ_027["REQ-027<br/>done"]
  REQ_027 -->|requisito| CAP_NARRAR
  REQ_027 ==>|move| MET_ATENCAO
  REQ_027 -.->|validado por| TEST_workspace_target_tests_test_logs_fts_v13_py
  RISK_ALVO_001["RISK-ALVO-001"]
  RISK_ALVO_002["RISK-ALVO-002"]
  RISK_CARCACA_001["RISK-CARCACA-001"]
  RISK_CHANGE_001["RISK-CHANGE-001"]
  RISK_DEP_001["RISK-DEP-001"]
  RISK_DIAG_001["RISK-DIAG-001"]
  RISK_EXT_002["RISK-EXT-002"]
  RISK_HOMOLOG_001["RISK-HOMOLOG-001"]
  RISK_META_001["RISK-META-001"]
  RISK_MOLDE_001["RISK-MOLDE-001"]
  RISK_SEGREDO_001["RISK-SEGREDO-001"]
  RISK_SOCKET_001["RISK-SOCKET-001"]
  RISK_WEBQA_001["RISK-WEBQA-001"]
  ADR_001["ADR-001"]
  ADR_001 -->|mitiga| RISK_WEBQA_001
  ADR_002["ADR-002"]
  ADR_002 -->|mitiga| RISK_META_001
  ADR_003["ADR-003"]
  ADR_003 -->|mitiga| RISK_DEP_001
  ADR_004["ADR-004"]
  ADR_004 -->|mitiga| RISK_CHANGE_001
  ADR_015["ADR-015"]
  ADR_015 -->|mitiga| RISK_ALVO_001
  ADR_016["ADR-016"]
  ADR_016 -->|mitiga| RISK_ALVO_001
  ADR_016 -->|mitiga| RISK_SEGREDO_001
  ADR_017["ADR-017"]
  ADR_017 -->|mitiga| RISK_ALVO_001
  ADR_017 -->|mitiga| RISK_HOMOLOG_001
  ADR_018["ADR-018"]
  ADR_018 -->|mitiga| RISK_ALVO_001
  ADR_018 -->|mitiga| RISK_HOMOLOG_001
  classDef project fill:#1f2937,stroke:#111827,color:#fff;
  class PROJ_danzeroum_projectcockpitdocker project;
  classDef cap fill:#2563eb,stroke:#1e40af,color:#fff;
  class CAP_AGIR,CAP_DIAGNOSTICAR,CAP_NARRAR,CAP_OBSERVAR,CAP_SUSTENTAR cap;
  classDef cmp fill:#0891b2,stroke:#0e7490,color:#fff;
  class CMP_ACHADOS,CMP_APP,CMP_ATUALIZACOES,CMP_BARREIRA_ACOES,CMP_CERTS,CMP_CONTAINERS,CMP_DRIFT,CMP_EMPACOTAMENTO,CMP_EVENTOS,CMP_INGRESS,CMP_INVENTARIO_HOST,CMP_LOGS_BUSCA,CMP_MASCARAMENTO,CMP_NOTIFICACOES,CMP_OPERACOES,CMP_PERSISTENCIA,CMP_POLITICA_RESPOSTA,CMP_PROXY,CMP_REGRAS_ACHADO,CMP_RESUMO,CMP_SERIES,CMP_SESSAO,CMP_TELA_ATENCAO,CMP_TELA_AUDITORIA,CMP_TELA_BACKEND,CMP_TELA_CAPACIDADE,CMP_TELA_EXECUTIVO,CMP_TELA_INGRESS,CMP_TELA_PLANTAO,CMP_TELA_PROJETOS,CMP_TELA_TAREFAS,CMP_TELA_TOPOLOGIA,CMP_UI_CASCA,CMP_UI_INFRA,CMP_UI_KERNEL,CMP_UI_MODULOS_INLINE cmp;
  classDef ifc fill:#7c3aed,stroke:#5b21b6,color:#fff;
  classDef rule fill:#16a34a,stroke:#15803d,color:#fff;
  class RULE_AGIR_001,RULE_AGIR_002,RULE_DIAG_001,RULE_NARRAR_001,RULE_OBSERVAR_001,RULE_SUSTENTAR_001,RULE_SUSTENTAR_002,RULE_SUSTENTAR_003,RULE_SUSTENTAR_004 rule;
  classDef ui fill:#db2777,stroke:#9d174d,color:#fff;
  class UI_COCKPIT_EXECUTIVO,UI_COCKPIT_PAINEL ui;
  classDef req fill:#0d9488,stroke:#0f766e,color:#fff;
  class REQ_001,REQ_002,REQ_003,REQ_004,REQ_005,REQ_006,REQ_007,REQ_008,REQ_009,REQ_010,REQ_011,REQ_012,REQ_013,REQ_014,REQ_015,REQ_016,REQ_017,REQ_018,REQ_019,REQ_020,REQ_021,REQ_022,REQ_023,REQ_024,REQ_025,REQ_026,REQ_027 req;
  classDef met fill:#ea580c,stroke:#c2410c,color:#fff;
  class MET_ACAO_AUDITADA,MET_ATENCAO,MET_COMPARAVEL,MET_FRONTEIRA,MET_LEITURA_ESTAVEL,MET_PENDENCIA,MET_SUPERFICIE met;
  classDef test fill:#57534e,stroke:#44403c,color:#fff;
  class TEST_workspace_target_tests_fixtures_exercita_kernel_mjs,TEST_workspace_target_tests_fixtures_exercita_notificacoes_mjs,TEST_workspace_target_tests_fixtures_exercita_render_vivo_mjs,TEST_workspace_target_tests_fixtures_exercita_rotas_mjs,TEST_workspace_target_tests_fixtures_exercita_telas_mjs,TEST_workspace_target_tests_fixtures_exercita_updates_mjs,TEST_workspace_target_tests_fixtures_renderiza_capacidade_mjs,TEST_workspace_target_tests_fixtures_renderiza_telas_mjs,TEST_workspace_target_tests_test_acessibilidade_py,TEST_workspace_target_tests_test_ack_audit_py,TEST_workspace_target_tests_test_api_py,TEST_workspace_target_tests_test_backend_py,TEST_workspace_target_tests_test_cabecalhos_seguranca_py,TEST_workspace_target_tests_test_cache_py,TEST_workspace_target_tests_test_cache_http_py,TEST_workspace_target_tests_test_capacidade_cards_py,TEST_workspace_target_tests_test_capacidade_serie_curta_py,TEST_workspace_target_tests_test_certs_sprint5_py,TEST_workspace_target_tests_test_ciclo_acao_sintetico_py,TEST_workspace_target_tests_test_config_ingress_path_py,TEST_workspace_target_tests_test_container_history_py,TEST_workspace_target_tests_test_contraste_severidade_py,TEST_workspace_target_tests_test_db_py,TEST_workspace_target_tests_test_deploy_credencial_py,TEST_workspace_target_tests_test_drift_b8_py,TEST_workspace_target_tests_test_events_rota_py,TEST_workspace_target_tests_test_events_v11_py,TEST_workspace_target_tests_test_executive_py,TEST_workspace_target_tests_test_f6_palette_py,TEST_workspace_target_tests_test_findings_py,TEST_workspace_target_tests_test_frescor_amostra_py,TEST_workspace_target_tests_test_frontend_modulos_py,TEST_workspace_target_tests_test_guarda_docs_registro_py,TEST_workspace_target_tests_test_guarda_schema_literal_py,TEST_workspace_target_tests_test_hardening_b11_py,TEST_workspace_target_tests_test_history_route_py,TEST_workspace_target_tests_test_ingress_parser_py,TEST_workspace_target_tests_test_kernel_cockpit_py,TEST_workspace_target_tests_test_logs_fts_v13_py,TEST_workspace_target_tests_test_logs_texto_py,TEST_workspace_target_tests_test_metrics_py,TEST_workspace_target_tests_test_metrics_prom_py,TEST_workspace_target_tests_test_migration_py,TEST_workspace_target_tests_test_no_backup_py,TEST_workspace_target_tests_test_notificacoes_ui_py,TEST_workspace_target_tests_test_notify_v15_py,TEST_workspace_target_tests_test_offline_py,TEST_workspace_target_tests_test_projects_security_py,TEST_workspace_target_tests_test_prune_sintetico_py,TEST_workspace_target_tests_test_prune_v12_py,TEST_workspace_target_tests_test_regras_container_parado_py,TEST_workspace_target_tests_test_render_vivo_py,TEST_workspace_target_tests_test_rotas_rail_py,TEST_workspace_target_tests_test_sampler_py,TEST_workspace_target_tests_test_security_py,TEST_workspace_target_tests_test_session_py,TEST_workspace_target_tests_test_sinais_de_maturidade_py,TEST_workspace_target_tests_test_storage_py,TEST_workspace_target_tests_test_summary_py,TEST_workspace_target_tests_test_tasks_py,TEST_workspace_target_tests_test_tasks_api_py,TEST_workspace_target_tests_test_telas_renderizam_py,TEST_workspace_target_tests_test_telas_topologia_plantao_py,TEST_workspace_target_tests_test_unlock_v8_py,TEST_workspace_target_tests_test_updates_ui_py,TEST_workspace_target_tests_test_updates_v14_py test;
  classDef adr fill:#ca8a04,stroke:#a16207,color:#fff;
  class ADR_001,ADR_002,ADR_003,ADR_004,ADR_015,ADR_016,ADR_017,ADR_018 adr;
  classDef risk fill:#dc2626,stroke:#991b1b,color:#fff;
  class RISK_ALVO_001,RISK_ALVO_002,RISK_CARCACA_001,RISK_CHANGE_001,RISK_DEP_001,RISK_DIAG_001,RISK_EXT_002,RISK_HOMOLOG_001,RISK_META_001,RISK_MOLDE_001,RISK_SEGREDO_001,RISK_SOCKET_001,RISK_WEBQA_001 risk;
```

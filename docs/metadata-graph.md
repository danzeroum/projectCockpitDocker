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
  CMP_DRIFT["CMP-DRIFT<br/>drift.py"]
  CMP_DRIFT -->|realiza| CAP_DIAGNOSTICAR
  CMP_DRIFT -->|depende| CMP_MASCARAMENTO
  CMP_DRIFT -->|depende| CMP_POLITICA_RESPOSTA
  CMP_DRIFT -->|depende| CMP_SERIES
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
  CMP_EVENTOS -.->|testa| TEST_workspace_target_tests_test_cabecalhos_seguranca_py
  CMP_EVENTOS -.->|testa| TEST_workspace_target_tests_test_events_rota_py
  CMP_EVENTOS -.->|testa| TEST_workspace_target_tests_test_events_v11_py
  CMP_INGRESS["CMP-INGRESS<br/>parser.py"]
  CMP_INGRESS -->|realiza| CAP_DIAGNOSTICAR
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
  CMP_TELA_ATENCAO["CMP-TELA-ATENCAO<br/>atencao.js"]
  CMP_TELA_ATENCAO -->|realiza| CAP_NARRAR
  CMP_TELA_ATENCAO -->|depende| CMP_UI_INFRA
  CMP_TELA_ATENCAO -->|depende| CMP_UI_KERNEL
  CMP_TELA_ATENCAO -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_AUDITORIA["CMP-TELA-AUDITORIA<br/>auditoria.js"]
  CMP_TELA_AUDITORIA -->|realiza| CAP_NARRAR
  CMP_TELA_AUDITORIA -->|depende| CMP_UI_INFRA
  CMP_TELA_AUDITORIA -->|depende| CMP_UI_KERNEL
  CMP_TELA_AUDITORIA -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_BACKEND["CMP-TELA-BACKEND<br/>backend.js"]
  CMP_TELA_BACKEND -->|realiza| CAP_NARRAR
  CMP_TELA_BACKEND -->|depende| CMP_UI_INFRA
  CMP_TELA_BACKEND -->|depende| CMP_UI_KERNEL
  CMP_TELA_BACKEND -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_CAPACIDADE["CMP-TELA-CAPACIDADE<br/>capacidade.js"]
  CMP_TELA_CAPACIDADE -->|realiza| CAP_NARRAR
  CMP_TELA_CAPACIDADE -->|depende| CMP_UI_INFRA
  CMP_TELA_CAPACIDADE -->|depende| CMP_UI_KERNEL
  CMP_TELA_CAPACIDADE -.->|testa| TEST_workspace_target_tests_fixtures_renderiza_capacidade_mjs
  CMP_TELA_CAPACIDADE -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_EXECUTIVO["CMP-TELA-EXECUTIVO<br/>executivo.js"]
  CMP_TELA_EXECUTIVO -->|realiza| CAP_NARRAR
  CMP_TELA_EXECUTIVO -->|depende| CMP_UI_INFRA
  CMP_TELA_EXECUTIVO -->|depende| CMP_UI_KERNEL
  CMP_TELA_EXECUTIVO -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_INGRESS["CMP-TELA-INGRESS<br/>ingress.js"]
  CMP_TELA_INGRESS -->|realiza| CAP_NARRAR
  CMP_TELA_INGRESS -->|depende| CMP_UI_INFRA
  CMP_TELA_INGRESS -->|depende| CMP_UI_KERNEL
  CMP_TELA_INGRESS -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_PLANTAO["CMP-TELA-PLANTAO<br/>plantao.js"]
  CMP_TELA_PLANTAO -->|realiza| CAP_NARRAR
  CMP_TELA_PLANTAO -->|depende| CMP_UI_INFRA
  CMP_TELA_PLANTAO -->|depende| CMP_UI_KERNEL
  CMP_TELA_PLANTAO -.->|testa| TEST_workspace_target_tests_fixtures_exercita_telas_mjs
  CMP_TELA_PLANTAO -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_PROJETOS["CMP-TELA-PROJETOS<br/>projetos.js"]
  CMP_TELA_PROJETOS -->|realiza| CAP_NARRAR
  CMP_TELA_PROJETOS -->|depende| CMP_UI_INFRA
  CMP_TELA_PROJETOS -->|depende| CMP_UI_KERNEL
  CMP_TELA_PROJETOS -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_TAREFAS["CMP-TELA-TAREFAS<br/>tarefas.js"]
  CMP_TELA_TAREFAS -->|realiza| CAP_NARRAR
  CMP_TELA_TAREFAS -->|depende| CMP_UI_INFRA
  CMP_TELA_TAREFAS -->|depende| CMP_UI_KERNEL
  CMP_TELA_TAREFAS -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_TELA_TOPOLOGIA["CMP-TELA-TOPOLOGIA<br/>topologia.js"]
  CMP_TELA_TOPOLOGIA -->|realiza| CAP_NARRAR
  CMP_TELA_TOPOLOGIA -->|depende| CMP_UI_INFRA
  CMP_TELA_TOPOLOGIA -->|depende| CMP_UI_KERNEL
  CMP_TELA_TOPOLOGIA -.->|testa| TEST_workspace_target_tests_fixtures_exercita_telas_mjs
  CMP_TELA_TOPOLOGIA -.->|testa| TEST_workspace_target_tests_fixtures_renderiza_telas_mjs
  CMP_TELA_TOPOLOGIA -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_UI_CASCA["CMP-UI-CASCA<br/>index.html"]
  CMP_UI_CASCA -->|realiza| CAP_NARRAR
  CMP_UI_CASCA -.->|testa| TEST_workspace_target_tests_test_acessibilidade_py
  CMP_UI_CASCA -.->|testa| TEST_workspace_target_tests_test_contraste_severidade_py
  CMP_UI_INFRA["CMP-UI-INFRA<br/>commands.js"]
  CMP_UI_INFRA -->|realiza| CAP_NARRAR
  CMP_UI_INFRA -->|depende| CMP_UI_KERNEL
  CMP_UI_INFRA -.->|testa| TEST_workspace_target_tests_fixtures_exercita_notificacoes_mjs
  CMP_UI_INFRA -.->|testa| TEST_workspace_target_tests_fixtures_exercita_updates_mjs
  CMP_UI_INFRA -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_UI_INFRA -.->|testa| TEST_workspace_target_tests_test_notificacoes_ui_py
  CMP_UI_KERNEL["CMP-UI-KERNEL<br/>app.js"]
  CMP_UI_KERNEL -->|realiza| CAP_NARRAR
  CMP_UI_KERNEL -->|depende| CMP_UI_INFRA
  CMP_UI_KERNEL -->|depende| CMP_UI_MODULOS_INLINE
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
  CMP_UI_MODULOS_INLINE -.->|testa| TEST_workspace_target_tests_test_frontend_modulos_py
  CMP_UI_MODULOS_INLINE -.->|testa| TEST_workspace_target_tests_test_notificacoes_ui_py
  UI_COCKPIT_EXECUTIVO["UI-COCKPIT-EXECUTIVO"]
  UI_COCKPIT_EXECUTIVO -->|experiência| CAP_NARRAR
  UI_COCKPIT_PAINEL["UI-COCKPIT-PAINEL"]
  UI_COCKPIT_PAINEL -->|experiência| CAP_NARRAR
  MET_COMPARAVEL[["MET-COMPARAVEL"]]
  MET_FRONTEIRA[["MET-FRONTEIRA"]]
  MET_PENDENCIA[["MET-PENDENCIA"]]
  RISK_ALVO_001["RISK-ALVO-001"]
  RISK_ALVO_002["RISK-ALVO-002"]
  RISK_CARCACA_001["RISK-CARCACA-001"]
  RISK_CHANGE_001["RISK-CHANGE-001"]
  RISK_DEP_001["RISK-DEP-001"]
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
  classDef ui fill:#db2777,stroke:#9d174d,color:#fff;
  class UI_COCKPIT_EXECUTIVO,UI_COCKPIT_PAINEL ui;
  classDef req fill:#0d9488,stroke:#0f766e,color:#fff;
  classDef met fill:#ea580c,stroke:#c2410c,color:#fff;
  class MET_COMPARAVEL,MET_FRONTEIRA,MET_PENDENCIA met;
  classDef test fill:#57534e,stroke:#44403c,color:#fff;
  class TEST_workspace_target_tests_fixtures_exercita_kernel_mjs,TEST_workspace_target_tests_fixtures_exercita_notificacoes_mjs,TEST_workspace_target_tests_fixtures_exercita_render_vivo_mjs,TEST_workspace_target_tests_fixtures_exercita_rotas_mjs,TEST_workspace_target_tests_fixtures_exercita_telas_mjs,TEST_workspace_target_tests_fixtures_exercita_updates_mjs,TEST_workspace_target_tests_fixtures_renderiza_capacidade_mjs,TEST_workspace_target_tests_fixtures_renderiza_telas_mjs,TEST_workspace_target_tests_test_acessibilidade_py,TEST_workspace_target_tests_test_ack_audit_py,TEST_workspace_target_tests_test_api_py,TEST_workspace_target_tests_test_backend_py,TEST_workspace_target_tests_test_cabecalhos_seguranca_py,TEST_workspace_target_tests_test_cache_py,TEST_workspace_target_tests_test_cache_http_py,TEST_workspace_target_tests_test_capacidade_cards_py,TEST_workspace_target_tests_test_capacidade_serie_curta_py,TEST_workspace_target_tests_test_certs_sprint5_py,TEST_workspace_target_tests_test_ciclo_acao_sintetico_py,TEST_workspace_target_tests_test_config_ingress_path_py,TEST_workspace_target_tests_test_container_history_py,TEST_workspace_target_tests_test_contraste_severidade_py,TEST_workspace_target_tests_test_db_py,TEST_workspace_target_tests_test_deploy_credencial_py,TEST_workspace_target_tests_test_drift_b8_py,TEST_workspace_target_tests_test_events_rota_py,TEST_workspace_target_tests_test_events_v11_py,TEST_workspace_target_tests_test_executive_py,TEST_workspace_target_tests_test_f6_palette_py,TEST_workspace_target_tests_test_findings_py,TEST_workspace_target_tests_test_frescor_amostra_py,TEST_workspace_target_tests_test_frontend_modulos_py,TEST_workspace_target_tests_test_guarda_docs_registro_py,TEST_workspace_target_tests_test_guarda_schema_literal_py,TEST_workspace_target_tests_test_hardening_b11_py,TEST_workspace_target_tests_test_history_route_py,TEST_workspace_target_tests_test_ingress_parser_py,TEST_workspace_target_tests_test_kernel_cockpit_py,TEST_workspace_target_tests_test_logs_fts_v13_py,TEST_workspace_target_tests_test_logs_texto_py,TEST_workspace_target_tests_test_metrics_py,TEST_workspace_target_tests_test_metrics_prom_py,TEST_workspace_target_tests_test_migration_py,TEST_workspace_target_tests_test_no_backup_py,TEST_workspace_target_tests_test_notificacoes_ui_py,TEST_workspace_target_tests_test_notify_v15_py,TEST_workspace_target_tests_test_offline_py,TEST_workspace_target_tests_test_projects_security_py,TEST_workspace_target_tests_test_prune_sintetico_py,TEST_workspace_target_tests_test_prune_v12_py,TEST_workspace_target_tests_test_regras_container_parado_py,TEST_workspace_target_tests_test_render_vivo_py,TEST_workspace_target_tests_test_rotas_rail_py,TEST_workspace_target_tests_test_sampler_py,TEST_workspace_target_tests_test_session_py,TEST_workspace_target_tests_test_sinais_de_maturidade_py,TEST_workspace_target_tests_test_storage_py,TEST_workspace_target_tests_test_summary_py,TEST_workspace_target_tests_test_tasks_py,TEST_workspace_target_tests_test_tasks_api_py,TEST_workspace_target_tests_test_telas_renderizam_py,TEST_workspace_target_tests_test_telas_topologia_plantao_py,TEST_workspace_target_tests_test_unlock_v8_py,TEST_workspace_target_tests_test_updates_ui_py,TEST_workspace_target_tests_test_updates_v14_py test;
  classDef adr fill:#ca8a04,stroke:#a16207,color:#fff;
  class ADR_001,ADR_002,ADR_003,ADR_004,ADR_015,ADR_016,ADR_017,ADR_018 adr;
  classDef risk fill:#dc2626,stroke:#991b1b,color:#fff;
  class RISK_ALVO_001,RISK_ALVO_002,RISK_CARCACA_001,RISK_CHANGE_001,RISK_DEP_001,RISK_HOMOLOG_001,RISK_META_001,RISK_MOLDE_001,RISK_SEGREDO_001,RISK_SOCKET_001,RISK_WEBQA_001 risk;
```

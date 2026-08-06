# ADR-018 — A bancada de homologação é etapa governada, não isenção

- **Status:** accepted
- **Data:** 2026-08-06
- **Contexto:** CP-003, fatia-4 (a divisão que extraiu `src/cockpit_harness/`)
- **Supersede:** nada. Complementa a ADR-017, que decidiu que o stack de homologação mora aqui.

## O problema

`deploy/homologacao/` — três arquivos: um compose, um `.env.example` e um script de ingress —
não pertencia a etapa alguma de `harness/stages.yaml`, nem a uma isenção declarada. A partição do
repositório acusava os três, corretamente.

A saída barata era declarar `deploy/` isento. Ela está errada, e o motivo é o que este ADR
registra: **isenção custa a evidência**. Um stack que sobe um socket-proxy contra o daemon Docker
do servidor real não é "arquivo que não governa o produto" — é o artefato de maior consequência
deste repositório. Isento, ele passaria a não ter fiscal declarado, e o laudo diria "partição
fechada" sobre um repositório onde ninguém vigia a porta.

O que empurrava para a isenção não era o `deploy/`; eram as **quatro regras de negócio** que o
descreviam.

## A decisão

**(a) `deploy/` ganha etapa própria: STAGE-DEPLOY**, com artefatos, lente de privacidade e cinco
fiscais resolvíveis — quatro símbolos de teste, verificados por AST, e um passo de workflow que
prova que eles *rodam*. Símbolo que existe e ninguém executa é fiscal de papel.

**(b) RULE-HOMOLOG-001..004 são aposentadas como regras de NEGÓCIO**, com o motivo escrito:
*elas nunca descreveram o cockpit; descreviam o plano de controle antigo* — `src/cockpit_harness/`,
que saiu deste repositório nesta mesma fatia. Uma regra de negócio de um repositório consumidor
deve dizer o que o **alvo** faz; estas diziam o que a ferramenta de auditoria exigia do ambiente
onde ela mediria. É outra camada.

Aposentadoria **com migração**, não apagamento. O enunciado e a razão de cada uma estão preservados
abaixo, e a mordida de cada uma virou um fiscal declarado em STAGE-DEPLOY, um por invariante:

| Invariante (era) | O que ela promete | Fiscal que a sucede (`tests/integration/test_homologacao.py`) |
|---|---|---|
| RULE-HOMOLOG-001 | Homologação não age sobre a **infraestrutura** | `test_socket_proxy_nega_escrita_no_daemon` |
| RULE-HOMOLOG-002 | Homologação não **colide** com produção | `test_container_nao_colide_com_producao` |
| RULE-HOMOLOG-003 | Homologação não **reusa a credencial** de produção | `test_script_recusa_credencial_identica_a_de_producao` |
| RULE-HOMOLOG-004 | Produção nunca é **publicada** pelo caminho de homologação | `test_script_de_ingress_recusa_o_host_de_producao` |

A tabela lista o fiscal *representativo* de cada invariante — aquele cuja remoção seria a perda
real. Os outros ~20 casos do arquivo continuam existindo e cobrindo as bordas; o que STAGE-DEPLOY
declara é a âncora que não pode sumir sem o fiscal deixar de resolver.

**(c) CAP-ALVO aposenta junto**, pelo mesmo motivo: ela chamava-se "Auditoria do Docker Cockpit
publicado" e descrevia o software que auditaria o cockpit, não o cockpit. **O sucessor da história
dela é a CP-001** — a campanha de homologação do Trabalho A, que continua aberta. A bancada existe
para servir aquela campanha: é o ambiente que a régua terá permissão de medir quando ela for
reaberta. Os quatro requisitos que pendiam de CAP-ALVO (REQ-005, REQ-006, REQ-007, REQ-009) não
foram cumpridos nem cancelados — são aquela CP, e voltam como requisitos do alvo quando ela
reabrir sobre STAGE-DEPLOY.

**(d) Recusada** a alternativa de declarar `deploy/` como `code_roots` do repositório, e o motivo
é dela mesma: `code_roots` descreve **o alvo** (`workspace/target/app/`). Apontá-lo para `deploy/`
faria os fiscais de cobertura medirem a bancada como se fosse o produto auditado.

## As quatro invariantes, preservadas

### 1. Homologação não age sobre a INFRAESTRUTURA

O stack fixa `ENABLE_ACTIONS="0"` — as rotas que tocam o daemon não são registradas: **404, não
403** — e o socket-proxy nega `POST`/`DELETE`. Duas trancas em camadas diferentes: a de dentro é da
aplicação, a de fora é do daemon. Uma tranca que o vigiado desliga sozinho não é uma tranca.

**Onde a regra para, e por que parar aí é o certo.** Ela chamava-se "não tem superfície de escrita",
e isso era FALSO — descoberto ao medir o alvo, não ao ler o compose. `POST /api/findings/{id}/ack`
e `POST /api/tasks` **não** passam por `ENABLE_ACTIONS`: existem em qualquer instalação e aceitam
escrita com um token de destravamento válido. O que elas escrevem é o estado do próprio painel
(reconhecer um achado, abrir um cartão), no banco de homologação, separado do de produção.

E devem continuar assim. `ENABLE_ACTIONS` responde "esta instância pode agir sobre a
infraestrutura?", não "esta instância aceita qualquer escrita". Triagem é leitura qualificada: um
observador que não pode reconhecer um achado não consegue exercitar o fluxo que homologação existe
para exercitar. Gatear `ack`/`tasks` tornaria homologação incapaz de testar justamente o caminho
que ela deveria validar.

### 2. Homologação não colide com produção

Nomes de container, nome de projeto e volume de dados são próprios; toda montagem de host é
somente-leitura. `compose up` com o nome de container de produção derruba o cockpit de verdade, e
`down -v` com o volume compartilhado apaga 30 dias de série histórica.

### 3. Homologação não reusa a credencial de produção

O basic auth do ingress de homologação usa um `.htpasswd` separado; o `.env` real nunca é comitado
e o `.example` carrega apenas placeholders. Credenciais iguais fazem o ambiente de teste virar uma
porta alternativa para o mesmo servidor: quem obtém a senha "de teste" entra na produção.

### 4. Produção nunca é publicada pelo caminho de homologação

O script de ingress recusa `docker.danzeroum.com` e só escreve blocos apontando para o upstream
`docker-cockpit-homolog:8000`. Rodá-lo com o host de produção publicaria `docker.danzeroum.com`
servindo o stack de teste, com TLS válido — o pior tipo de erro, porque parece que funcionou.

## Consequências

- A partição do repositório fecha sobre `deploy/` **com** fiscal, e não por isenção.
- `business/rules/` fica vazio. Não é lacuna: as regras que existiam descreviam software que saiu,
  e o alvo ainda não teve as suas autoradas — isso é outra fatia. Regra inventada agora seria
  afirmação sem leitura.
- Renomear qualquer um dos quatro testes referenciados **quebra o fiscal da etapa**, que é o
  comportamento desejado: o nome vira contrato.
- A prosa das quatro invariantes vive aqui e não na declaração da etapa porque o schema de
  `stages.yaml` é `additionalProperties: false` e não tem campo de justificativa. Registrado como
  lacuna do molde, irmã da CONF-007 — não contornada com campo inventado local.

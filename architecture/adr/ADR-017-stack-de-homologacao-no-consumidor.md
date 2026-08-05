# ADR-017 — O stack de homologação mora no consumidor; o produto continua upstream

- **Status:** accepted
- **Data:** 2026-08-03
- **Substitui:** ADR-015
- **Capacidades relacionadas:** CAP-ALVO
- **Riscos relacionados:** RISK-ALVO-001, RISK-HOMOLOG-001

## Contexto

A ADR-015 decidiu que nada do Docker Cockpit entraria neste repositório: nem o código, nem o
deploy. O raciocínio continua válido para o **código** — uma cópia do produto envelheceria em
silêncio, e o laudo mediria uma versão que já não é a publicada.

Mas ela tratou "código" e "como se sobe o ambiente que a régua audita" como a mesma coisa, e
não são. O stack de homologação não é o produto: é a **bancada de teste** que este repositório
precisa para existir. Quem quiser entender por que a auditoria mede o que mede tem de olhar,
no mesmo lugar, três coisas — a régua declarada, o alvo autorizado e o ambiente onde esse alvo
roda. Espalhá-las em dois repositórios torna a revisão de um PR de qualidade um exercício de
abrir abas.

O dono do projeto pediu explicitamente para ver a harness e o ambiente juntos.

## Decisão

`deploy/homologacao/` mora **neste** repositório: `compose.yml`, `.env.example` e o script de
ingress do host de homologação. O que **não** muda de ADR-015:

- o **código-fonte** do cockpit continua em `danzeroum/docker` e não é vendorizado — o compose
  constrói a partir do clone que já existe no servidor (`COCKPIT_SRC`);
- o stack de **produção** continua sendo assunto do repositório do produto. Este repositório
  não define, não altera e não sobe produção.

E o que a mudança obriga: um compose de ambiente de teste é onde as travas afrouxam sem que
ninguém repare. Por isso ele nasce com fiscal — `tests/integration/test_homologacao.py` reprova
colisão de nome com produção, `ENABLE_ACTIONS` diferente de `0`, `POST`/`DELETE` liberados no
socket-proxy, montagem de host sem `:ro`, credencial de verdade no `.example` e retenção longa.

## Consequências

- Um PR de qualidade passa a ser revisável num lugar só: régua, alvo, autorização e bancada.
- Homologação nasce mais travada que produção — sem superfície de escrita, e com o daemon
  negando escrita na origem. Produção fixa `ENABLE_ACTIONS: "1"` deliberadamente; aqui o pin é
  o oposto, também deliberado.
- **Custo real:** o deploy do cockpit agora tem dois lugares. Quando o compose de produção
  mudar (nova variável, novo volume, novo mount), o de homologação não muda junto, e a bancada
  vai divergir do alvo em silêncio. Nada neste repositório detecta isso — é a fraqueza desta
  decisão, e ela é o preço de ver tudo junto. Mitigação disponível se incomodar: um teste que
  baixe o compose de produção no commit declarado e compare as chaves.
- O isolamento é de container, volume e permissão de daemon — **não de rede**: os dois stacks
  compartilham `btv-prod-net`, porque é por ela que o global-ingress alcança os upstreams.

## Fiscal

`tests/integration/test_homologacao.py` (todas as travas acima);
`deploy/homologacao/setup-ingress-homolog.sh` (recusa o host de produção, exige `.htpasswd`
separado e o upstream de homologação); `.gitignore` (o `.env` real nunca é comitado).

# Parecer de proporcionalidade — Docker Cockpit sob a harness

> Leitura humana de `governance/privacy-review.yaml`, que é a fonte tipada. O alvo é
> `danzeroum/docker` no SHA `d6ae70eafee925e70f768f9c303229eb5673b6ba`, materializado em
> `workspace/target/`. Este parecer é **leitura de código**, não medição de comportamento —
> nenhuma requisição foi emitida contra o cockpit publicado.

## PAPEL DO SISTEMA

O cockpit **não coleta dado pessoal**. Não há cadastro, perfil, formulário ou base de titulares. O
objeto observado é infraestrutura: containers, imagens, redes, volumes e eventos de um daemon
Docker, lidos através de um socket-proxy (`workspace/target/docker-compose.yml`).

A única identidade que ele manipula é operacional: o usuário do basic auth do ingress, atrelado a
um token de sessão aleatório guardado **só como hash**, com prazo de 30 minutos
(`workspace/target/app/auth.py`). Isso é credencial de operador, não dado de titular.

Papel declarado: **`incidental`**. Não `none`, porque a exposição existe; não `operator`, porque o
cockpit não trata dado de ninguém por conta de terceiro — ele exibe o que outro processo escreveu.

## DADOS INCIDENTAIS

Um ponto, e ele é estrutural em vez de configurável:

`GET /api/containers/{id}/logs?tail=500`
(`workspace/target/app/routers/containers.py:96`) devolve a **saída bruta** de qualquer container
do host. Log de aplicação de terceiro é onde dado pessoal aparece por acidente — e-mail em stack
trace, IP em log de acesso, token em URL de query. Nada disso foi coletado por ninguém, e nenhum
ajuste do cockpit o elimina: quem escreve é a aplicação observada.

Por isso `fields: []` em `governance/data-inventory.yaml`. Inventariar um campo aqui exigiria
nomeá-lo, dar-lhe finalidade, base legal e `owning_component` — e o dado incidental não tem nome,
não tem finalidade e não pertence a componente nenhum. Um campo inventado dispararia três travas do
molde sobre uma ficção.

## CONTROLES PROPORCIONAIS

| Controle | O que já existe | Onde |
|---|---|---|
| Autorização de mutação | token de sessão aleatório, só hash, 30 min, atrelado ao usuário do ingress | `app/auth.py` |
| Gateway confiável | `TRUSTED_GATEWAY_CIDR` ausente ⇒ `/session/unlock` responde 403, **fail-closed** | `docker-compose.yml` |
| Mascaramento | por nome de chave, mais credencial embutida em URI | `app/masking.py` |
| Limite de janela | `tail` default 500 linhas | `app/routers/containers.py:96` |
| Isolamento do daemon | socket-proxy com allowlist de recursos, `mem_limit 64m`, `pids_limit 64` | `docker-compose.yml` |

São proporcionais ao papel `incidental`: reduzem quem alcança e quanto se vê, sem exigir do cockpit
um regime de tratamento que ele não pratica.

## CONTROLES DESCARTADOS

**Redação automática de PII nos logs.** Descartada, e a razão é a mesma que torna o dado
incidental: o cockpit não sabe o formato do que a aplicação alheia escreve. Um redator genérico
produziria dois danos — falso negativo (o dado passa, e agora com aparência de ter sido filtrado) e
falso positivo (o operador perde a linha de log que precisava para diagnosticar). Trocar
diagnóstico por uma garantia que não se sustenta piora as duas coisas.

**Encarregado (Art. 41) e os quatro endpoints do Art. 18.** Descartados **enquanto** o papel for
`incidental`. Não é dispensa: é a consequência de `fields: []`. Exigi-los agora seria declarar
capacidade de atender direito sobre dado que este sistema não sabe localizar.

**Ampliar a máscara de `masking.py` por lista de termos.** Não descartada — registrada como
`RISCO-002` (P2), consumida por `RISK-SEGREDO-001`. Acrescentar `authorization`, `pwd`, `jwt` e
`cookie` é barato; o que não é barato é a ilusão de completude que uma lista maior produz. O
tratamento certo é a lista **mais** o registro de que ela é incompleta por construção.

## O gatilho

Se a varredura encontrar dado pessoal **sistemático** — não incidental — nos logs expostos,
`lgpd_relevance` sobe de `incidental` para `operator` por change-proposal, e o data-inventory ganha
campos. Um e-mail num stack trace é incidente; um pipeline que despeja registros de titulares no
stdout de um container observado é tratamento, e aí o papel mudou de fato.

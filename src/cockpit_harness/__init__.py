"""Harness de adoção do Docker Cockpit sob a WebQA Suite.

Este pacote é o software DESTE repositório — o plano de controle da adoção. Ele não
reimplementa a régua: não há checks, não há lista curada, não há motor de auditoria aqui.
O que existe é o que a adoção precisa provar sobre si mesma:

- ``contrato``     — o consumidor está conforme WEBQA_CONSUMER_CONTRACT.md (pin, espelho, fronteira).
- ``plano``        — quem pode disparar qual modo, lido de harness/harness.yaml (nunca inferido).
- ``procedencia``  — o laudo carimba a régua que o produziu, e dois laudos só se comparam se a régua for a mesma.
- ``escopo_regua`` — traduz o escopo do contrato para o schema que a régua lê (mesmo nome, formatos incompatíveis).
- ``veredito``     — lê o laudo da fase C e emite o código de saída que a régua não emite.
- ``cli``          — a porta de linha de comando usada pelo CI e pelo agente.
"""

__all__ = ["codigos", "contrato", "plano", "procedencia", "escopo_regua", "veredito", "cli"]

"""Integração — o fiscal de metadados e o diagrama derivado, rodados de verdade.

Metadado sem fiscal é "markdown que não morde" (invariante 6). Rodar `validate_metadata.py` e
`generate_graph.py --check` dentro do inventário faz o repositório reprovar a si mesmo quando a
declaração e o código divergem, sem esperar o CI.
"""

from __future__ import annotations

import subprocess
import sys

import pytest
from pathlib import Path


def _rodar(raiz: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, *args],
        cwd=raiz, capture_output=True, text=True, timeout=180,
    )


@pytest.mark.skip(reason=(
    "APOSENTADO na CP-003 fatia-3, por decisão de danzeroum. Ele exigia `validate_metadata` sair "
    "0 — e o modelo de incubação da carcaça v1.0.0 PROMETE o vermelho que ele proíbe: um derivado "
    "nasce vermelho e /ingerir é o caminho até o verde (ADR-019 do molde). Um teste que proíbe o "
    "estado que o modelo promete não fiscaliza nada; ele só adia a leitura do CI.\n"
    "SUBSTITUÍDO PELA CATRACA, e não removido: ci/catraca.py garante o que este teste tentava "
    "garantir e não conseguia — que o vermelho ENCOLHE. Ela recusa subida de categoria e "
    "categoria nova, com baseline versionado e conferido contra a branch base. É estritamente "
    "mais forte: este teste era binário e cego ao tamanho da dívida.\n"
    "Fica como `skip` e não apagado, porque a aposentadoria é registro: quem vier depois precisa "
    "saber que a pergunta foi feita e por que a resposta mudou de instrumento."))
def test_metadados_coerentes_com_o_repositorio(raiz: Path):
    saida = _rodar(raiz, "ci/validate_metadata.py")
    assert saida.returncode == 0, saida.stdout + saida.stderr


def test_diagrama_derivado_em_dia(raiz: Path):
    saida = _rodar(raiz, "ci/generate_graph.py", "--check")
    assert saida.returncode == 0, saida.stdout + saida.stderr

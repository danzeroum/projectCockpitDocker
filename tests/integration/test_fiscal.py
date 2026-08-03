"""Integração — o fiscal de metadados e o diagrama derivado, rodados de verdade.

Metadado sem fiscal é "markdown que não morde" (invariante 6). Rodar `validate_metadata.py` e
`generate_graph.py --check` dentro do inventário faz o repositório reprovar a si mesmo quando a
declaração e o código divergem, sem esperar o CI.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def _rodar(raiz: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, *args],
        cwd=raiz, capture_output=True, text=True, timeout=180,
    )


def test_metadados_coerentes_com_o_repositorio(raiz: Path):
    saida = _rodar(raiz, "ci/validate_metadata.py")
    assert saida.returncode == 0, saida.stdout + saida.stderr


def test_diagrama_derivado_em_dia(raiz: Path):
    saida = _rodar(raiz, "ci/generate_graph.py", "--check")
    assert saida.returncode == 0, saida.stdout + saida.stderr

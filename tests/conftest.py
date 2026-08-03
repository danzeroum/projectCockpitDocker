"""Fixtures compartilhadas pelos quatro níveis de teste.

`RAIZ` é o repositório real (o que os testes de integração e aceitação inspecionam).
`repo_falso` fabrica um consumidor mínimo em tmp_path, para que os testes de unidade exercitem
os LIMITES (pin por faixa, espelho divergente, régua copiada, escopo expirado) sem depender do
estado do repositório de verdade.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session")
def raiz() -> Path:
    return RAIZ


@pytest.fixture
def repo_falso(tmp_path: Path):
    def _construir(
        *,
        pin: str = "webqa-suite==1.0.0",
        espelho: str = "1.0.0",
        base_url: str = "https://homologacao-nao-declarada.invalid",
        ambiente: str = "staging",
        escopo: str | None = None,
        copiar_regua: str | None = None,
    ) -> Path:
        (tmp_path / "requirements-qa.txt").write_text(f"# comentário\n{pin}\n", encoding="utf-8")
        qa = tmp_path / "tests" / "qa"
        qa.mkdir(parents=True)
        (qa / "config.yaml").write_text(
            textwrap.dedent(
                f"""
                standard_version: "{espelho}"
                target:
                  base_url: "{base_url}"
                  environment: {ambiente}
                thresholds:
                  max_high: 0
                  max_medium: 5
                active_gates: []
                """
            ).strip()
            + "\n",
            encoding="utf-8",
        )
        if escopo is not None:
            (qa / "escopo-autorizado.yaml").write_text(escopo, encoding="utf-8")
        if copiar_regua is not None:
            destino = tmp_path / copiar_regua
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text("# cópia proibida da régua\n", encoding="utf-8")
        return tmp_path

    return _construir


@pytest.fixture
def escopo_valido() -> str:
    """Escopo autorizado, vigente e com prova de posse — o caso feliz de §3."""
    return (
        textwrap.dedent(
            """
            authorized: true
            scope:
              hosts: ["homolog.exemplo.test"]
              paths_in_scope: ["/api/*"]
              paths_excluded: []
            proof_of_possession:
              method: dns-txt
              reference: "webqa-ownership=abc123"
            authorization_expires: "2999-12-31"
            """
        ).strip()
        + "\n"
    )

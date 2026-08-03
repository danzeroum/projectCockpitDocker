"""Procedência do laudo: qual régua produziu este número (contrato §5 e §7).

Sem procedência, um laudo é uma opinião com aparência de medida. Com ela, "não comparável" vira
um resultado possível — e muito melhor que um painel aparentemente preciso e enganoso.

Duas coisas moram aqui:

- montar e validar o envelope do laudo contra ``harness/schemas/report.schema.json``;
- decidir se dois laudos são comparáveis, pela fingerprint (nome, versão, commit, hash da lista
  curada, versão do schema). Divergiu em qualquer campo ⇒ ``not_comparable``.

A versão da régua NÃO é declarada neste módulo: ela é lida de ``requirements-qa.txt`` pelo
chamador (fonte única). O que este módulo carimba é o que foi observado no run.
"""

from __future__ import annotations

import datetime as _dt
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

from cockpit_harness.codigos import NaoComparavel, ProcedenciaInvalida

SCHEMA_LAUDO = "1.0"
NAO_INSTALADA = "UNINSTALLED"

RESULTADOS = ("ok", "findings", "suite_not_installed", "error")
MODOS = ("inventory", "passive", "load", "active_discovery")
RUNNERS = ("agent", "human", "ci")


def hash_lista_curada(caminho: Path) -> str:
    """SHA-256 da lista curada da suíte, no formato ``sha256:<hex>``.

    Carimba-se o HASH, nunca a lista: dois laudos com a mesma versão do padrão e hashes
    diferentes provam que alguém editou a régua — e o hash não traz a lista para dentro do
    consumidor (invariante 1).
    """
    if not caminho.exists():
        raise ProcedenciaInvalida(f"lista curada inexistente: {caminho}")
    digest = hashlib.sha256(caminho.read_bytes()).hexdigest()
    return f"sha256:{digest}"


@dataclass(frozen=True)
class Regua:
    """A régua que produziu o laudo."""

    name: str
    version: str
    commit: str
    sensitive_paths_hash: str

    @classmethod
    def ausente(cls, name: str = "webqa-suite") -> "Regua":
        """Régua não instalada — degradação tolerante (result ``suite_not_installed``, código 20)."""
        return cls(name=name, version=NAO_INSTALADA, commit=NAO_INSTALADA,
                   sensitive_paths_hash=NAO_INSTALADA)

    def como_dict(self) -> dict:
        return {
            "name": self.name,
            "version": self.version,
            "commit": self.commit,
            "sensitive_paths_hash": self.sensitive_paths_hash,
        }


def novo_run_id(momento: _dt.datetime | None = None) -> str:
    """``2026-08-03T13-34-00Z`` — cruza laudo, logs e decisão do agente."""
    momento = momento or _dt.datetime.now(_dt.timezone.utc)
    return momento.astimezone(_dt.timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")


def montar_laudo(
    *,
    regua: Regua,
    repositorio: str,
    commit: str,
    run_id: str,
    modo: str,
    runner_kind: str,
    rede_usada: bool,
    gates_ativos: tuple[str, ...] = (),
    resultado: str = "ok",
    achados: tuple[dict, ...] = (),
    resumo: dict | None = None,
) -> dict:
    """Monta o envelope do laudo (contrato §5). Não decide nada: apenas carimba o observado."""
    if modo not in MODOS:
        raise ProcedenciaInvalida(f"modo desconhecido: {modo!r}")
    if runner_kind not in RUNNERS:
        raise ProcedenciaInvalida(f"runner_kind desconhecido: {runner_kind!r}")
    if resultado not in RESULTADOS:
        raise ProcedenciaInvalida(f"result desconhecido: {resultado!r}")
    if resultado == "findings" and not achados:
        raise ProcedenciaInvalida("result 'findings' sem achados")
    if resultado != "findings" and achados:
        raise ProcedenciaInvalida("achados presentes com result diferente de 'findings'")

    laudo: dict = {
        "schema_version": SCHEMA_LAUDO,
        "standard": regua.como_dict(),
        "consumer_project": {"repository": repositorio, "commit": commit},
        "execution": {
            "run_id": run_id,
            "mode": modo,
            "network_used": rede_usada,
            "active_gates": list(gates_ativos),
            "runner_kind": runner_kind,
        },
        "result": resultado,
        "findings": list(achados),
    }
    if resumo is not None:
        laudo["summary"] = resumo
    return laudo


def _validador(schemas: Path):
    from jsonschema import Draft202012Validator  # import tardio: jsonschema é dependência de dev
    from referencing import Registry, Resource

    report = json.loads((schemas / "report.schema.json").read_text(encoding="utf-8"))
    provenance = json.loads((schemas / "provenance.schema.json").read_text(encoding="utf-8"))
    registro = Registry().with_resources(
        [
            (provenance["$id"], Resource.from_contents(provenance)),
            (report["$id"], Resource.from_contents(report)),
        ]
    )
    return Draft202012Validator(report, registry=registro)


def validar(laudo: dict, schemas: Path) -> None:
    """Valida o laudo contra report+provenance. Laudo sem procedência válida é erro 30."""
    erros = sorted(_validador(schemas).iter_errors(laudo), key=lambda e: list(e.path))
    if erros:
        detalhes = "; ".join(
            f"{'/'.join(str(p) for p in e.path) or '(raiz)'}: {e.message}" for e in erros
        )
        raise ProcedenciaInvalida(detalhes)


def fingerprint(laudo: dict) -> tuple[str, str, str, str, str]:
    """(name, version, commit, sensitive_paths_hash, schema_version) — contrato §7."""
    padrao = laudo.get("standard") or {}
    faltando = [c for c in ("name", "version", "commit", "sensitive_paths_hash") if not padrao.get(c)]
    if faltando or not laudo.get("schema_version"):
        raise ProcedenciaInvalida("bloco de procedência incompleto: " + ", ".join(faltando or ["schema_version"]))
    return (
        padrao["name"],
        padrao["version"],
        padrao["commit"],
        padrao["sensitive_paths_hash"],
        laudo["schema_version"],
    )


def comparaveis(a: dict, b: dict) -> bool:
    """Dois laudos só se comparam se a régua for exatamente a mesma."""
    return fingerprint(a) == fingerprint(b)


def exigir_comparaveis(a: dict, b: dict) -> None:
    """Porta da agregação. Recusa com NaoComparavel (31) em vez de somar maçã com laranja."""
    if not comparaveis(a, b):
        raise NaoComparavel(f"réguas incompatíveis: {fingerprint(a)} != {fingerprint(b)}")

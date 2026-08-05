#!/usr/bin/env python3
"""A catraca da ingestão: o contador de achados só desce.

POR QUE ISTO EXISTE. Este repositório acabou de virar `derived` e nasceu VERMELHO de propósito —
274 achados, dos quais 209 são o mapa de componentes e testes de um sistema real que ainda não foi
autorado. A doutrina do molde diz que isso é correto (`/ingerir` é o caminho do vermelho ao verde,
e o ADR-019 chama o vermelho de mapa). O que a doutrina NÃO dá é a garantia de que o mapa encolhe.

Sem catraca, "vermelho declarado" e "vermelho esquecido" são o mesmo estado observável. Pior:
qualquer PR pode acrescentar um órfão novo e ninguém nota, porque o CI já estava vermelho — o
número sobe dentro de um vermelho que ninguém lê. É o modo de falha exato que um repositório em
incubação tem, e ele dura anos.

O QUE ELA GARANTE, e o que deliberadamente não garante:

  garante ....... nenhuma CATEGORIA nova aparece; nenhuma categoria SOBE de contagem
  não garante ... que cada PR desça alguma coisa. Exigir descida por PR faria alguém apagar uma
                  declaração para "pagar o pedágio", que é o oposto do que se quer.

A COMPARAÇÃO É POR IGUALDADE, não por teto. Um teto ("current <= baseline") deixaria o baseline
alto para sempre: o primeiro PR desce 40, ninguém regrava, e o PR seguinte pode subir 40 de volta
sem que a catraca gire. Exigir igualdade força quem desce a REGRAVAR — e é o diff do baseline, no
PR, que torna a descida visível a quem revisa. A catraca gira porque alguém a gira, e o registro
de que girou é o arquivo versionado.

DUAS PERGUNTAS DISTINTAS, e a segunda é a que fecha o buraco:

  1. o baseline gravado descreve o repositório de agora?   -> --verificar (padrão)
  2. o baseline gravado é menor ou igual ao da base?        -> --anterior <arquivo>

A (1) sozinha seria burlável: bastaria regravar o baseline para cima junto com a regressão, e o
arquivo passaria a descrever fielmente um repositório pior. A (2) é o que impede isso, e por isso
o workflow busca o baseline da branch base em vez de confiar no que veio no PR.

Uso:  python ci/catraca.py [--gravar] [--anterior <arquivo>] [--json]
Saída: 0 a catraca segurou · 1 subiu / categoria nova / baseline desatualizado · 2 não consegui medir.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import harness_lib as hl

BASELINE = "harness/state/baseline-achados.json"

# `[categoria] mensagem` — a forma que ci/validate_metadata.py::err usa em todos os achados.
_CATEGORIA = re.compile(r"^\s*\[([^\]]+)\]")


@dataclass(frozen=True)
class Veredito:
    """`segurou` é a resposta; as três listas são o que se diz a quem lê o PR."""

    segurou: bool
    subiram: tuple[tuple[str, int, int], ...] = ()      # (categoria, antes, agora)
    novas: tuple[tuple[str, int], ...] = ()             # (categoria, agora)
    desceram: tuple[tuple[str, int, int], ...] = ()     # (categoria, antes, agora)
    motivos: tuple[str, ...] = field(default=())


def comparar(*, atual: dict[str, int], baseline: dict[str, int]) -> Veredito:
    """Núcleo puro. Compara duas contagens por categoria e diz se a catraca segurou.

    Puro pelo motivo de sempre nesta casa: "o repositório piorou" e "não consegui medir o
    repositório" pedem reações opostas, e um comparador que também mede não consegue separá-las.
    """
    subiram, novas, desceram = [], [], []

    for cat, n in sorted(atual.items()):
        antes = baseline.get(cat)
        if antes is None:
            novas.append((cat, n))
        elif n > antes:
            subiram.append((cat, antes, n))
        elif n < antes:
            desceram.append((cat, antes, n))

    # Categoria que sumiu do atual e continua no baseline é DESCIDA até zero — o melhor caso, e
    # ainda assim exige regravar: um baseline que lista categoria inexistente descreve outro
    # repositório.
    for cat, antes in sorted(baseline.items()):
        if cat not in atual and antes > 0:
            desceram.append((cat, antes, 0))

    motivos = []
    if novas:
        motivos.append(
            "CATEGORIA NOVA: " + ", ".join(f"{c} ({n})" for c, n in novas) +
            " — achado de um tipo que não existia. A catraca recusa mesmo que o TOTAL tenha caído: "
            "trocar dez órfãos por dez regras quebradas mantém o número e muda o problema.")
    if subiram:
        motivos.append(
            "SUBIDA: " + ", ".join(f"{c} {a}→{n}" for c, a, n in subiram) +
            " — a catraca não gira para trás. O repositório está em incubação e vermelho; o que "
            "não pode é ficar mais vermelho sem ninguém notar dentro do vermelho que já havia.")
    if desceram and not (novas or subiram):
        motivos.append(
            "DESCEU (é o esperado): " + ", ".join(f"{c} {a}→{n}" for c, a, n in desceram) +
            f" — regrave com `python ci/catraca.py --gravar` e inclua {BASELINE} no PR. A catraca "
            f"gira porque alguém a gira; o diff do baseline é o registro de que girou.")

    return Veredito(segurou=not (novas or subiram or desceram),
                    subiram=tuple(subiram), novas=tuple(novas), desceram=tuple(desceram),
                    motivos=tuple(motivos))


def nao_regrediu(*, novo: dict[str, int], anterior: dict[str, int],
                 declaradas: dict[str, str] | None = None) -> list[str]:
    """O baseline do PR contra o da base. Sem isto, regravar para cima legalizaria a regressão.

    A CATEGORIA NOVA DECLARADA é a correção de um falso positivo que esta função produziu contra o
    PR que a estreou. `audit_lgpd` saía 2 ("não consegui fiscalizar") por falta do data-inventary;
    quando o arquivo nasceu, o fiscal passou a RODAR e suas categorias apareceram do nada. A
    catraca leu isso como regressão — e era progresso: um fiscal que começa a medir é exatamente o
    que se quer.

    Recusar sem escape teria ensinado a desligar a catraca no primeiro PR útil (princípio (e)).
    Aceitar em silêncio teria aberto o buraco que ela existe para fechar. A saída é a mesma que
    esta casa usa em toda parte — `env_hygiene.exceptions`, `scan.exclusions`, `stages:ungoverned`:
    **exceção DECLARADA, nunca regra removida.** A categoria nova entra se, e só se, o baseline do
    PR disser qual é e por quê; e a justificativa aparece no diff, onde alguém a contesta.

    Elevar uma categoria EXISTENTE continua sem escape. Não é assimetria: "este fiscal passou a
    medir" é uma afirmação verificável sobre o mundo, e "este número subiu" é a definição do que a
    catraca impede.
    """
    declaradas = declaradas or {}
    ruins = []
    for cat, n in sorted(novo.items()):
        antes = anterior.get(cat)
        if antes is None:
            if cat not in declaradas:
                ruins.append(
                    f"o baseline do PR inventa a categoria {cat!r} ({n}), ausente na base — se ela "
                    f"nasceu porque um fiscal passou a rodar, declare-a em "
                    f"`categorias_novas_declaradas` com o motivo; categoria que aparece sem "
                    f"explicação é indistinguível de dívida nova")
            elif len(declaradas[cat].strip()) < 40:
                ruins.append(f"a categoria nova {cat!r} está declarada com justificativa vazia ou "
                             f"curta demais — declaração sem motivo é a exceção virando carimbo")
        elif n > antes:
            ruins.append(f"o baseline do PR eleva {cat!r} de {antes} para {n} — regravar para cima "
                         f"é a única forma de a catraca girar para trás, e é por isso que ela é "
                         f"conferida contra a base e não contra si mesma")
    for cat in sorted(declaradas):
        if cat in anterior:
            ruins.append(f"{cat!r} está declarada como categoria nova e já existia na base — "
                         f"declaração morta faz a próxima parecer revisada")
        elif cat not in novo:
            ruins.append(f"{cat!r} está declarada como categoria nova e não aparece na medição")
    return ruins


# --------------------------------------------------------------------------------------
# Camada de I/O. Mede o repositório; nenhuma decisão mora aqui.
# --------------------------------------------------------------------------------------

def medir() -> dict[str, int]:
    """Contagem de achados por categoria, do repositório de agora.

    Duas fontes, porque os fiscais desta casa relatam de dois jeitos: `validate_metadata` acumula
    strings `[categoria] ...`, e os fiscais de laudo escrevem JSON com `origin`. Ler só uma delas
    faria a catraca segurar metade da porta.
    """
    import contextlib
    import importlib
    import io

    contagem: dict[str, int] = {}
    # Os fiscais imprimem seus 299 achados; a catraca não é o lugar de relê-los. Quem quer a lista
    # roda `ci/validate_all.py`, que existe exatamente para isso. Aqui só o veredito.
    silencio = contextlib.redirect_stdout(io.StringIO())

    import inventory_code
    inventory_code.reset_cache()
    import validate_metadata as vm
    importlib.reload(vm)
    with silencio:
        vm.main(["--quiet"])
    for msg in vm.errors:
        m = _CATEGORIA.match(msg)
        cat = f"meta:{m.group(1)}" if m else "meta:sem-categoria"
        contagem[cat] = contagem.get(cat, 0) + 1

    for modulo, laudo in (("audit_governance", "harness/reports/governance-audit.json"),
                          ("audit_lgpd", "harness/reports/lgpd-audit.json"),
                          ("audit_ledger", "harness/reports/ledger-audit.json")):
        mod = importlib.import_module(modulo)
        importlib.reload(mod)
        # Um fiscal que sai 2 ("não consegui fiscalizar") não escreve laudo, e suas categorias
        # ficam AUSENTES em vez de zeradas. É deliberado: zerar seria afirmar "medi e não achei
        # nada", que é a confusão que o princípio (h) existe para impedir. A consequência é
        # visível e correta — no dia em que ele voltar a rodar, as categorias dele nascem NOVAS,
        # a catraca recusa, e alguém regrava sabendo o que passou a ser medido.
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                mod.main(["--quiet"])
        except SystemExit:
            pass
        if not hl.rel_exists(laudo):
            continue
        for f in (hl.read_json(laudo) or {}).get("findings", []):
            if f.get("severity") == "info":
                continue          # `info` descreve estado declarado; contá-lo faria a catraca
                                  # travar em cima de decisão registrada, não de dívida
            cat = f"{modulo.replace('audit_', '')}:{f.get('origin', 'sem-origem')}"
            contagem[cat] = contagem.get(cat, 0) + 1

    return contagem


def _ler(caminho: str | Path) -> dict[str, int]:
    doc = json.loads(Path(caminho).read_text(encoding="utf-8"))
    return {k: int(v) for k, v in (doc.get("por_categoria") or {}).items()}


def _declaradas(caminho: str | Path) -> dict[str, str]:
    doc = json.loads(Path(caminho).read_text(encoding="utf-8"))
    return {d["categoria"]: d.get("justificativa", "")
            for d in (doc.get("categorias_novas_declaradas") or [])}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="A catraca da ingestão: o contador só desce.")
    p.add_argument("--gravar", action="store_true", help="regrava o baseline com o estado de agora")
    p.add_argument("--anterior", help="baseline da branch base, para conferir que não subiu")
    p.add_argument("--json", action="store_true")
    args = p.parse_args(argv)

    try:
        atual = medir()
    except Exception as exc:  # noqa: BLE001 - não conseguir medir é 2, nunca 0
        print(f"✗ catraca: não foi possível medir ({exc}).", file=sys.stderr)
        return 2

    destino = hl.REPO / BASELINE
    total = sum(atual.values())

    if args.gravar:
        destino.parent.mkdir(parents=True, exist_ok=True)
        # As declarações sobrevivem ao regravar. Elas são texto humano sobre POR QUE uma categoria
        # nasceu; recalcular contagens não é motivo para apagá-lo.
        anteriores = (json.loads(destino.read_text(encoding="utf-8")).get(
            "categorias_novas_declaradas") or []) if destino.exists() else []
        destino.write_text(json.dumps({
            "schema_version": "1.0",
            "comentario": "Contagem de achados por categoria. Baseline da catraca (ci/catraca.py): "
                          "este repositório está em incubação e vermelho de propósito; o que a "
                          "catraca garante é que o vermelho não cresce. Regravar para CIMA é "
                          "recusado pelo workflow, que compara este arquivo com o da branch base.",
            "total": total,
            "por_categoria": dict(sorted(atual.items())),
            "categorias_novas_declaradas": anteriores,
        }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"✓ catraca: baseline gravado — {total} achado(s) em {len(atual)} categoria(s).")
        return 0

    if not destino.exists():
        print(f"✗ catraca: {BASELINE} não existe. Grave o baseline inicial com "
              f"`python ci/catraca.py --gravar` — sem ele não há catraca, só vermelho.",
              file=sys.stderr)
        return 1

    baseline = _ler(destino)
    v = comparar(atual=atual, baseline=baseline)

    if args.anterior:
        ruins = nao_regrediu(novo=baseline, anterior=_ler(args.anterior),
                             declaradas=_declaradas(destino))
        for r in ruins:
            print(f"✗ catraca: {r}", file=sys.stderr)
        if ruins:
            return 1

    if args.json:
        print(json.dumps({"total": total, "por_categoria": dict(sorted(atual.items())),
                          "segurou": v.segurou, "motivos": list(v.motivos)},
                         indent=2, ensure_ascii=False))
    elif v.segurou:
        print(f"✓ catraca: {total} achado(s), igual ao baseline. Nada subiu, nada é novo.")
    else:
        print(f"✗ catraca: o baseline diz {sum(baseline.values())} e o repositório tem {total}.",
              file=sys.stderr)
        for m in v.motivos:
            print(f"  - {m}", file=sys.stderr)

    return 0 if v.segurou else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

"""Porta de linha de comando da harness — usada pelo CI e pelo agente.

Regra da CLI (contrato §6): sai com código estável, nunca com traceback. Falha de configuração
é evento operacional auditável, não crash.

    python -m cockpit_harness checar              # verificação sem rede do consumidor
    python -m cockpit_harness pendencias          # imprime INCOMPLETE:* (uma por linha)
    python -m cockpit_harness modo --modo passive --runner agent
    python -m cockpit_harness escopo-regua --saida $RUNNER_TEMP/escopo.yaml
    python -m cockpit_harness veredito --laudo harness/reports/sondagem.json
    python -m cockpit_harness laudo --modo inventory --runner ci --saida docs/laudo-adocao.json
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

from cockpit_harness import contrato, plano, procedencia
from cockpit_harness.codigos import Codigo, ErroHarness

RAIZ_PADRAO = Path(__file__).resolve().parents[2]
REPOSITORIO = "danzeroum/projectCockpitDocker"


def _git(diretorio: Path, *args: str) -> str:
    try:
        saida = subprocess.run(
            ["git", "-C", str(diretorio), *args],
            capture_output=True, text=True, check=True, timeout=30,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return saida.stdout.strip()


def _regua_observada(args: argparse.Namespace, versao: str) -> tuple[procedencia.Regua, str]:
    """Descobre commit e hash da lista curada. Sem observação, a régua é declarada AUSENTE.

    Inventar commit/hash seria pior que admitir a ausência: a fingerprint existe justamente para
    que dois laudos não se comparem quando a régua não é comprovadamente a mesma.
    """
    if args.commit_regua and args.hash_lista:
        return procedencia.Regua("webqa-suite", versao, args.commit_regua, args.hash_lista), "ok"
    if args.regua:
        clone = Path(args.regua).resolve()
        commit = _git(clone, "rev-parse", "HEAD")
        lista = clone / "webqa-suite" / "data" / "caminhos-sensiveis.yaml"
        if commit and lista.exists():
            return (
                procedencia.Regua("webqa-suite", versao, commit, procedencia.hash_lista_curada(lista)),
                "ok",
            )
    return procedencia.Regua.ausente(), "suite_not_installed"


def cmd_checar(args: argparse.Namespace) -> int:
    raiz = args.raiz
    atual = contrato.situacao(raiz)
    print(f"padrão declarado ....... webqa-suite=={atual.versao} (fonte única: requirements-qa.txt)")
    print(f"espelho config.yaml .... {atual.versao} (casa com o pin)")
    print(f"fronteira da régua ..... intacta (webqa/, checks/, data/caminhos-sensiveis.yaml ausentes)")
    print(f"alvo declarado ......... {atual.alvo or '— (placeholder)'} [{atual.ambiente}]")
    print(f"escopo autorizado ...... {'sim' if atual.escopo and atual.escopo.autorizado else 'não'}")
    if atual.pendencias:
        print("pendências ............. " + ", ".join(atual.pendencias))
        print("modos de rede .......... RECUSADOS (fail-closed)")
    else:
        print("modos de rede .......... liberados para passive")
    return int(Codigo.OK)


def cmd_versao(args: argparse.Namespace) -> int:
    """Imprime a versão da régua lida da FONTE ÚNICA — para o CI não restatar o número no YAML."""
    print(contrato.conferir_fonte_unica(args.raiz))
    return int(Codigo.OK)


def cmd_alvo(args: argparse.Namespace) -> int:
    """Imprime a base_url do alvo. Sem alvo declarado, não imprime nada e sai 12."""
    atual = contrato.exigir_rede_liberada(args.raiz)
    print(atual.alvo)
    return int(Codigo.OK)


def cmd_pendencias(args: argparse.Namespace) -> int:
    atual = contrato.situacao(args.raiz)
    for pendencia in atual.pendencias:
        print(pendencia)
    if atual.pendencias and args.exigir:
        return int(Codigo.SCOPE_MISSING)
    return int(Codigo.OK)


def cmd_modo(args: argparse.Namespace) -> int:
    controle = plano.carregar(args.raiz)
    plano.exigir_ambiente_limpo(controle, dict(os.environ))
    plano.exigir_permissao(controle, args.modo, args.runner)
    if (plano.modos(controle).get(args.modo) or {}).get("network"):
        contrato.exigir_rede_liberada(args.raiz)
    print(f"modo {args.modo!r} autorizado para runner-kind {args.runner!r}")
    return int(Codigo.OK)


def cmd_escopo_regua(args: argparse.Namespace) -> int:
    """Traduz o escopo do contrato (§3) para o formato que a régua lê. Sai 12 se faltar.

    Existe porque os dois arquivos se chamam `escopo-autorizado.yaml` e têm schemas
    incompatíveis — o CI copiava um no lugar do outro, e `webqa.escopo.carregar`
    recusaria com "escopo sem alvos declarados".
    """
    from cockpit_harness import escopo_regua

    atual = contrato.exigir_rede_liberada(args.raiz)
    destino = escopo_regua.escrever(atual, Path(args.saida))
    print(f"✓ escopo traduzido para a régua em {destino}")
    return int(Codigo.OK)


def cmd_veredito(args: argparse.Namespace) -> int:
    """Veredito sobre o laudo da sondagem. 22 = não medido; 23 = medido e reprovou.

    A régua sai 0 mesmo com o laudo dizendo `inconclusivo: true` — este comando é
    quem impede que "não medi" chegue ao CI como "está limpo".
    """
    from cockpit_harness import veredito

    print(veredito.avaliar(Path(args.laudo), args.raiz))
    return int(Codigo.OK)


def cmd_laudo(args: argparse.Namespace) -> int:
    raiz = args.raiz
    versao = contrato.conferir_fonte_unica(raiz)
    regua, resultado = _regua_observada(args, versao)

    controle = plano.carregar(raiz)
    plano.exigir_permissao(controle, args.modo, args.runner)
    rede = bool((plano.modos(controle).get(args.modo) or {}).get("network"))
    if rede:
        contrato.exigir_rede_liberada(raiz)

    laudo = procedencia.montar_laudo(
        regua=regua,
        repositorio=REPOSITORIO,
        commit=_git(raiz, "rev-parse", "HEAD") or "unknown",
        run_id=args.run_id or procedencia.novo_run_id(),
        modo=args.modo,
        runner_kind=args.runner,
        rede_usada=rede,
        resultado=resultado,
        resumo={"pendencias": list(contrato.situacao(raiz).pendencias)},
    )
    procedencia.validar(laudo, raiz / "harness" / "schemas")

    texto = json.dumps(laudo, indent=2, ensure_ascii=False) + "\n"
    if args.saida:
        destino = Path(args.saida)
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(texto, encoding="utf-8")
        print(f"✓ laudo escrito em {destino}")
    else:
        print(texto, end="")
    return int(Codigo.OK)


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="cockpit-harness", description=__doc__)
    parser.add_argument("--raiz", type=Path, default=RAIZ_PADRAO, help="raiz do repositório consumidor")
    subs = parser.add_subparsers(dest="comando", required=True)

    subs.add_parser("checar", help="verificação sem rede do consumidor").set_defaults(func=cmd_checar)
    subs.add_parser("versao", help="imprime a versão da régua (fonte única)").set_defaults(func=cmd_versao)
    subs.add_parser("alvo", help="imprime a base_url autorizada; sai 12 sem alvo").set_defaults(func=cmd_alvo)

    p_pend = subs.add_parser("pendencias", help="lista pendências INCOMPLETE:*")
    p_pend.add_argument("--exigir", action="store_true", help="sai 12 se houver pendência")
    p_pend.set_defaults(func=cmd_pendencias)

    p_modo = subs.add_parser("modo", help="pergunta ao plano se um runner pode disparar um modo")
    p_modo.add_argument("--modo", required=True)
    p_modo.add_argument("--runner", required=True)
    p_modo.set_defaults(func=cmd_modo)

    p_escopo = subs.add_parser("escopo-regua",
                               help="traduz o escopo do contrato para o formato da régua")
    p_escopo.add_argument("--saida", required=True, help="arquivo de destino (efêmero, no runner)")
    p_escopo.set_defaults(func=cmd_escopo_regua)

    p_ver = subs.add_parser("veredito",
                            help="veredito sobre o laudo da sondagem; 22 = não medido, 23 = reprovou")
    p_ver.add_argument("--laudo", required=True, help="laudo JSON produzido por webqa.sondagem")
    p_ver.set_defaults(func=cmd_veredito)

    p_laudo = subs.add_parser("laudo", help="emite o laudo com procedência carimbada")
    p_laudo.add_argument("--modo", default="inventory")
    p_laudo.add_argument("--runner", default="ci")
    p_laudo.add_argument("--regua", help="caminho de um clone de danzeroum/qa-suite (para commit+hash)")
    p_laudo.add_argument("--commit-regua", help="commit da régua, quando observado fora daqui")
    p_laudo.add_argument("--hash-lista", help="sha256:<hex> da lista curada")
    p_laudo.add_argument("--run-id", help="run_id explícito (default: agora, UTC)")
    p_laudo.add_argument("--saida", help="arquivo de destino (default: stdout)")
    p_laudo.set_defaults(func=cmd_laudo)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = construir_parser().parse_args(argv)
    try:
        return args.func(args)
    except ErroHarness as erro:
        print(f"✗ [{erro.codigo.name}] {erro}", file=sys.stderr)
        return int(erro.codigo)


if __name__ == "__main__":  # pragma: no cover - ponto de entrada
    sys.exit(main())

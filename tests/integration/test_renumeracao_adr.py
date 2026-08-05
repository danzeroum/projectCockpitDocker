"""Guarda da renumeração ADR-005/006/007 → 015/016/017 (CP-003 fatia-1b).

O PROBLEMA QUE ELA RESOLVEU. Este repositório tem SETE ADRs próprios; a carcaça v1.0.0 trouxe
`ci/`, `harness/policies/` e `.claude/commands/` cheios de referências aos ADRs **do molde**, que
são decisões inteiramente outras. Nos números 005, 006 e 007 os dois conjuntos colidiam: a mesma
string apontava para duas decisões diferentes conforme o arquivo em que se lia.

Renomear a população LOCAL é a resolução da colisão. Um `sed` cego teria corrompido as duas.

E O CRITÉRIO NÃO É O CAMINHO. Foi a leitura referência por referência que mostrou: dois arquivos
que MORAM em caminho local — `security/threat-model.yaml` e `governance/conformance-review.yaml` —
citavam "ADR-006" querendo dizer o do MOLDE. Eles não foram renumerados; foram DESAMBIGUADOS, e é
por isso que a asserção abaixo procura a palavra "MOLDE" neles.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent.parent

# A população do MOLDE. Estas referências significam as decisões do repositório-molde e não podem
# ter sido tocadas — se a renumeração as alcançasse, cada mensagem de fiscal passaria a apontar
# para a decisão errada deste repositório.
POP_MOLDE = ("ci/", "harness/policies/", ".claude/")

# Registro histórico: descreve o que era verdade quando foi escrito, e a CP-003 o declarou
# intocável. As referências antigas SOBREVIVEM aqui de propósito.
HISTORICO = {"docs/laudo-adocao.md", "docs/laudo-adocao.json", "docs/ADOCAO.md",
             "harness/change-proposals/CP-002-atualizar-a-carcaca.yaml"}

# Caminho local, significado do molde: desambiguados em vez de renumerados.
AMBIGUAS = {"security/threat-model.yaml", "governance/conformance-review.yaml"}

ANTIGO = re.compile(r"ADR-00[567]")


def _versionados() -> list[str]:
    return subprocess.run(["git", "-C", str(RAIZ), "ls-files"],
                          capture_output=True, text=True).stdout.split()


def test_populacao_do_MOLDE_nao_foi_tocada():
    """A metade da guarda que impede o dano: as referências do molde continuam existindo.

    Se este teste falhar com ZERO ocorrências, a renumeração passou por cima delas — e o pior é
    que o repositório ficaria verde, porque os números 015/016/017 também existem aqui agora.
    """
    achadas = [rel for rel in _versionados()
               if rel.startswith(POP_MOLDE) and Path(rel).suffix in (".py", ".md")
               and ANTIGO.search((RAIZ / rel).read_text(encoding="utf-8", errors="replace"))]
    assert achadas, (
        "nenhum arquivo de ci/, harness/policies/ ou .claude/ cita ADR-005/006/007 — a "
        "renumeração provavelmente atropelou a população do MOLDE, e os fiscais transplantados "
        "passaram a apontar para as decisões erradas deste repositório")


def test_refs_locais_antigas_so_sobrevivem_no_registro_historico():
    """A outra metade: fora do histórico e da população do molde, o número antigo não existe."""
    sobras = []
    for rel in _versionados():
        if rel.startswith(POP_MOLDE) or rel in HISTORICO or rel in AMBIGUAS:
            continue
        if Path(rel).suffix not in (".py", ".yaml", ".md", ".json"):
            continue
        if ANTIGO.search((RAIZ / rel).read_text(encoding="utf-8", errors="replace")):
            sobras.append(rel)
    assert not sobras, f"referência local antiga fora do registro histórico: {sobras}"


def test_as_ambiguas_dizem_QUAL_ADR_006():
    """Número nu, em repositório com dois namespaces de ADR, é ambiguidade que o próximo leitor
    resolve errado. Estas duas dizem 'do MOLDE' por extenso."""
    for rel in sorted(AMBIGUAS):
        texto = (RAIZ / rel).read_text(encoding="utf-8")
        for m in ANTIGO.finditer(texto):
            trecho = texto[m.start():m.start() + 120]
            assert "MOLDE" in trecho.upper(), f"{rel}: '{trecho[:60]}…' não diz de qual ADR-006 fala"


@pytest.mark.parametrize("novo", ["ADR-015", "ADR-016", "ADR-017"])
def test_os_novos_numeros_existem_como_arquivo_e_como_entrada(novo):
    import yaml
    idx = yaml.safe_load((RAIZ / "architecture/adr/index.yaml").read_text(encoding="utf-8"))
    entrada = next((a for a in idx["adrs"] if a["id"] == novo), None)
    assert entrada, f"{novo} não está no index"
    assert (RAIZ / entrada["file"]).exists(), f"{entrada['file']} não existe"
    assert (RAIZ / entrada["file"]).read_text(encoding="utf-8").startswith(f"# {novo}")


def test_MUTACAO_reverter_uma_referencia_local_e_detectada(tmp_path):
    """A borda que o aceite pede: se reverter UMA referência local ao número antigo passasse
    despercebido, a renumeração não teria guarda — teria acontecido.

    Mutação aplicada numa CÓPIA, e a cópia é o ponto: mutar a árvore de trabalho e confiar em
    restaurá-la depois é como um teste deixa o repositório pior do que encontrou.
    """
    import shutil
    copia = tmp_path / "repo"
    shutil.copytree(RAIZ, copia, ignore=shutil.ignore_patterns(
        ".git", "__pycache__", "workspace", "*.pyc", ".pytest_cache"))

    alvo = copia / "governance/risk-register.yaml"
    texto = alvo.read_text(encoding="utf-8")
    assert "ADR-016" in texto
    alvo.write_text(texto.replace("ADR-016", "ADR-006", 1), encoding="utf-8")

    sobras = [rel for rel in _versionados()
              if not rel.startswith(POP_MOLDE) and rel not in HISTORICO and rel not in AMBIGUAS
              and Path(rel).suffix in (".py", ".yaml", ".md", ".json")
              and (copia / rel).exists()
              and ANTIGO.search((copia / rel).read_text(encoding="utf-8", errors="replace"))]
    assert sobras == ["governance/risk-register.yaml"], sobras


def test_nenhuma_assercao_casa_com_a_PROPRIA_DECLARACAO_no_index():
    """A lição do ADR-028 do molde, em forma de teste.

    Lá, uma asserção `file_matches` cujo padrão continha o próprio texto da declaração passou a
    casar consigo mesma no `index.yaml`: ela ficava verde por existir, não por o repositório estar
    conforme. Aqui nenhuma asserção aponta para `index.yaml` — e se um dia apontar, este teste
    exige que o padrão NÃO case o arquivo que a declara.
    """
    import yaml
    idx_rel = "architecture/adr/index.yaml"
    bruto = (RAIZ / idx_rel).read_text(encoding="utf-8")
    idx = yaml.safe_load(bruto)
    for adr in idx["adrs"]:
        for a in adr.get("assertions") or []:
            if a.get("kind") not in ("file_matches", "file_lacks"):
                continue
            if idx_rel not in (a.get("files") or []):
                continue
            assert not re.search(a["pattern"], bruto, re.MULTILINE), (
                f"{a['id']} casa com o próprio index.yaml — ficaria verde por existir, "
                f"não por o repositório estar conforme")

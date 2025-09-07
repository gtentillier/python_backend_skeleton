import re
from pathlib import Path
from typing import Optional


def increment_headers_in_text(content: str, shift: int = 1) -> str:
    """
    Incrémente les numéros des en-têtes Markdown du type '# N' par `shift`.
    Retourne le contenu modifié.
    """
    matches = re.findall(r"^#+\s+(-?\d+)", content, flags=re.MULTILINE)
    if not matches:
        return content

    max_part = max(int(m) for m in matches)
    # On remplace du plus grand vers le plus petit pour éviter les collisions
    for part in range(max_part, -1, -1):
        content = re.sub(
            rf"^(#+)\s+{part}\b",
            lambda m,
            p=part: f"{m.group(1)} {p + shift}",
            content,
            flags=re.MULTILINE,
        )
    return content


def increment_headers(filename: Path, shift: int = 1, encoding: str = "utf-8") -> None:
    """
    Lit `filename`, incrémente les en-têtes et réécrit le fichier.
    Retourne le nouveau contenu pour usage éventuel.
    """
    if not filename.is_file():
        print(f"Erreur : {filename} n'est pas un fichier valide.")
        return
    if not filename.suffix == ".md":
        print(f"Erreur : {filename} n'est pas un fichier Markdown.")
        return

    content = filename.read_text(encoding=encoding)
    new_content = increment_headers_in_text(content, shift=shift)
    if new_content is None:
        print(f"Erreur : Aucun en-tête à modifier dans {filename}.")
        return
    else:
        filename.write_text(new_content, encoding=encoding)
        print(f"En-têtes mis à jour dans {filename} avec un décalage de {shift}.")
        return


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python _increment_md_titles.py <filename.md> [shift]")
        sys.exit(1)

    filename = sys.argv[1]
    shift = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    increment_headers(Path(filename), shift=shift)

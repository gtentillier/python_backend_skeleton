import os
from typing import List

keep_project_root = False  # Set to True if you want to keep the project root in the architecture output

folder_to_exclude = [
    '.venv',
    '.git',
    ".github",
    ".vscode",
    "notebooks",
    "default_project_name.egg-info",
    '__pycache__',
]

file_end_to_exclude = [
    '.py',
    '.md',
    '.txt',
    'architecture',
    'LICENCE',
    '.ipynb',
    '.DS_Store',
]

files_to_keep = [
    'copilot-instructions.md',
    'empty.chatmode.md',
    'requirements.txt',
    ".gitignore",
]

folder_to_exclude_inner = []

#!/usr/bin/env python3
"""
Module to save the project architecture (file and folder tree) in a .txt file,
ignoring the .venv folder and markdown files other than README.md.
The tree uses vertical and horizontal lines to visually represent the structure.

Usage:
    python get_archi.py
"""


def ignore_file(file_name: str) -> bool:
    """Check if a file should be ignored based on its name."""
    if file_name in files_to_keep:
        return False
    return (file_name.endswith(tuple(file_end_to_exclude)))


def generate_architecture(root_dir: str, output_file: str) -> None:
    """Generate a textual representation of the project structure and save it to a file.

    Args:
        root_dir (str): The root directory of the project.
        output_file (str): The path to the output text file.
    """
    tree_lines: List[str] = []

    def recurse_dir(current_dir: str, prefix: str = "") -> None:
        try:
            entries = os.listdir(current_dir)
        except OSError as e:
            tree_lines.append(f"{prefix}Error accessing {current_dir}: {e}")
            return

        directories: List[str] = []
        files: List[str] = []
        for entry in sorted(entries):
            full_path = os.path.join(current_dir, entry)
            if os.path.isdir(full_path):
                if entry in folder_to_exclude:
                    continue
                directories.append(entry)
            else:
                if ignore_file(entry):
                    continue
                files.append(entry)

        children = directories + files
        count = len(children)

        for index, child in enumerate(children):
            connector = "└──" if index == count - 1 else "├──"
            tree_lines.append(f"{prefix}{connector} {child}")
            full_child_path = os.path.join(current_dir, child)
            if os.path.isdir(full_child_path):
                # If this directory is in folder_to_exlude_inner, do not recurse into it
                if child in folder_to_exclude_inner:
                    continue
                extension = "    " if index == count - 1 else "│   "
                recurse_dir(full_child_path, prefix + extension)

    if keep_project_root:
        tree_lines.append(f"{os.path.basename(root_dir)}")
    recurse_dir(root_dir)

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(tree_lines))
    except Exception as e:
        print(f"Error writing to file {output_file}: {e}")


if __name__ == "__main__":
    # Assuming the project root is the current working directory.
    project_root = os.getcwd()
    output_path = os.path.join(project_root, "architecture")
    generate_architecture(project_root, output_path)
    print(f"\n📐 Project architecture saved to {output_path}")

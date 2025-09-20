from pathlib import Path
from typing import List, Union

keep_project_root: bool = False  # Set to True if you want to keep the project root in the architecture output

folder_to_exclude: List[str] = [
    ".venv",
    ".git",
    ".github",
    ".vscode",
    "notebooks",
    "default_project_name.egg-info",
    "__pycache__",
]

file_end_to_exclude: List[str] = [
    "__init__.py",
    ".md",
    ".txt",
    "architecture",
    "LICENCE",
    ".ipynb",
    ".DS_Store",
]

files_to_keep: List[str] = [
    "copilot-instructions.md",
    "empty.chatmode.md",
    "requirements.txt",
    ".gitignore",
]

folder_to_exclude_inner: List[str] = []


def ignore_file(file_name: str) -> bool:
    """Check if a file should be ignored based on its name.

    Args:
        file_name (str): Name of the file.

    Returns:
        bool: True if the file should be ignored.
    """
    if file_name in files_to_keep:
        return False
    return file_name.endswith(tuple(file_end_to_exclude))


def generate_architecture_lines(root_dir: Union[str, Path]) -> List[str]:
    """Return a textual representation of the project structure as list of lines.

    Args:
        root_dir (Union[str, Path]): The root directory of the project.

    Returns:
        List[str]: Lines representing the project tree.
    """
    root_path: Path = Path(root_dir)
    tree_lines: List[str] = []

    def recurse_dir(current_dir: Path, prefix: str = "") -> None:
        try:
            entries = sorted([p for p in current_dir.iterdir()], key=lambda p: p.name)
        except OSError as e:
            tree_lines.append(f"{prefix}Error accessing {current_dir}: {e}")
            return

        directories: List[Path] = []
        files: List[Path] = []
        for entry in entries:
            if entry.is_dir():
                if entry.name in folder_to_exclude:
                    continue
                directories.append(entry)
            else:
                if ignore_file(entry.name):
                    continue
                files.append(entry)

        children: List[Path] = directories + files
        count: int = len(children)

        for index, child in enumerate(children):
            connector = "└──" if index == count - 1 else "├──"
            tree_lines.append(f"{prefix}{connector} {child.name}")
            if child.is_dir():
                if child.name in folder_to_exclude_inner:
                    continue
                extension = "    " if index == count - 1 else "│   "
                recurse_dir(child, prefix + extension)

    if keep_project_root:
        tree_lines.append(f"{root_path.name}")
    recurse_dir(root_path)

    return tree_lines


def write_architecture_file(output_file: Union[str, Path], tree_lines: List[str]) -> None:
    """Write the architecture lines to a file.

    Args:
        output_file (Union[str, Path]): Destination file path.
        tree_lines (List[str]): Lines to write.
    """
    output_path: Path = Path(output_file)
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text("\n".join(tree_lines), encoding="utf-8")
    except Exception as e:
        print(f"Error writing to file {output_path}: {e}")


def format_as_codeblock(tree_lines: List[str]) -> str:
    """Return the tree lines wrapped in a fenced code block.

    Args:
        tree_lines (List[str]): Lines to include inside the code block.

    Returns:
        str: The fenced code block as a string.
    """
    return "```\n" + "\n".join(tree_lines) + "\n```"


def replace_fenced_block_in_file(md_file: Union[str, Path], new_block: str, anchor_heading: Union[str, None] = None) -> bool:
    """Replace the first fenced code block (or the first after an anchor) in a markdown file.

    Args:
        md_file (Union[str, Path]): Path to the markdown file to update.
        new_block (str): New fenced block to insert (must include the fence lines).
        anchor_heading (Union[str, None], optional): If provided, search for the first fence after this heading. Defaults to None.

    Returns:
        bool: True if replacement succeeded, False otherwise.
    """
    md_path = Path(md_file)
    try:
        content = md_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {md_path}: {e}")
        return False

    search_start = 0
    if anchor_heading:
        idx = content.find(anchor_heading)
        if idx != -1:
            search_start = idx + len(anchor_heading)

    open_idx = content.find("```", search_start)
    if open_idx == -1:
        # no fenced block found
        return False
    close_idx = content.find("```", open_idx + 3)
    if close_idx == -1:
        # no closing fence
        return False

    new_content = content[:open_idx] + new_block + content[close_idx + 3:]
    try:
        md_path.write_text(new_content, encoding="utf-8")
    except Exception as e:
        print(f"Error writing to {md_path}: {e}")
        return False

    return True


if __name__ == "__main__":
    project_root = Path.cwd()
    output_path = project_root / "architecture"

    # Generate architecture lines and write to the `architecture` file
    tree = generate_architecture_lines(project_root)
    write_architecture_file(output_path, tree)
    print(f"\n📐 Project architecture saved to {output_path}")

    # Replace the fenced block under the architecture heading in copilot-instructions.md
    md_file = project_root / ".github" / "copilot-instructions.md"
    new_block = format_as_codeblock(tree)
    # Use a flexible anchor so the heading number can change (e.g. "## 4. Architecture du projet :")
    anchor = "Architecture du projet"
    replaced = replace_fenced_block_in_file(md_file, new_block, anchor_heading=anchor)
    if replaced:
        print(f"🔁 Updated fenced architecture block in {md_file}")
    else:
        print(f"⚠️ Could not find fenced block to replace in {md_file}")

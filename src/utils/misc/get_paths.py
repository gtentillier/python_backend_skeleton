import os
from typing import Optional

path_project = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))


def path_data(filename: Optional[str] = None) -> str:
    """Get the path to the data directory, optionally appending a filename.
    Args:
        filename (Optional[str]): The name of the file to append to the data path.
    Returns:
        str: The full path to the data directory or the specified file within it.
    """
    if filename is None:
        return os.path.join(path_project, 'data')
    else:
        return os.path.join(path_project, 'data', filename)


__all__ = ["path_project", "path_data"]

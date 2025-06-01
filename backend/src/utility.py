"""
Contains some helper functions for paths
"""

from pathlib import Path

def get_path(file: str) -> str:
    """
    Adds a "file_name" to get correct path.
    """
    here = Path(__file__).resolve().parent
    repo_root = here.parent
    return repo_root / 'json' / f'{file}.json'

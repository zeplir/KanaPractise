"""
Contains some helper functions for paths
"""

from pathlib import Path
import secrets

def get_path(file: str) -> str:
    """
    Adds a "file_name" to get correct path.
    """
    here = Path(__file__).resolve().parent
    repo_root = here.parent
    return repo_root / 'json' / f'{file}.json'

def get_key() -> str:
    """
    Returns the key which is in backend/keys/..
    Not yet implemented...
    """
    #here = Path(__file__).resolve().parent
    #repo_root = here.parent
    #path = repo_root / 'keys' / 'my_key.pem'
    #with open(path, "r") as f:
    #    try:
    #        return f.read()
    #    except FileExistsError as e:
    #        print("Error, %s", e)
    #        return None
    return secrets.token_hex(32)

"""
Contains some helper functions for paths
"""

from pathlib import Path

def get_path(suffix = None) -> str:
    if not suffix:
        return Path(__file__).resolve().parent
    return Path(__file__).resolve().parent / f"{suffix}"

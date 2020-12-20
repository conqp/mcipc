"""Implementation of the function command."""

from pathlib import Path
from typing import Union

from mcipc.rcon.client import Client


__all__ = ['function']


def function(self: Client, name: Union[Path, str]) -> str:
    """Runs the given function."""

    return self.run('function', name)

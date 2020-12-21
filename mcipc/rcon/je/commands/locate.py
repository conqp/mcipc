"""Implementation of the locate command."""

from mcipc.rcon.client import Client
from mcipc.rcon.je.types import Structure


__all__ = ['locate']


def locate(client: Client, structure: Structure) -> str:
    """Locates the respective structure."""

    return client.run('locate', structure)

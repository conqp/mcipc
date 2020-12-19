"""Implementation of the locate command."""

from mcipc.rcon.be.types import Structure
from mcipc.rcon.client import Client


__all__ = ['locate']


def locate(client: Client, structure: Structure) -> str:
    """Locates the respective structure."""

    return client.run('locate', structure)

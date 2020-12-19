"""Implementation of the save command."""

from mcipc.rcon.client import Client
from mcipc.rcon.be.types import SaveCommand


__all__ = ['save']


def save(self: Client, command: SaveCommand) -> str:
    """Issues the specified save command."""

    return self.run('save', command)

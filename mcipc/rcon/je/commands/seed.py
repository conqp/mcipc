"""Implementation of the seed command."""

from mcipc.rcon.client import Client
from mcipc.rcon.je.parsers.seed import parse


__all__ = ['seed']


def seed(self: Client) -> int:
    """Returns the server seed."""

    return parse(self.run('seed'))

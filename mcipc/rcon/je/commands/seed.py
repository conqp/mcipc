"""Implementation of the seed command."""

from mcipc.rcon.je.parsers.seed import parse
from mcipc.rcon.proto import Client


__all__ = ['seed']


def seed(self: Client) -> int:
    """Returns the server seed."""

    return parse(self.run('seed'))

"""Implementation of the list command."""

from mcipc.rcon.client import Client
from mcipc.rcon.je.parser.players import parse
from mcipc.rcon.response_types import Players


__all__ = ['list']


def list(client: Client, uuids: bool = False) -> Players:
    """Returns the players."""

    return parse(client.run('list', 'uuids' if uuids else None))

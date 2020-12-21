"""Implementation of the list command."""

from mcipc.rcon.client import Client
from mcipc.rcon.functions import parsed
from mcipc.rcon.response_types.players import parse


__all__ = ['list']


# pylint: disable=W0622
@parsed(parse)
def list(client: Client, uuids: bool = False) -> str:
    """Returns the players."""

    return client.run('list', 'uuids' if uuids else None)

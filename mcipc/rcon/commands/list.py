"""Implementation of the list command."""

from mcipc.rcon.proto import Client
from mcipc.rcon.response_types import Players


__all__ = ['list_']


def list_(client: Client) -> Players:
    """Returns the players."""

    return Players.from_response(client.run('list'))

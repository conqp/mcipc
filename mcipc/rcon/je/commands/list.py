"""Implementation of the list command."""

from mcipc.rcon.client import Client


__all__ = ['list']


# pylint: disable=W0622
def list(client: Client, uuids: bool = False) -> str:
    """Returns the players."""

    return client.run('list', 'uuids' if uuids else None)

"""Implementation of the list command."""

from mcipc.rcon.proto import Client


__all__ = ['list']


def list(client: Client) -> str:
    """Returns the players."""

    return client.run('list')

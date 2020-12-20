"""Implementation of the list command."""

from mcipc.rcon.client import Client


__all__ = ['list']


def list(client: Client) -> str:    # pylint: disable=W0622
    """Returns the players."""

    return client.run('list')

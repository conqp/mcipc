"""Implementation of the help command."""

from mcipc.rcon.client import Client


__all__ = ['help']


# pylint: disable=W0622
def help(client: Client, command: str = None) -> str:
    """Returns help about commands."""

    return client.run('help', command)

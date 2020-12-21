"""Implementation of the help command."""

from mcipc.rcon.client import Client
from mcipc.rcon.je.parsers.help import parse


__all__ = ['help']


# pylint: disable=W0622
def help(client: Client, command: str = None) -> dict:
    """Returns help about commands."""

    return parse(client.run('help', command))

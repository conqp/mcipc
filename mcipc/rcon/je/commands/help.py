"""Implementation of the help command."""

from mcipc.rcon.client import Client
from mcipc.rcon.je.parsers.help import parse
from mcipc.rcon.response_types import Help


__all__ = ['help']


# pylint: disable=W0622
def help(client: Client, command: str = None) -> Help:
    """Returns help about commands."""

    return parse(client.run('help', command))

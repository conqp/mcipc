"""Implementation of the help command."""

from mcipc.rcon.client import Client
from mcipc.rcon.functions import parsed
from mcipc.rcon.response_types.help import parse


__all__ = ['help']


# pylint: disable=W0622
@parsed(parse)
def help(client: Client, command: str = None) -> str:
    """Returns help about commands."""

    return client.run('help', command)

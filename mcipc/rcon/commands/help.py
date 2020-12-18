"""Implementation of the help command."""

from typing import Union

from mcipc.rcon.proto import Client
from mcipc.rcon.response_types import Help


__all__ = ['help_']


def help_(client: Client, command: Union[str, int] = None) -> Help:
    """Returns help about commands."""

    if command is None:
        text = client.run('help')
    else:
        text = client.run('help', command)

    return Help.from_response(text)

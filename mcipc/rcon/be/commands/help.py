"""Implementation of the help command."""

from typing import Union

from mcipc.rcon.proto import Client


__all__ = ['help']


def help(client: Client, command_or_page: Union[str, int] = None) -> str:
    """Returns help about commands."""

    return client.run('help', command)
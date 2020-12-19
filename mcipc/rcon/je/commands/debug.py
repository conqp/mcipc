"""Implementation of the debug command."""

from mcipc.rcon.client import Client
from mcipc.rcon.types import DebugCommand


__all__ = ['debug']


def debug(self: Client, command: DebugCommand) -> str:
    """Invokes the debug command."""

    return self.run('debug', command)

"""Implementation of the setidletimeout command."""

from mcipc.rcon.client import Client


__all__ = ['setidletimeout']


def setidletimeout(self: Client, minutes: int) -> str:
    """Sets the time before idle players are kicked from the server."""

    return self.run('setidletimeout', minutes)

"""Implementation of the geteduclientinfo command."""

from mcipc.rcon.client import Client


__all__ = ['geteduclientinfo']


def geteduclientinfo(self: Client) -> str:
    """Returns information about the game's client."""

    return self.run('geteduclientinfo')

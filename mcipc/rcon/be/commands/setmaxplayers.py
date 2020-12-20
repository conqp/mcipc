"""Implementation of the setmaxplayers command."""

from mcipc.rcon.client import Client


__all__ = ['setmaxplayers']


def setmaxplayers(self: Client, max_players: int) -> str:
    """Sets the maximally allowed players on the server."""

    return self.run('setmaxplayers', max_players)

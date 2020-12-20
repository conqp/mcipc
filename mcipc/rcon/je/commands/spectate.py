"""Implementation of the spectate command."""

from mcipc.rcon.client import Client


__all__ = ['spectate']


def spectate(self: Client, target: str = None, player: str = None) -> str:
    """Start or stop spectating."""

    return self.run('spectate', target, player)

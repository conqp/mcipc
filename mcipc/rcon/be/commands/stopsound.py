"""Implementation of the stopsound command."""

from mcipc.rcon.client import Client


__all__ = ['stopsound']


def stopsound(self: Client, player: str, sound: str = None) -> str:
    """Stops playing a sound."""

    return self.run('stopsound', player, sound)

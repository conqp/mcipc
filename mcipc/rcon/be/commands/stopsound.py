"""Implementation of the stopsound command."""

from typing import Optional

from mcipc.rcon.client import Client


__all__ = ['stopsound']


def stopsound(self: Client, player: str, sound: Optional[str] = None) -> str:
    """Stops playing a sound."""

    return self.run('stopsound', player, sound)

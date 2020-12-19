"""Implementation of the playsound command."""

from mcipc.rcon.client import Client
from mcipc.rcon.types import Vec3


__all__ = ['playsound']


# pylint: disable=R0913
def playsound(self: Client, sound: str, player: str = None,
              position: Vec3 = None, volume: float = None,
              minimum_volume: float = None) -> str:
    """Plays a sound."""

    return self.run('playsound', sound, player, position, volume,
                    minimum_volume)

"""Implementation of the playsound command."""

from typing import Optional

from mcipc.rcon.client import Client
from mcipc.rcon.types import Vec3


__all__ = ['playsound']


# pylint: disable=R0913
def playsound(
        self: Client,
        sound: str,
        player: Optional[str] = None,
        position: Optional[Vec3] = None,
        volume: Optional[float] = None,
        minimum_volume: Optional[float] = None
) -> str:
    """Plays a sound."""

    return self.run('playsound', sound, player, position, volume,
                    minimum_volume)

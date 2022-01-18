"""Implementation of the playsound command."""

from typing import Optional

from mcipc.rcon.client import Client
from mcipc.rcon.je.types import SoundSource
from mcipc.rcon.types import Vec3


__all__ = ['playsound']


# pylint: disable=R0913
def playsound(
        self: Client,
        sound: str,
        source: SoundSource,
        targets: str,
        pos: Optional[Vec3] = None,
        volume: Optional[float] = None,
        pitch: Optional[float] = None,
        min_volume: Optional[float] = None
) -> str:
    """Plays a sound."""

    return self.run(
        'playsound', sound, source, targets, pos, volume, pitch, min_volume
    )

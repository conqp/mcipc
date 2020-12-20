"""Implementation of the playsound command."""

from mcipc.rcon.client import Client
from mcipc.rcon.je.types import SoundSource
from mcipc.rcon.types import Vec3


__all__ = ['playsound']


# pylint: disable=R0913
def playsound(self: Client, sound: str, source: SoundSource, targets: str,
              pos: Vec3 = None, volume: float = None, pitch: float = None,
              min_volume: float = None) -> str:
    """Plays a sound."""

    return self.run('playsound', sound, source, targets, pos, volume, pitch,
                    min_volume)

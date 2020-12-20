"""Implementation of the stopsound command."""

from mcipc.rcon.client import Client
from mcipc.rcon.je.types import SoundSource


__all__ = ['stopsound']


def stopsound(self: Client, targets: str, source: SoundSource = None,
              sound: str = None) -> str:
    """Stops a sound."""

    return self.run('stopsound', targets, source, sound)

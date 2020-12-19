"""Implementation of the particle command."""

from mcipc.rcon.client import Client
from mcipc.rcon.types import Vec3


__all__ = ['particle']


def particle(self: Client, effect: str, position: Vec3) -> str:
    """Creates the respective particles."""

    return self.run('particle', effect, position)

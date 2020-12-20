"""Implementation of the setworldspawn command."""

from mcipc.rcon.client import Client
from mcipc.rcon.types import Vec3


__all__ = ['setworldspawn']


def setworldspawn(self: Client, pos: Vec3 = None, angle: float = None) -> str:
    """Sets the world spawn."""

    return self.run('setworldspawn', pos, angle)

"""Implementation of the clearspawnpoint."""

from mcipc.rcon.client import Client
from mcipc.rcon.types import Vec3


__all__ = ['clearspawnpoint']


def clearspawnpoint(self: Client, player: str = None) -> str:
    """Used to remove spawnpoints in the world."""

    return self.run('clearspawnpoint', player)

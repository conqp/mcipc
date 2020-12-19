"""Implementation of the spawnpoint command."""

from mcipc.rcon.client import Client
from mcipc.rcon.types import Vec3


__all__ = ['spawnpoint']


def spawnpoint(self: Client, player: str = None,
               spawn_pos: Vec3 = None) -> str:
    """Sets the spawn point for a player."""

    return self.run('spawnpoint', player, spawn_pos)

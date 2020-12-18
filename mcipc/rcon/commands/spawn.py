"""Spawn-related commands."""

from mcipc.rcon.proto import Client
from mcipc.rcon.types import Vec3


__all__ = ['clearspawnpoint', 'setworldspawn', 'spawnpoint']


def clearspawnpoint(self: Client, player: str = None) -> str:
    """Used to remove spawnpoints in the world."""

    return self.run('clearspawnpoint', player)


def setworldspawn(self: Client, position: Vec3 = None,
                  angle: float = None) -> str:
    """Sets the world spawn."""

    return self.run('setworldspawn', position, angle)


def spawnpoint(self: Client, targets: str = None, position: Vec3 = None,
               angle: float = None) -> str:
    """Sets the spawn point for a player."""

    return self.run('spawnpoint', targets, position, angle)

"""Implementation of the spawnpoint command."""

from typing import Optional

from mcipc.rcon.client import Client
from mcipc.rcon.types import Vec3


__all__ = ['spawnpoint']


def spawnpoint(
        self: Client,
        player: Optional[str] = None,
        spawn_pos: Optional[Vec3] = None
) -> str:
    """Sets the spawn point for a player."""

    return self.run('spawnpoint', player, spawn_pos)

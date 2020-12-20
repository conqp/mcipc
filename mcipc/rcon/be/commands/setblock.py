"""Implementation of the setblock command."""

from mcipc.rcon.client import Client
from mcipc.rcon.types import SetblockMode, Vec3


__all__ = ['setblock']


def setblock(self: Client, position: Vec3, tile_name: str,
             tile_data: int = None, mode: SetblockMode = None) -> str:
    """Sets a block."""

    return self.run('setblock', position, tile_name, tile_data, mode)

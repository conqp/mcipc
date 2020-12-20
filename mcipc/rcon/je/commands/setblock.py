"""Implementation of the setblock command."""

from mcipc.rcon.client import Client
from mcipc.rcon.types import SetblockMode, Vec3


__all__ = ['setblock']


def setblock(self: Client, pos: Vec3, block: str,
             mode: SetblockMode = None) -> str:
    """Sets a block."""

    return self.run('setblock', pos, block, mode)

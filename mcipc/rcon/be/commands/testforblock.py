"""Implementation of the testforblock command."""

from typing import Optional

from mcipc.rcon.client import Client
from mcipc.rcon.types import Vec3


__all__ = ['testforblock']


def testforblock(
        self: Client,
        position: Vec3,
        tile_name: str,
        data_value: Optional[int] = None
) -> str:
    """Tests whether a certain block is in a specific location."""

    return self.run('testforblock', position, tile_name, data_value)

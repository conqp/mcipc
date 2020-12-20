"""Implementation of the fill command."""

from mcipc.rcon.client import Client
from mcipc.rcon.types import FillMode, Vec3


__all__ = ['fill']


# pylint: disable=C0103,R0913
def fill(self: Client, from_: Vec3, to: Vec3, block: str,
         tile_data: int = None, old_block_handling: FillMode = None,
         replace_tile_name: str = None, replace_data_value: str = None) -> str:
    """Fills all or parts of a region with a specific block."""

    return self.run('fill', from_, to, block, tile_data, old_block_handling,
                    replace_tile_name, replace_data_value)

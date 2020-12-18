"""Implementation of the fill command."""

from mcipc.rcon.proto import Client
from mcipc.rcon.types import FillMode, Vec3


__all__ = ['fill_be', 'fill_je']


# pylint: disable=W0622,R0913,C0103
def fill_be(self: Client, from_: Vec3, to: Vec3, block: str,
            tile_data: int = None, old_block_handling: FillMode = None,
            replace_tile_name: str = None,
            replace_data_value: str = None) -> str:
    """Fills all or parts of a region with a specific block."""

    return self.run('fill', from_, to, block, tile_data, old_block_handling,
                    replace_tile_name, replace_data_value)


def fill_je(self: Client, from_: Vec3, to: Vec3, block: str,
            mode: FillMode = None, filter: str = None) -> str:
    """Fills all or parts of a region with a specific block."""

    command = ['fill', from_, to, block, (mode := FillMode(mode))]

    if filter is not None and mode == FillMode.REPLACE:
        command.append(filter)

    return self.run(*command)

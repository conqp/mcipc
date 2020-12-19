"""Implementation of the fill command."""

from mcipc.rcon.proto import Client
from mcipc.rcon.types import FillMode, Vec3


__all__ = ['fill']


def fill(self: Client, from_: Vec3, to: Vec3, block: str,
         mode: FillMode = None, filter: str = None) -> str:
    """Fills all or parts of a region with a specific block."""

    command = ['fill', from_, to, block, (mode := FillMode(mode))]

    if filter is not None and mode == FillMode.REPLACE:
        command.append(filter)

    return self.run(*command)

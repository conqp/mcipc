"""Implementation of the fill command."""

from mcipc.rcon.client import Client
from mcipc.rcon import FillMode
from mcipc.rcon.types import Vec3 as Vec3Hint


__all__ = ['fill']


# pylint: disable=C0103,R0913,W0622
def fill(self: Client, from_: Vec3Hint, to: Vec3Hint, block: str,
         mode: FillMode = None, filter: str = None) -> str:
    """Fills all or parts of a region with a specific block."""

    command = ['fill', from_, to, block]

    if mode is not None:
        command.append(mode := FillMode(mode))

        if filter is not None and mode == FillMode.REPLACE:
            command.append(filter)

    return self.run(*command)

"""Implementation of the fill command."""

from typing import Optional
from mcipc.rcon.client import Client
from mcipc.rcon.enumerations import FillMode
from mcipc.rcon.types import FillMode as FillModeHint, Vec3


__all__ = ['fill']


def fill(
        self: Client,
        from_: Vec3,
        to: Vec3,
        block: str,
        mode: Optional[FillModeHint] = None,
        filter: Optional[str] = None
) -> str:
    """Fills all or parts of a region with a specific block."""

    command = ['fill', from_, to, block]

    if mode is not None:
        command.append(mode := FillMode(mode))

        if filter is not None and mode == FillMode.REPLACE:
            command.append(filter)

    return self.run(*command)

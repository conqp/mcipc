"""Implementation of the clone command."""

from mcipc.rcon.client import Client
from mcipc.rcon.enumerations import MaskMode
from mcipc.rcon.types import CloneMode, MaskMode as MaskModeHint, Vec3


__all__ = ['clone']


# pylint: disable=W0622
def clone(self: Client, begin: Vec3, end: Vec3, destination: Vec3, *,
          mask_mode: MaskModeHint = None, filter: str = None,
          clone_mode: CloneMode = None) -> str:
    """Clones blocks from one region to another."""

    args = ['clone', begin, end, destination]

    if mask_mode is not None:
        args.append(mask_mode := MaskMode(mask_mode))

        if mask_mode == MaskMode.FILTERED:
            if filter is None:
                raise ValueError('Missing filter.')

            args.append(filter)

        args.append(clone_mode)

    return self.run(*args)

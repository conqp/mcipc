"""Implementation of the clone command."""

from mcipc.rcon.client import Client
from mcipc.rcon import CloneMode, MaskMode
from mcipc.rcon.types import Vec3 as Vec3Hint


__all__ = ['clone']


def clone(self: Client, begin: Vec3Hint, end: Vec3Hint, destination: Vec3Hint, *,
          mask_mode: MaskMode = None,
          filter: str = None,   # pylint: disable=W0622
          clone_mode: CloneMode = None) -> str:
    """Clones blocks from one region to another."""

    args = ['clone', begin, end, destination]

    if mask_mode is not None:
        args.append(mask_mode := MaskMode(mask_mode))

        if mask_mode == str(MaskMode.FILTERED):
            if filter is None:
                raise ValueError('Missing filter.')

            args.append(filter)

        args.append(clone_mode)

    return self.run(*args)

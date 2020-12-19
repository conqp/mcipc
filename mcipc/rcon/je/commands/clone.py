"""Implementation of the clone command."""

from mcipc.rcon.client import Client
from mcipc.rcon.types import CloneMode, MaskMode, Vec3


__all__ = ['clone']


def clone(self: Client, begin: Vec3, end: Vec3, destination: Vec3, *,
          mask_mode: MaskMode = None,
          filter: str = None,   # pylint: disable=W0622
          clone_mode: CloneMode = None) -> str:
    """Clones blocks from one region to another."""

    args = ['clone', begin, end, destination]

    if mask_mode is not None:
        args.append(mask_mode := str(mask_mode))

        if mask_mode == str(MaskMode.FILTERED):
            if filter is None:
                raise ValueError('Missing filter.')

            args.append(filter)

        args.append(clone_mode)

    return self.run(*args)

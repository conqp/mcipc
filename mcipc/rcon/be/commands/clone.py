"""Implementation of the clone command."""

from mcipc.rcon.client import Client
from mcipc.rcon.enumerations import MaskMode
from mcipc.rcon.types import CloneMode, MaskMode as MaskModeHint, Vec3


__all__ = ['clone']


def clone(self: Client, begin: Vec3, end: Vec3, destination: Vec3, *,
          mask_mode: MaskModeHint = None, clone_mode: CloneMode = None,
          tile_name: str = None, tile_data: int = None) -> str:
    """Clones blocks from one region to another."""

    args = ['clone', begin, end, destination]

    if mask_mode is not None:
        args.append(mask_mode := MaskMode(mask_mode))

        if filtered := mask_mode == MaskMode.FILTERED:
            if clone_mode is None:
                raise ValueError('Missing clone mode.')

            if tile_name is None:
                raise ValueError('Missing tile name.')

            if tile_data is None:
                raise ValueError('Missing tile data.')

        args.append(clone_mode)

        if filtered:
            args += [tile_name, tile_data]

    return self.run(*args)

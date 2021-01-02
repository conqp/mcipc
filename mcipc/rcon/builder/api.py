"""Exposed API functions."""

from mcipc.rcon.builder.functions import check_xz_dir
from mcipc.rcon.builder.functions import offsets
from mcipc.rcon.builder.functions import normalize
from mcipc.rcon.builder.functions import validate
from mcipc.rcon.builder.item import Item
from mcipc.rcon.builder.types import Anchor, Direction, Profile, Vec3
from mcipc.rcon.client import Client
from mcipc.rcon.enumerations import FillMode


__all__ = ['mktunnel']


def mktunnel(client: Client, profile: Profile, start: Vec3, *,
             end: Vec3 = None, direction: Direction = None, length: int = 1,
             anchor: Anchor = Anchor.BOTTOM_RIGHT, default: Item = Item.AIR,
             mode: FillMode = None, filter: str = None):
    """Creates a tunnel with the given profile."""

    start = Vec3(*start)    # Ensure Vec3 object.

    if not validate(profile):
        raise ValueError('Invalid matrix.')

    if end is None:
        end = start + direction.value * (length - 1)
    else:
        end = Vec3(*end)    # Ensure Vec3 object.

    final_direction: Vec3 = check_xz_dir(start, end)
    profile = list(normalize(profile, default=default))

    for block, offset in offsets(profile, final_direction, anchor):
        result = client.fill(
            start + offset, end + offset, block, mode=mode, filter=filter
        )
        print(result)

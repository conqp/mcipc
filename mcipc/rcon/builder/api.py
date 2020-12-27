"""Exposed API functions."""

from mcipc.rcon.builder.functions import check_xz_dir
from mcipc.rcon.builder.functions import get_offset
from mcipc.rcon.builder.functions import normalize
from mcipc.rcon.builder.functions import validate
from mcipc.rcon.builder.item import Item
from mcipc.rcon.builder.types import Anchor, Direction, Profile, Vec3
from mcipc.rcon.client import Client


__all__ = ['mktunnel']


def mktunnel(client: Client, profile: Profile, start: Vec3, *,
             end: Vec3 = None, direction: Direction = None, length: int = 1,
             anchor: Anchor = Anchor.BOTTOM_RIGHT, default: Item = Item.AIR):
    """Creates a tunnel with the given profile."""

    start = Vec3(*start)    # Ensure Vec3 object.

    if not validate(profile):
        raise ValueError('Invalid matrix.')

    if end is None:
        end = start + direction.value * length
    else:
        end = Vec3(*end)    # Ensure Vec3 object.

    direction = check_xz_dir(start, end)
    profile = list(normalize(profile, default=default))

    for y, row in enumerate(profile):   # pylint: disable=C0103
        for xz, block in enumerate(row):    # pylint: disable=C0103
            offset = get_offset(y, xz, direction, anchor)
            result = client.fill(start + offset, end + offset, block)
            print(result)

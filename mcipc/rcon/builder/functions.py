"""Helper functions."""

from typing import Iterator

from mcipc.rcon.builder.item import Item
from mcipc.rcon.builder.types import Anchor, Profile, Row, Vec3


__all__ = ['validate', 'normalize', 'check_xz_dir', 'get_offset']


def validate(profile: Profile) -> bool:
    """Sanitizes a matrix."""

    rows = iter(profile)

    try:
        first = len(next(rows))
    except StopIteration:
        return True

    return all(len(row) == first for row in rows)


def normalize(profile: Profile, default: Item = Item.AIR) -> Iterator[Row]:
    """Normalizes a profile."""

    for row in profile:
        yield [default if block is None else Item(block) for block in row]


def check_xz_dir(start: Vec3, end: Vec3) -> Vec3:
    """Checks whether the vetors for a line."""

    if sum(coord1 != coord2 for coord1, coord2 in zip(start, end)) != 1:
        raise ValueError('Not one direction given.')

    return end - start


# pylint: disable=C0103
def get_offset(y: int, xz: int, direction: Vec3, anchor: Anchor) -> Vec3:
    """Returns returns the offset."""

    top = anchor in {Anchor.TOP_LEFT, Anchor.TOP_RIGHT}
    left = anchor in {Anchor.TOP_LEFT, Anchor.BOTTOM_LEFT}

    if direction.north:
        return Vec3(xz if left else -xz, -y if top else y, 0)

    if direction.south:
        return Vec3(-xz if left else xz, -y if top else y, 0)

    if direction.east:
        return Vec3(0, -y if top else y, xz if left else -xz)

    if direction.west:
        return Vec3(0, -y if top else y, -xz if left else xz)

    raise ValueError('Cannot determine offset.')

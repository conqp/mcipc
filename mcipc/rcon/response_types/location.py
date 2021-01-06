"""Locations."""

from re import fullmatch
from typing import NamedTuple, Union

from mcipc.functions import json_serializable
from mcipc.rcon.errors import LocationNotFound


__all__ = ['Location', 'parse']


REGEX = ('The nearest (.+) is at \\[(-?\\d+), (~|-?\\d+), '
         '(-?\\d+)\\] \\((\\d+) block[s]? away\\)')


@json_serializable
class Location(NamedTuple):
    """A 3D location."""

    name: str
    x: int
    y: Union[int, None]
    z: int
    distance: int


def parse(text: str) -> Location:
    """Creates a location from a server response."""

    if (match := fullmatch(REGEX, text)) is None:
        raise LocationNotFound(text)

    name, x, y, z, distance = match.groups()    # pylint: disable=C0103
    return Location(name, int(x), None if y == '~' else int(y), int(z),
                    int(distance))

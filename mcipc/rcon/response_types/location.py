"""Locations."""

from __future__ import annotations
from re import fullmatch
from typing import NamedTuple, Union

from mcipc.rcon.exceptions import NotALocation


__all__ = ['Location']


REGEX = ('The nearest (.+) is at \\[(-?\\d+), (~|-?\\d+), '
         '(-?\\d+)\\] \\((\\d+) block[s]? away\\)')


class Location(NamedTuple):
    """A 3D location."""

    name: str
    x: int
    y: Union[int, None]
    z: int
    distance: int

    @classmethod
    def from_response(cls, text: str) -> Location:
        """Creates a location from a server response."""
        if (match := fullmatch(REGEX, text)) is None:
            raise NotALocation(text)

        name, x, y, z, distance = match.groups()    # pylint: disable=C0103
        return cls(name, int(x), None if y == '~' else int(y), int(z),
                   int(distance))

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {
            'name': self.name,
            'x': self.x,
            'y': self.y,
            'z': self.z,
            'distance': self.distance
        }

"""Locations."""

from __future__ import annotations
from re import compile  # pylint: disable=W0622
from typing import NamedTuple, Union

from mcipc.rcon.exceptions import NotALocation


__all__ = ['Location']


REGEX = compile('.*\\[(-?\\d+), (~|-?\\d+), (-?\\d+)\\].*')


class Location(NamedTuple):
    """A 3D location."""

    x: int
    y: Union[int, None]
    z: int

    @classmethod
    def from_response(cls, text: str) -> Location:
        """Creates a location from a server response."""
        if (match := REGEX.fullmatch(text)) is None:
            raise NotALocation(text)

        x, y, z = match.groups()    # pylint: disable=C0103
        return cls(int(x), None if y == '~' else int(y), int(z))

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {'x': self.x, 'y': self.y, 'z': self.z}

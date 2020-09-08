"""Locations."""

from re import compile  # pylint: disable=W0622
from typing import NamedTuple, Union

from mcipc.rcon.exceptions import NotALocation


__all__ = ['Location']


REGEX = compile('.*\\[(-?\\d+), (~|-?\\d+), (-?\\d+)\\].*')


def _int_or_none(string: str) -> Union[int, None]:
    """Returns None iff coordinate is special "~"
    character or else the respective integer value.
    """

    if string == '~':
        return None

    return int(string)


class Location(NamedTuple):
    """A 3D location."""

    x: int
    y: Union[int, None]
    z: int

    @classmethod
    def from_response(cls, text: str):
        """Creates a location from a server response."""
        match = REGEX.fullmatch(text)

        if match is None:
            raise NotALocation(text)

        coord_x, coord_y, coord_z = match.groups()
        return cls(int(coord_x), _int_or_none(coord_y), int(coord_z))

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {'x': self.x, 'y': self.y, 'z': self.z}

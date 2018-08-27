"""Locations."""

from collections import namedtuple
from re import compile  # pylint: disable=W0622


__all__ = ['Location']


REGEX = compile('.*\\[(-?\\d+), (~|-?\\d+), (-?\\d+)\\].*')


def _int_or_none(string):
    """Returns None iff coordinate is special "~"
    character or else the respective integer value.
    """

    if string == '~':
        return None

    return int(string)


class Location(namedtuple('Location', ('x', 'y', 'z'))):
    """A 3D location."""

    __slots__ = ()

    @classmethod
    def from_response(cls, text):
        """Creates a location from a server response."""
        match = REGEX.fullmatch(text)
        return cls(*(_int_or_none(item) for item in match.groups()))

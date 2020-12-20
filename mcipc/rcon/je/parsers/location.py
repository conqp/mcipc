"""Parses a location from a server response."""

from re import fullmatch

from mcipc.rcon.response_types import Location


__all__ = ['parse']


REGEX = ('The nearest (.+) is at \\[(-?\\d+), (~|-?\\d+), '
         '(-?\\d+)\\] \\((\\d+) block[s]? away\\)')


def parse(text: str) -> Location:
    """Creates a location from a server response."""

    if (match := fullmatch(REGEX, text)) is None:
        raise ValueError(text)

    name, x, y, z, distance = match.groups()    # pylint: disable=C0103
    return Location(name, int(x), None if y == '~' else int(y), int(z),
                    int(distance))

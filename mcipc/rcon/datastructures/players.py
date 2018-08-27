"""Information about online players."""

from collections import namedtuple
from re import compile  # pylint: disable=W0622


__all__ = ['Players']


REGEX = compile('.+ (\\d+) .+ (\\d+) .+: (.*)')


class Players(namedtuple('Players', ('online', 'max', 'names'))):
    """Online players information."""

    __slots__ = ()

    @classmethod
    def from_response(cls, text):
        """Creates the players information from a server response."""
        match = REGEX.fullmatch(text)
        online, max_, names = match.groups()
        names = [name.strip() for name in names.split(', ') if name.strip()]
        return cls(int(online), int(max_), tuple(names))

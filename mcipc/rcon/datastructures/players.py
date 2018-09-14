"""Information about online players."""

from re import compile  # pylint: disable=W0622
from typing import NamedTuple, Tuple


__all__ = ['Players']


REGEX = compile('.+ (\\d+) .+ (\\d+) .+: (.*)')


class Players(NamedTuple):
    """Online players information."""

    online: int
    max: int
    names: Tuple[str]

    @classmethod
    def from_response(cls, text):
        """Creates the players information from a server response."""
        match = REGEX.fullmatch(text)
        online, max_, names = match.groups()
        names = filter(None, map(lambda name: name.strip(), names.split(', ')))
        return cls(int(online), int(max_), tuple(names))

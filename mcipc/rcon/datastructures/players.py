"""Information about online players."""

from __future__ import annotations
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
    def from_response(cls, text: str) -> Players:
        """Creates the players information from a server response."""
        match = REGEX.fullmatch(text)
        online, max_, names = match.groups()
        names = filter(None, map(lambda name: name.strip(), names.split(', ')))
        return cls(int(online), int(max_), tuple(names))

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {'online': self.online, 'max': self.max, 'names': self.names}

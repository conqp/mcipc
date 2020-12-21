"""Result of a successful kick."""

from re import fullmatch
from typing import NamedTuple

from mcipc.rcon.errors import NoPlayerFound


__all__ = ['KickedPlayer', 'parse']


REGEX = 'Kicked (.*): (.*)'


class KickedPlayer(NamedTuple):
    """Stores information about a kicked player."""

    name: str
    reason: str

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {'name': self.name, 'reason': self.reason}


def parse(text: str) -> KickedPlayer:
    """Parses a kicked player from the text."""

    if (match := fullmatch(REGEX, text)) is not None:
        return KickedPlayer(*match.groups())

    raise NoPlayerFound()

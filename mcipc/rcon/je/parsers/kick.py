"""Parsing of kick events."""

from re import fullmatch

from mcipc.rcon.je.errors import NoPlayerFound
from mcipc.rcon.response_types import KickedPlayer


__all__ = ['parse']


REGEX = 'Kicked (.*): (.*)'


def parse(text: str) -> KickedPlayer:
    """Parses a kicked player from the text."""

    if (match := fullmatch(REGEX, text)) is not None:
        return KickedPlayer(*match.groups())

    raise NoPlayerFound()

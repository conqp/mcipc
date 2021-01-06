"""Result of a successful kick."""

from re import fullmatch
from typing import NamedTuple

from mcipc.functions import json_serializable
from mcipc.rcon.errors import NoPlayerFound


__all__ = ['KickedPlayer', 'parse']


REGEX = 'Kicked (.*): (.*)'


@json_serializable
class KickedPlayer(NamedTuple):
    """Stores information about a kicked player."""

    name: str
    reason: str


def parse(text: str) -> KickedPlayer:
    """Parses a kicked player from the text."""

    if (match := fullmatch(REGEX, text)) is not None:
        return KickedPlayer(*match.groups())

    raise NoPlayerFound()

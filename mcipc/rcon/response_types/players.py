"""Information about online players."""

from __future__ import annotations
from re import Match, fullmatch
from typing import Generator, NamedTuple, Tuple
from uuid import UUID


__all__ = ['Players']


REGEX_JAVA = '.+ (\\d+) .+ (\\d+) .+: (.*)'
REGEX_JAVA_NAME = '(\\S+)(?: \\((\\S+)\\))?'
REGEX_PAPER = '.+ §c(\\d+)§6 .+ §c(\\d+)§6 .+\\.([\\s\\S]*)'
REGEX_PAPER_NAME = '(.+): (?:§4)?(\\w+)(?:§r)?§f'


class Player(NamedTuple):
    """Player names with optional UUIDs."""

    name: str
    uuid: UUID = None
    state: str = None

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {'name': str(self), 'uuid': self.uuid.hex, 'state': self.state}


class Players(NamedTuple):
    """Online players information."""

    online: int
    max: int
    players: Tuple[Player]

    @property
    def names(self) -> Tuple[str]:  # XXX: For backward compatibility.
        """Returns a tuple of the players' names."""
        return tuple(player.name for player in self.players)

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {
            'online': self.online,
            'max': self.max,
            'players': [player.to_json() for player in self.players]
        }

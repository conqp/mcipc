"""Information about online players."""

from re import Match, fullmatch
from typing import Iterator, List, NamedTuple, Optional
from uuid import UUID

from mcipc.functions import json_serializable


__all__ = ['Player', 'Players', 'parse']


REGEX_JAVA = '.+ (\\d+) .+ (\\d+) .+: (.*)'
REGEX_JAVA_NAME = '(\\S+)(?: \\((\\S+)\\))?'
REGEX_PAPER = '.+ §c(\\d+)§6 .+ §c(\\d+)§6 .+\\.([\\s\\S]*)'
REGEX_PAPER_NAME = '§6(.+)§r: (?:§4)?(\\w+)(?:§r)?§f'


@json_serializable
class Player(NamedTuple):
    """Player names with optional UUIDs."""

    name: str
    uuid: Optional[UUID] = None
    state: Optional[str] = None


@json_serializable
class Players(NamedTuple):
    """Online players information."""

    online: int
    max: int
    players: List[Player]

    @property
    def names(self) -> List[str]:
        """Returns a list of the players' names
        for backward compatibility.
        """
        return [player.name for player in self.players]


def player_from_java_name(name: str) -> Player:
    """Returns a player from a Java Edition response name."""

    if (match := fullmatch(REGEX_JAVA_NAME, name)) is None:
        raise ValueError(f'Invalid Java Edition server string: {name}')

    name, uuid = match.groups()
    return Player(name, uuid=None if uuid is None else UUID(uuid))


def players_from_java_names(names: str) -> Iterator[Player]:
    """Yields players from a Java Edition response names."""

    for name in filter(None, map(str.strip, names.split(', '))):
        yield player_from_java_name(name)


def player_from_paper_name(name: str) -> Player:
    """Returns a player from a Paper server response name."""

    if (match := fullmatch(REGEX_PAPER_NAME, name.strip())) is None:
        raise ValueError(f'Invalid Paper server string: {name}')

    state, name = match.groups()
    return Player(name, state=state)


def players_from_paper_names(names: str) -> Iterator[Player]:
    """Yields players from a paper server response names."""

    for name in filter(None, names.split('\n')):
        yield player_from_paper_name(name)


def from_java(match: Match) -> Players:
    """Creates the players information from a Java Edition server match."""

    online, max_, names = match.groups()
    players = players_from_java_names(names)
    return Players(int(online), int(max_), list(players))


def from_paper(match: Match) -> Players:
    """Creates the players information from a Paper server match.
    https://github.com/conqp/mcipc/issues/13#issuecomment-726145034
    """

    online, max_, names = match.groups()
    players = players_from_paper_names(names)
    return Players(int(online), int(max_), list(players))


def parse(text: str) -> Players:
    """Creates the players information from a server response."""

    if (match := fullmatch(REGEX_JAVA, text)) is not None:
        return from_java(match)

    if (match := fullmatch(REGEX_PAPER, text)) is not None:
        return from_paper(match)

    raise ValueError('Unexpected players response:', text)

"""Information about online players."""

from re import Match, fullmatch
from typing import Iterator, NamedTuple, Tuple
from uuid import UUID


__all__ = ['Player', 'Players', 'parse']


REGEX_JAVA = '.+ (\\d+) .+ (\\d+) .+: (.*)'
REGEX_JAVA_NAME = '(\\S+)(?: \\((\\S+)\\))?'
REGEX_PAPER = '.+ §c(\\d+)§6 .+ §c(\\d+)§6 .+\\.([\\s\\S]*)'
REGEX_PAPER_NAME = '§6(.+)§r: (?:§4)?(\\w+)(?:§r)?§f'


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


def player_from_java_name(name: str) -> Player:
    """Returns a player from a Java Edition response name."""

    if (match := fullmatch(REGEX_JAVA_NAME, name)) is None:
        raise ValueError(f'Invalid Java Edition server string: {name}')

    name, uuid = match.groups()
    uuid = None if uuid is None else UUID(uuid)
    return Player(name, uuid=uuid)


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
    return Players(int(online), int(max_), tuple(players))


def from_paper(match: Match) -> Players:
    """Creates the players information from a Paper server match.
    https://github.com/conqp/mcipc/issues/13#issuecomment-726145034
    """

    online, max_, names = match.groups()
    players = players_from_paper_names(names)
    return Players(int(online), int(max_), tuple(players))


def parse(text: str) -> Players:
    """Creates the players information from a server response."""

    if (match := fullmatch(REGEX_JAVA, text)) is not None:
        return from_java(match)

    if (match := fullmatch(REGEX_PAPER, text)) is not None:
        return from_paper(match)

    raise ValueError('Unexpected players response:', text)

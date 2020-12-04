"""Tests players parsing.

For the Paper-related stuff, see: https://github.com/conqp/mcipc/issues/13
"""

from random import choice, choices, randint
from string import ascii_letters, digits
from typing import Generator

from unittest import TestCase

from mcipc.rcon.datastructures.players import Players


VANILLA_STR = 'There are {online} of a max of {max} players online: {names}'
PAPER_STR = (
    '§6Es sind §c{online}§6 von maximal §c{max}§6 Spielern online.{names}'
)
PAPER_PLAYER_TEMPLATE = '§6{prefix}§r: §4{name}{suffix}§f'
PAPER_PLAYER_SUFFIX = '§r'
PAPER_PREFIXES = ('dev', 'obsidian')


def players_to_vanilla_str(players: Players) -> str:
    """Returns a string as returned by a vanilla server."""

    return VANILLA_STR.format(
        online=players.online,
        max=players.max,
        names=', '.join(players.names)
    )


def get_paper_players(players: Players) -> Generator[str, None, None]:
    """Yieds player names formatted like on a Paper server."""

    if not players.names:
        return

    yield ''    # For initial newline.
    *names, last = players.names

    for name in names:
        yield PAPER_PLAYER_TEMPLATE.format(
            prefix=choice(PAPER_PREFIXES),
            name=name,
            suffix=PAPER_PLAYER_SUFFIX
        )

    yield PAPER_PLAYER_TEMPLATE.format(
        prefix=choice(PAPER_PREFIXES),
        name=last,
        suffix=''
    )


def players_to_paper_str(players: Players) -> str:
    """Returns a string as returned by a Paper server."""

    return PAPER_STR.format(
        online=players.online,
        max=players.max,
        names='\n'.join(get_paper_players(players))
    )


def get_random_player_name(pool: str = ascii_letters+digits,
                           minlen: int = 1, maxlen: int = 100) -> str:
    """Returns a random player name."""

    return ''.join(choices(pool, k=randint(minlen, maxlen)))


def get_players_test_cases(count: int = 100) -> Generator[Players, None, None]:
    """Yields player strings for a vanilla server."""

    for online in range(count):
        yield Players(
            online,
            randint(online, online*2),
            tuple(get_random_player_name() for _ in range(online))
        )


class TestPlayers(TestCase):
    """Tests players parsing on a vanilla server."""

    def check_string(self, string: str, players: Players):
        """Checks whether players tuples are considered equal."""
        self.assertEqual(Players.from_response(string), players)

    def check_vanilla(self, players: Players):
        """Tests players response parsing from a vanilla server."""
        self.check_string(players_to_vanilla_str(players), players)

    def check_paper(self, players: Players):
        """Tests players response parsing from a paper server."""
        self.check_string(players_to_paper_str(players), players)

    def test_players(self):
        """Tests players response parsing."""
        for players in get_players_test_cases():
            self.check_vanilla(players)
            self.check_paper(players)

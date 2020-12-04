"""Tests players parsing."""

from random import choice, choices, randint
from string import ascii_letters, digits
from typing import Iterable, NamedTuple

from unittest import TestCase

from mcipc.rcon.datastructures.players import Players


VANILLA_STR = 'There are {online} of a max of {max} players online: {names}'
PAPER_STR = (
    '§6Es sind §c{online}§6 von maximal §c{max}§6 Spielern online.{names}'
)
PAPER_PLAYER_TEMPLATE = '§6{prefix}§r: §4{name}{suffix}§f'
PAPER_PLAYER_SUFFIX = '§r'
PAPER_PREFIXES = ('dev', 'obsidian')


class PlayersTestSetting(NamedTuple):
    """A test setting for a players string."""

    online: int
    max: int
    names: Iterable[str]

    def to_vanilla_str(self):
        """Returns a string as returned by a vanilla server."""
        return VANILLA_STR.format(
            online=self.online, max=self.max, names=', '.join(self.names))

    def get_paper_players(self):
        """Yieds player names formatted like on a Paper server."""
        if not self.names:
            return

        yield ''    # For initial newline.
        *names, last = self.names

        for name in names:
            yield PAPER_PLAYER_TEMPLATE.format(
                prefix=choice(PAPER_PREFIXES), name=name,
                suffix=PAPER_PLAYER_SUFFIX
            )

        yield PAPER_PLAYER_TEMPLATE.format(
            prefix=choice(PAPER_PREFIXES), name=last, suffix='')

    def to_paper_str(self):
        """Returns a string as returned by a Paper server.
        See: https://github.com/conqp/mcipc/issues/13
        """
        names = '\n'.join(self.get_paper_players())
        return PAPER_STR.format(online=self.online, max=self.max, names=names)


def get_random_player_name(pool=ascii_letters+digits, minlen=1, maxlen=100):
    """Returns a random player name."""

    length = randint(minlen, maxlen)
    return ''.join(choices(pool, k=length))


def get_player_settings(count=100):
    """Yields player strings for a vanilla server."""

    for online in range(count):
        yield PlayersTestSetting(
            online,
            randint(online, online*2),
            [get_random_player_name() for _ in range(online)]
        )


class TestPlayers(TestCase):
    """Tests players parsing on a vanilla server."""

    def assertPlayersEqual(self, one, other):   # pylint: disable=C0103
        """Checks whether players tuples are considered equal."""
        self.assertEqual(one.online, other.online)
        self.assertEqual(one.max, other.max)
        self.assertSequenceEqual(one.names, other.names)

    def test_vanilla(self):
        """Tests players from a vanilla server."""
        for test_setting in get_player_settings():
            players = Players.from_response(test_setting.to_vanilla_str())
            self.assertPlayersEqual(test_setting, players)

    def test_paper(self):
        """Tests players from a paper server."""
        for test_setting in get_player_settings():
            players = Players.from_response(test_setting.to_paper_str())
            self.assertPlayersEqual(test_setting, players)

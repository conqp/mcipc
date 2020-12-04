"""Tests players parsing."""

from random import choices, randint
from string import ascii_letters, digits
from typing import Iterable, NamedTuple

from unittest import TestCase

from mcipc.rcon.datastructures.players import Players


VANILLA_STR = 'There are {online} of a max of {max} players online: {names}'


class PlayersTestSetting(NamedTuple):
    """A test setting for a players string."""

    online: int
    max: int
    names: Iterable[str]

    def to_vanilla_str(self):
        """Returns a string as returned by a vanilla server."""
        return VANILLA_STR.format(
            online=self.online, max=self.max, names=', '.join(self.names))


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

    def test_vanilla(self):
        """Tests players from a vanilla server."""

        for player_setting in get_player_settings():
            players = Players.from_response(player_setting.to_vanilla_str())
            self.assertEqual(players.online, player_setting.online)
            self.assertEqual(players.max, player_setting.max)
            self.assertSequenceEqual(players.names, player_setting.names)

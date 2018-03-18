"""High level client API."""

from collections import namedtuple
from logging import getLogger
from subprocess import PIPE, CalledProcessError, check_output

from mcipc.config import FORTUNE
from mcipc.rcon.proto import RequestIdMismatchError, RawClient


LOGGER = getLogger(__file__)


class OnlinePlayers(namedtuple('OnlinePlayers', ('online', 'max', 'players'))):
    """Online players information."""

    @classmethod
    def from_string(cls, string):
        """Creates the players information from the server response string."""
        header, *players = string.split(':')
        players = ':'.join(players).split(', ')
        players = [player for player in players if player]
        _, _, amount, _, _ = header.split()
        online, max_ = amount.split('/')
        return cls(int(online), int(max_), players)


class Client(RawClient):
    """A high-level RCON client."""

    @property
    def players(self):
        """Returns the players."""
        return OnlinePlayers.from_string(self.run('list'))

    def login(self, passwd):
        """Performs a login, returning False on failure."""
        try:
            return super().login(passwd)
        except RequestIdMismatchError:
            return False

    def say(self, message):
        """Broadcast a message to all players."""
        return self.run('say', message)

    def tell(self, player, message):
        """Whispers a message to the respective player."""
        return self.run('tell', player, message)

    def op(self, player):
        """Makes the respective player an operator."""
        return self.run('op', player)

    def deop(self, player):
        """Revokes operator status from the respective player."""
        return self.run('deop', player)

    def kick(self, player, *reasons):
        """Kicks the respective player."""
        return self.run('kick', player, *reasons)

    def tp(self, target_player, dst_player_or_coordinates, yaw_pitch=None):
        """Teleports players."""
        args = [str(target_player)]

        if isinstance(dst_player_or_coordinates, (tuple, list)):
            args += [str(coord) for coord in dst_player_or_coordinates]
        else:
            args += [str(dst_player_or_coordinates)]

        if yaw_pitch is not None:
            args += [str(item) for item in yaw_pitch]

        return self.run('tp', *args)

    def fortune(self, *fortune_options):
        """Sends a fortune to all players."""
        try:
            text = check_output((FORTUNE,) + fortune_options, stderr=PIPE)
        except CalledProcessError as called_process_error:
            if called_process_error.returncode == 127:
                LOGGER.error('%s is not available.', FORTUNE)
            else:
                LOGGER.error('Error running %s.', FORTUNE)
                LOGGER.debug(called_process_error.stderr.decode())

            return False

        LOGGER.debug('Fortune text:\n%s', text)
        return self.say(text)

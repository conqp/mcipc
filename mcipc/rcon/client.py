"""High level client API."""

from collections import namedtuple
from datetime import datetime
from locale import LC_TIME, getdefaultlocale, setlocale
from logging import getLogger
from subprocess import PIPE, CalledProcessError, check_output

from mcipc.config import FORTUNE
from mcipc.rcon.proto import RequestIdMismatchError, RawClient


LOGGER = getLogger(__file__)


def _fix_text(text):
    """Fixes text for ascii compliance."""

    return text.replace('\t', '        ')


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
        LOGGER.debug('Sending text: "%s".', message)
        return self.run('say', _fix_text(message))

    def tell(self, player, message):
        """Whispers a message to the respective player."""
        return self.run('tell', player, _fix_text(message))

    def mkop(self, player):
        """Makes the respective player an operator."""
        return self.run('op', player)

    def deop(self, player):
        """Revokes operator status from the respective player."""
        return self.run('deop', player)

    def kick(self, player, *reasons):
        """Kicks the respective player."""
        return self.run('kick', player, *reasons)

    def teleport(self, target_player, dst_player_or_coordinates, yaw_pitch=None):
        """Teleports players."""
        args = [str(target_player)]

        if isinstance(dst_player_or_coordinates, (tuple, list)):
            args += [str(coord) for coord in dst_player_or_coordinates]
        else:
            args += [str(dst_player_or_coordinates)]

        if yaw_pitch is not None:
            args += [str(item) for item in yaw_pitch]

        return self.run('tp', *args)

    def fortune(self, short=True, offensive=False):
        """Sends a fortune to all players."""
        args = []

        if short:
            args.append('-s')

        if offensive:
            args.append('-o')

        try:
            text = check_output([FORTUNE] + args, stderr=PIPE)
        except FileNotFoundError:
            LOGGER.error('%s is not available.', FORTUNE)
        except CalledProcessError as called_process_error:
            LOGGER.error('Error running %s.', FORTUNE)
            LOGGER.debug(called_process_error.stderr.decode())
        else:
            text = text.decode()
            LOGGER.debug('Fortune text:\n%s', text)
            return self.say(text)

        return False

    def datetime(self, frmt='%c'):
        """Tells all players the current datetime."""
        setlocale(LC_TIME, getdefaultlocale())  # Fix loacale.
        text = datetime.now().strftime(frmt)
        return self.say(text)

"""High level client API."""

from datetime import datetime
from json import dumps
from locale import LC_TIME, getdefaultlocale, setlocale
from logging import getLogger
from subprocess import PIPE, CalledProcessError, check_output

from mcipc.config import FORTUNE
from mcipc.rcon.proto import RequestIdMismatch, RawClient
from mcipc.rcon.datastructures import Location, Players, Seed


__all__ = ['Client', 'ExtendedClient']


_LOGGER = getLogger(__file__)
_PLAYER_OR_COORDS = TypeError('Must specify either dst_player or coords.')


def _tab_to_spaces(text):
    """Fixes text for better ingame chat console display."""

    return text.replace('\t', '        ')


class Client(RawClient):
    """A high-level RCON client."""

    @property
    def players(self):
        """Returns the players."""
        response = self.run('list')
        return Players.from_response(response)

    @property
    def seed(self):
        """Returns the server seed."""
        response = self.run('seed')
        return Seed.from_response(response)

    def login(self, passwd):
        """Performs a login, returning False on failure."""
        try:
            return super().login(passwd)
        except RequestIdMismatch:
            return False

    def say(self, message):
        """Broadcast a message to all players."""
        _LOGGER.debug('Sending text: "%s".', message)
        return self.run('say', _tab_to_spaces(message))

    def tell(self, player, message):
        """Whispers a message to the respective player."""
        return self.run('tell', player, _tab_to_spaces(message))

    def tellraw(self, player, obj):
        """Sends a message represented by a JSON-ish object."""
        return self.run('tellraw', player, dumps(obj))

    def mkop(self, player):
        """Makes the respective player an operator."""
        return self.run('op', player)

    def deop(self, player):
        """Revokes operator status from the respective player."""
        return self.run('deop', player)

    def kick(self, player, *reasons):
        """Kicks the respective player."""
        return self.run('kick', player, *reasons)

    def teleport(self, player, dst_player=None, coords=None, yaw_pitch=None):
        """Teleports players."""
        args = [str(player)]

        if dst_player is not None and coords is not None:
            raise _PLAYER_OR_COORDS
        elif dst_player is not None:
            args.append(str(dst_player))
        elif coords is not None:
            coord_x, coord_y, coord_z = coords
            args += [str(coord_x), str(coord_y), str(coord_z)]
        else:
            raise _PLAYER_OR_COORDS

        if yaw_pitch is not None:
            yaw, pitch = yaw_pitch
            args += [str(yaw), str(pitch)]

        return self.run('tp', *args)

    def locate(self, structure):
        """Locates the respective structure."""
        response = self.run('locate', str(structure))
        return Location.from_response(response)


class ExtendedClient(Client):
    """Client with some more extras."""

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
            _LOGGER.error('%s is not available.', FORTUNE)
        except CalledProcessError as called_process_error:
            _LOGGER.error('Error running %s.', FORTUNE)
            _LOGGER.debug(called_process_error.stderr.decode())
        else:
            text = text.decode()
            _LOGGER.debug('Fortune text:\n%s', text)
            return self.say(text)

        return False

    def datetime(self, frmt='%c'):
        """Tells all players the current datetime."""
        setlocale(LC_TIME, getdefaultlocale())  # Fix loacale.
        text = datetime.now().strftime(frmt)
        return self.say(text)

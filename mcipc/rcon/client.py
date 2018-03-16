"""High level client API."""

from collections import namedtuple

from mcipc.rcon.proto import RawClient


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

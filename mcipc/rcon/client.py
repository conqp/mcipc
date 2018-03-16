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

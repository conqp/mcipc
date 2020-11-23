"""High level client API."""

from json import dumps
from typing import Tuple

from mcipc.rcon.datastructures import Help, Location, Players, Seed
from mcipc.rcon.exceptions import NotALocation, StructureNotFound
from mcipc.rcon.proto import Client as _Client


__all__ = ['Client']


Coords = Tuple[float, float, float]
Orientation = Tuple[float, float]


class AdminMixin:
    """Administrative methods."""

    def deop(self, player: str) -> str:
        """Revokes operator status from the respective player."""
        return self.run('deop', player)

    def kick(self, player: str, *reasons: str) -> str:
        """Kicks the respective player."""
        return self.run('kick', player, *reasons)

    def mkop(self, player: str) -> str:
        """Makes the respective player an operator."""
        return self.run('op', player)

    def teleport(self, player: str, *,
                 dst_player: str = None,
                 coords: Coords = None,
                 orientation: Orientation = None) -> str:
        """Teleports the player to either another
        player or a set of coordinates.
        """
        args = [player]

        if sum(item is None for item in (dst_player, coords)) != 1:
            raise TypeError('Must specify either dst_player or coords.')

        if dst_player is not None:
            args.append(dst_player)
        elif coords is not None:
            x, y, z = coords    # pylint: disable=C0103
            args += [str(x), str(y), str(z)]

        if orientation is not None:
            yaw, pitch = orientation
            args += [str(yaw), str(pitch)]

        return self.run('tp', *args)

    tp = teleport   # Alias.


class ChatMixin:
    """Mixin provinding chat-related methods."""

    def me(self, message: str) -> str:  # pylint: disable=C0103
        """Sends a message from RCON in first-person perspective."""
        return self.run('me', message)

    def tell(self, player: str, message: str) -> str:
        """Whispers a message to the respective player."""
        return self.run('tell', player, message)

    w = msg = tell  # Aliases.

    def say(self, message: str) -> str:
        """Broadcast a message to all players."""
        return self.run('say', message)

    def tellraw(self, player: str, obj: dict) -> str:
        """Sends a message represented by a JSON-ish dict."""
        return self.run('tellraw', player, dumps(obj))

    def send_url(self, player: str, url: str, text: str = None) -> str:
        """Sends a URL to the specified player.
        If no text is specified, it will default to the original URL.
        """
        json = {
            'text': text or url,
            'clickEvent': {
                'action': 'open_url',
                'value': url
            }
        }
        return self.tellraw(player, json)


class InfoMixin:
    """Server information mixin."""

    @property
    def players(self) -> Players:
        """Returns the players."""
        response = self.run('list')
        return Players.from_response(response)

    @property
    def seed(self) -> Seed:
        """Returns the server seed."""
        response = self.run('seed')
        return Seed.from_response(response)

    def help(self, command: str = None) -> Help:
        """Returns help about commands."""
        if command is None:
            text = self.run('help')
        else:
            text = self.run('help', command)

        items = filter(None, text.split('/'))
        command_args = (item.split(maxsplit=1) for item in items)
        return Help.from_sequence(command_args)

    def locate(self, structure: str) -> Location:
        """Locates the respective structure."""
        response = self.run('locate', structure)

        try:
            return Location.from_response(response)
        except NotALocation:
            raise StructureNotFound(structure) from None


class Client(_Client, AdminMixin, ChatMixin, InfoMixin):
    """A high-level RCON client."""

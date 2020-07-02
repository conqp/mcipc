"""High level client API."""

from json import dumps

from mcipc.rcon.datastructures import Help, Location, Players, Seed
from mcipc.rcon.proto import Client as _Client


__all__ = ['Client']


class AdminMixin:
    """Administrative methods."""

    def deop(self, player: str) -> str:
        """Revokes operator status from the respective player."""
        return self.run('deop', player)

    def kick(self, player: str, *reasons) -> str:
        """Kicks the respective player."""
        return self.run('kick', player, *reasons)

    def mkop(self, player: str) -> str:
        """Makes the respective player an operator."""
        return self.run('op', player)

    def teleport(self, player: str, *, dst_player: str = None,
                 coords: tuple = None, orientation: tuple = None) -> str:
        """Teleports players."""
        args = [player]

        if sum(item is None for item in (dst_player, coords)) != 1:
            raise TypeError('Must specify either dst_player or coords.')

        if dst_player is not None:
            args.append(dst_player)
        elif coords is not None:
            coord_x, coord_y, coord_z = coords
            args += [str(coord_x), str(coord_y), str(coord_z)]

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

    def send_url(self, player: str, url: str, text: str = None) -> str:
        """Sends a URL to the specified player.
        If text is None, it will default to the original URL.
        """
        if text is None:
            text = url

        json = {
            'text': text,
            'clickEvent': {
                'action': 'open_url',
                'value': url
            }
        }
        return self.tellraw(player, json)

    def tellraw(self, player: str, obj: dict) -> str:
        """Sends a message represented by a JSON-ish dict."""
        return self.run('tellraw', player, dumps(obj))


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

    def help(self, command: str = None) -> tuple:
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
        return Location.from_response(response)


class Client(_Client, AdminMixin, ChatMixin, InfoMixin):
    """A high-level RCON client."""

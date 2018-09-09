"""High level client API."""

from json import dumps

from mcipc.rcon.datastructures import Location, Players, Seed
from mcipc.rcon.proto import Client as _Client


__all__ = ['Client']


_PLAYER_OR_COORDS = TypeError('Must specify either dst_player or coords.')


class Client(_Client):
    """A high-level RCON client."""

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

    def deop(self, player: str):
        """Revokes operator status from the respective player."""
        return self.run('deop', player)

    def kick(self, player: str, *reasons):
        """Kicks the respective player."""
        return self.run('kick', player, *reasons)

    def locate(self, structure: str) -> Location:
        """Locates the respective structure."""
        response = self.run('locate', str(structure))
        return Location.from_response(response)

    def mkop(self, player: str):
        """Makes the respective player an operator."""
        return self.run('op', player)

    def say(self, message: str):
        """Broadcast a message to all players."""
        return self.run('say', message)

    def send_url(self, player: str, url: str, text: str = None):
        """Sends a URL to the specified player.
        If text is None, it will default to the original URL.
        """
        if text is None:
            text = url

        json = {'text': text, 'clickEvent': {
            'action': 'open_url', 'value': url}}

        return self.tellraw(player, json)

    def teleport(self, player: str, *, dst_player: str = None,
                 coords: tuple = None, yaw_pitch: tuple = None):
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

    def tell(self, player: str, message: str):
        """Whispers a message to the respective player."""
        return self.run('tell', player, str(message))

    def tellraw(self, player: str, obj: dict):
        """Sends a message represented by a JSON-ish object."""
        return self.run('tellraw', player, dumps(obj))

"""Implementation of the kick command."""

from mcipc.rcon.client import Client
from mcipc.rcon.functions import parsed
from mcipc.rcon.response_types.kick import parse


__all__ = ['kick']


@parsed(parse)
def kick(self: Client, player: str, *reasons: str) -> str:
    """Kicks the respective player."""

    return self.run('kick', player, *reasons)

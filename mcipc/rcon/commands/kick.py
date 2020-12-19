"""Implementation of the kick command."""

from mcipc.rcon.proto import Client


__all__ = ['kick']


def kick(self: Client, player: str, *reasons: str) -> str:
    """Kicks the respective player."""

    return self.run('kick', player, *reasons)

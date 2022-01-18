"""Implementation of the music command."""

from typing import Optional

from mcipc.rcon.be.types import MusicRepeatMode
from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['MusicProxy', 'music']


class MusicProxy(CommandProxy):
    """Proxy for music commands."""

    def play(
            self,
            track_name: str,
            volume: Optional[float] = None,
            fade_seconds: Optional[float] = None,
            repeat_mode: Optional[MusicRepeatMode] = None
    ) -> str:
        """Plays the music track."""
        return self._run('play', track_name, volume, fade_seconds, repeat_mode)

    def queue(
            self,
            track_name: str,
            volume: Optional[float] = None,
            fade_seconds: Optional[float] = None,
            repeat_mode: Optional[MusicRepeatMode] = None
    ) -> str:
        """Add the music tracks to the queue."""
        return self._run('queue', track_name, volume, fade_seconds,
                         repeat_mode)

    def stop(self, fade_seconds: Optional[float] = None) -> str:
        """Stops the music."""
        return self._run('stop', fade_seconds)

    def volume(self, volume: float) -> str:
        """Adjusting the music volume."""
        return self._run('volume', volume)


def music(self: Client) -> MusicProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.be.commands.music.MusicProxy`
    """

    return MusicProxy(self, 'music')

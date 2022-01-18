"""Common weather proxy implementation."""

from typing import Optional

from mcipc.rcon.proxy import CommandProxy


__all__ = ['WeatherProxy']


class WeatherProxy(CommandProxy):
    """Proxy for weather commands."""

    def clear(self, duration: Optional[int] = None) -> str:
        """Sets the weather to clear."""
        return self._run('clear', duration)

    def rain(self, duration: Optional[int] = None) -> str:
        """Sets the weather to raining."""
        return self._run('rain', duration)

    def thunder(self, duration: Optional[int] = None) -> str:
        """Sets the weather to a thunderstorm."""
        return self._run('thunder', duration)

"""Common weather proxy implementation."""

from mcipc.rcon.proxy import CommandProxy


__all__ = ['WeatherProxy']


class WeatherProxy(CommandProxy):
    """Proxy for weather commands."""

    def clear(self, duration: int = None) -> str:
        """Sets the weather to clear."""
        return self._run('clear', duration)

    def rain(self, duration: int = None) -> str:
        """Sets the weahter to raining."""
        return self._run('rain', duration)

    def thunder(self, duration: int = None) -> str:
        """Sets the weather to a thunderstorm."""
        return self._run('thunder', duration)

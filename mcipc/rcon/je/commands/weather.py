"""Implementation of the weather command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['WeatherProxy', 'weather']


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


def weather(self: Client) -> WeatherProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.weather.WeatherProxy`
    """

    return WeatherProxy(self, 'weather')

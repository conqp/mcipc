"""Implementation of the weather command."""

from mcipc.rcon.client import Client
from mcipc.rcon.commands.weather import WeatherProxy


__all__ = ['WeatherProxy', 'weather']


class WeatherProxy(WeatherProxy):   # pylint: disable=E0102
    """Proxy for weather commands."""

    def query(self) -> str:
        """Queries the current weather."""
        return self._run('query')


def weather(self: Client) -> WeatherProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.be.commands.weather.WeatherProxy`
    """

    return WeatherProxy(self, 'weather')

"""Implementation of the weather command."""

from mcipc.rcon.client import Client
from mcipc.rcon.commands.weather import WeatherProxy


__all__ = ['WeatherProxy', 'weather']


def weather(self: Client) -> WeatherProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.weather.WeatherProxy`
    """

    return WeatherProxy(self, 'weather')

"""Implementation of the time command."""

from typing import Union

from mcipc.rcon.client import Client
from mcipc.rcon.je.types import Time, TimeSpec
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import TimeType


__all__ = ['TimeProxy', 'time']


class TimeProxy(CommandProxy):
    """Proxy for time commands."""

    # pylint: disable=W0621
    def add(self, time: Time) -> str:
        """Adds time."""
        return self._run('add', time)

    def query(self, time_type: TimeType) -> str:
        """Queries the given time type."""
        return self._run('query', time_type)

    def set(self, time: Union[TimeSpec, Time]) -> str:
        """Sets the time to the given amount."""
        return self._run('set', time)


def time(self: Client) -> TimeProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.time.TimeProxy`
    """

    return TimeProxy(self, 'time')

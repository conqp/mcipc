"""Implementation of the schedule command."""

from mcipc.rcon.client import Client
from mcipc.rcon.je.types import ScheduleMode, Time
from mcipc.rcon.proxy import CommandProxy


__all__ = ['ScheduleProxy', 'schedule']


class ScheduleProxy(CommandProxy):
    """Proxy for schedule sub-commands."""

    def function(self, function: str, time: Time,
                 mode: ScheduleMode = None) -> str:
        """Adds a schedule."""
        return self._run('function', function, time, mode)

    def clear(self, function: str) -> str:
        """Removes a schedule."""
        return self._run('clear', function)


def schedule(self: Client) -> ScheduleProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.schedule.ScheduleProxy`
    """

    return ScheduleProxy(self, 'schedule')

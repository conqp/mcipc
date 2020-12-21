"""Implementation of the schedule command."""

from pathlib import Path

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import Vec3


__all__ = ['ScheduleProxy', 'schedule']


class ScheduleProxy(CommandProxy):
    """Proxy for schedule-related commands."""

    # pylint: disable=C0103
    def __call__(self, from_: Vec3, to: Vec3, function: Path) -> str:
        """Adds a schedule."""
        return self._run(from_, to, function)

    def circle(self, center: Vec3, radius: int, function: Path) -> str:
        """Adds a circle."""
        return self._run('circle', center, radius, function)

    def tickingarea(self, name: str, function: Path) -> str:
        """Adds a ticking ares."""
        return self._run('tickingarea', name, function)


def schedule(self: Client) -> ScheduleProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.be.commands.schedule.ScheduleProxy`
    """

    return ScheduleProxy(self, 'schedule', 'on_area_loaded', 'add')

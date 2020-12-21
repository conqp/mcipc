"""Implementes the tickingarea command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import Vec3


__all__ = ['AddProxy', 'TickingareaProxy', 'tickingarea']


class AddProxy(CommandProxy):
    """Proxy for add comamnds."""

    # pylint: disable=C0103
    def __call__(self, from_: Vec3, to: Vec3, name: str = None) -> str:
        """Adds a ticking area based on locations."""
        return self._run(from_, to, name)

    def circle(self, center: Vec3, radius: int, name: str = None) -> str:
        """Adds a ticking area in a circle."""
        return self._run('circle', center, radius, name)


class TickingareaProxy(CommandProxy):
    """Proxy for tickingarea commands."""

    def add(self) -> AddProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.be.commands.tickingarea.AddProxy`
        """
        return self._proxy(AddProxy, 'add')

    def remove(self, *, name: str = None, position: Vec3 = None) -> str:
        """Removes a ticking ares."""
        if name is None and position is None:
            return self._run('remove_all')

        if name is not None:
            return self._run('remove', name)

        return self._run('remove', position)

    def list(self, all_dimensions: bool = False) -> str:
        """Lists ticking areas."""
        return self._run('list', 'all-dimensions' if all_dimensions else None)


def tickingarea(self: Client) -> TickingareaProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.be.commands.tickingarea.TickingareaProxy`
    """

    return TickingareaProxy(self, 'tickingarea')

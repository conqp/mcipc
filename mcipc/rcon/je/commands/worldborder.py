"""Implementation of the worldborder command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import Vec2


__all__ = ['DamageProxy', 'WarningProxy', 'WorldborderProxy', 'worldborder']


class DamageProxy(CommandProxy):
    """Proxy for damage commands."""

    def amount(self, damage_per_block: float) -> str:
        """Sets the amount of damage per block."""
        return self._run('amount', damage_per_block)

    def buffer(self, distance: float) -> str:
        """Sets the distance for the damage buffer."""
        return self._run('buffer', distance)


class WarningProxy(CommandProxy):
    """Proxy for warning commands."""

    def distance(self, distance: int) -> str:
        """Sets the warning distance."""
        return self._run('distance', distance)

    def time(self, time: int) -> str:
        """Sets the warning time."""
        return self._run('time', time)


class WorldborderProxy(CommandProxy):
    """Proxy for worldborder commands."""

    def add(self, distance: float, time: int = None) -> str:
        """Adds a world border."""
        return self._run('add', distance, time)

    def center(self, pos: Vec2) -> str:
        """Sets the center of the world border."""
        return self._run('center', pos)

    @property
    def damage(self) -> DamageProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.worldborder.DamageProxy`
        """
        return self._proxy(DamageProxy, 'damage')

    def get(self) -> str:
        """Returns information about the world border."""
        return self._run('get')

    def set(self, distance: float, time: int = None) -> str:
        """Sets the world border."""
        return self._run('set', distance, time)

    @property
    def warning(self) -> WarningProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.worldborder.WarningProxy`
        """
        return self._proxy(WorldborderProxy, 'warning')


def worldborder(self: Client) -> WorldborderProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.worldborder.WorldborderProxy`
    """

    return WorldborderProxy(self, 'worldborder')

"""Implementation of the bossbar command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import Attribute, Color, Style


__all__ = ['BossbarProxy', 'BossbarSetProxy', 'bossbar']


class BossbarSetProxy(CommandProxy):
    """Proxy to handle boss bar set commands."""

    def color(self, color: Color) -> str:
        """Set the text color (if no color was specified
        as part of a text component) and bar color.
        Defaults to white upon creation.
        """
        return self._run('color', color)

    def max(self, max: int) -> str:     # pylint: disable=W0622
        """Set the boss bar's maximum value. Defaults to 100 upon creation."""
        return self._run('max', max)

    def name(self, name: str) -> str:   # pylint: disable=W0622
        """Set the boss bar's name."""
        return self._run('name', name)

    def players(self, *targets: str) -> str:
        """Change the set of players to whom the bar is visible.
        Defaults to none upon creation.
        """
        return self._run('players', *targets)

    def style(self, style: Style) -> str:
        """Set the boss bar's visual amount of segments.
        Defaults to progress upon creation.
        """
        return self._run('style', style)

    def value(self, value: int) -> str:
        """Set the boss bar's current value.
        Defaults to 0 upon creation.
        """
        return self._run('value', value)

    def visible(self, visible: bool) -> str:
        """Set the boss bar's visibility.
        Defaults to true upon creation.
        """
        return self._run('visible', visible)


# pylint: disable=W0622,C0103
class BossbarProxy(CommandProxy):
    """Proxy for boss bar methods."""

    def add(self, id: str, name: dict) -> str:
        """Create a new boss bar."""
        return self._run('add', id, name)

    def get(self, id: str, attribute: Attribute) -> str:
        """Return the requested setting as a result of the command."""
        return self._run('get', id, attribute)

    def list(self) -> str:
        """Display a list of existing boss bars."""
        return self._run('list')

    def remove(self, id: str) -> str:
        """Remove an existing bossbar."""
        return self._run('remove', id)

    def set(self, id: str, attribute: Attribute) -> BossbarSetProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.bossbar.BossbarSetProxy`
        """
        return self._proxy(BossbarSetProxy, 'set', id, attribute)


def bossbar(self: Client) -> BossbarProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.bossbar.BossbarProxy`
    """

    return BossbarProxy(self, 'bossbar')

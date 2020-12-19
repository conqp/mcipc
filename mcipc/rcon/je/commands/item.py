"""Implementation of the item command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import Vec3


__all__ = ['item']


class CopyProxy(CommandProxy):
    """Proxy for item copy commands."""

    def block(self, pos: Vec3, slot: str, modifier: str = None) -> str:
        """Copies a block."""
        return self._run('block', pos, slot, modifier)

    def entity(self, targets: str, slot: str, modifier: str = None) -> str:
        """Copies an entity."""
        return self._run('entity', targets, slot, modifier)


class ItemSubProxy(CommandProxy):
    """Sub-proxy for block and entity related commands."""

    @property
    def copy(self) -> CopyProxy:
        """Delegates to the copy proxy."""
        return self._proxy(CopyProxy, 'copy')

    def modify(self, modifier: str) -> str:
        """Modifies the item."""
        return self._run('modify', modifier)

    # pylint: disable=W0621
    def replace(self, item: str, count: int = None) -> str:
        """Replaces an item."""
        return self._run('replace', item, count)


class ItemProxy(CommandProxy):
    """Proxy for item-related commands."""

    def block(self, pos: Vec3, slot: str) -> ItemSubProxy:
        """Delegates to a sub-proxy."""
        return self._proxy(ItemSubProxy, 'block', pos, slot)

    def entity(self, targets: str, slot: str) -> ItemSubProxy:
        """Delegates to a sub-proxy."""
        return self._proxy(ItemSubProxy, 'entity', targets, slot)


def item(self: Client) -> ItemProxy:
    """Delegates to a sub-proxy."""

    return ItemProxy(self, 'item')

"""Implementation of the replaceitem command."""

from mcipc.rcon.be.types import EntityEquipmentSlot, ReplaceMode
from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import Vec3


__all__ = ['ReplaceitemProxy', 'replaceitem']


class ReplaceitemProxy(CommandProxy):
    """Proxy for replaceitem related commands."""

    # pylint: disable=R0913
    def block(self, position: Vec3, slot_id: int, item_name: str,
              amount: int = None, data: int = None, components: dict = None,
              *, old_item_handling: ReplaceMode = None) -> str:
        """Replaces a block."""
        command = ['block', position, 'slot.container', slot_id]

        if old_item_handling is not None:
            command.append(old_item_handling)

        return self._run(*command, item_name, amount, data, components)

    def entity(self, target: str, slot_type: EntityEquipmentSlot, slot_id: int,
               item_name: str, amount: int = None, data: int = None,
               components: dict = None, *,
               old_item_handling: ReplaceMode = None) -> str:
        """Replaces an item."""
        command = ['entity', target, slot_type, slot_id]

        if old_item_handling is not None:
            command.append(old_item_handling)

        return self._run(*command, item_name, amount, data, components)


def replaceitem(self: Client) -> ReplaceitemProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.be.commands.replaceitem.ReplaceitemProxy`
    """

    return ReplaceitemProxy(self, 'replaceitem')

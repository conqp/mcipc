"""Implementation of the enchant command."""

from mcipc.rcon.je.types import Enchantment
from mcipc.rcon.proto import Client


__all__ = ['enchant']


def enchant(self: Client, target: str, enchantment: Enchantment,
            level: int = None) -> str:
    """Enchants the target."""

    return self.run('enchant', target, enchantment, level)

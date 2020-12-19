"""Implementation of the enchant command."""

from mcipc.rcon.client import Client
from mcipc.rcon.je.types import Enchantment


__all__ = ['enchant']


def enchant(self: Client, target: str, enchantment: Enchantment,
            level: int = None) -> str:
    """Enchants the target."""

    return self.run('enchant', target, enchantment, level)

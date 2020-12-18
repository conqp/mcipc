"""Implementation of the enchant command."""

from mcipc.rcon.proto import Client
from mcipc.rcon.types import Enchantment


__all__ = ['enchant']


def enchant(self: Client, target: str, enchantment: Enchantment,
            level: int = None) -> str:
    """Enchants the target."""

    return self.run('enchant', target, enchantment, level)

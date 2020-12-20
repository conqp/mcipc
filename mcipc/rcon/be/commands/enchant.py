"""Implementation of the enchant command."""

from typing import Union

from mcipc.rcon.be.types import Enchantment
from mcipc.rcon.client import Client


__all__ = ['enchant']


def enchant(self: Client, player: str, enchantment: Union[Enchantment, int],
            level: int = None) -> str:
    """Enchants the given player."""

    return self.run('enchant', player, enchantment, level)

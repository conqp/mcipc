"""Implementation of the ability command."""

from mcipc.rcon.client import Client
from mcipc.rcon.types import Ability


__all__ = ['ability']


# pylint: disable=W0621
def ability(self: Client, player: str, ability: Ability = None,
            value: bool = None) -> str:
    """Sets or queries player with a specific ability."""

    return self.run('ability', player, ability, value)

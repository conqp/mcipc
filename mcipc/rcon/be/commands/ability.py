"""Implementation of the ability command."""

from typing import Optional

from mcipc.rcon.client import Client
from mcipc.rcon.types import Ability


__all__ = ['ability']


# pylint: disable=W0621
def ability(
        self: Client,
        player: str,
        ability: Optional[Ability] = None,
        value: Optional[bool] = None
) -> str:
    """Sets or queries player with a specific ability."""

    return self.run('ability', player, ability, value)

"""Implementation of the teleport / tp command."""

from typing import Union

from mcipc.rcon.client import Client
from mcipc.rcon.types import Vec3


__all__ = ['teleport']


def teleport(self: Client, player: str,
             dst_player_or_coords: Union[str, Vec3] = None,
             orientation: Vec3 = None) -> str:
    """Teleports the player to either another
    player or a set of coordinates.
    """

    return self.run('tp', player, dst_player_or_coords, orientation)

"""Implementation of the summon command."""

from typing import Optional

from mcipc.rcon.client import Client
from mcipc.rcon.types import Vec3


__all__ = ['summon']


def summon(
        self: Client,
        entity: str,
        pos: Optional[Vec3] = None,
        nbt: Optional[dict] = None
) -> str:
    """Summons an entity."""

    return self.run('summon', entity, pos, nbt)

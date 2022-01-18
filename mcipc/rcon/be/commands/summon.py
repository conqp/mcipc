"""Implementation of the summon command."""

from typing import Optional

from mcipc.rcon.client import Client
from mcipc.rcon.types import Vec3


__all__ = ['summon']


def summon(
        self: Client,
        entity_type: str,
        spawn_pos: Optional[Vec3] = None,
        spawn_event: Optional[str] = None,
        name_tag: Optional[str] = None
) -> str:
    """Summons an entity."""

    command = ['summon', entity_type]

    if name_tag is not None and spawn_event is None:
        command += [name_tag, spawn_pos]
    else:
        command += [spawn_pos, spawn_event, name_tag]

    return self.run(*command)

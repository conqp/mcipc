"""Implementation of the teleport command."""

from typing import Optional

from mcipc.rcon.client import Client
from mcipc.rcon.types import Anchor, Rotation, Vec3


__all__ = ['teleport']


def teleport(
        self: Client,
        *,
        destination: Optional[str] = None,
        location: Optional[Vec3] = None,
        targets: Optional[str] = None,
        rotation: Optional[Rotation] = None,
        facing_location: Optional[Vec3] = None,
        facing_entity: Optional[str] = None,
        facing_anchor: Optional[Anchor] = None
) -> str:
    """Teleports the player."""

    command = ['teleport']

    if targets is not None:
        command.append(targets)

        if location is not None:
            command.append(location)

            if rotation is not None:
                command.append(rotation)
            elif facing_location is not None:
                command += ['facing', facing_location]
            elif facing_entity is not None:
                command += ['facing', 'entity', facing_entity, facing_anchor]
        elif destination is not None:
            command.append(destination)
        else:
            raise TypeError('Must specify either destination or location.')
    elif destination is not None:
        command.append(destination)
    elif location is not None:
        command.append(location)
    else:
        raise TypeError('Must specify destination, location or targets.')

    return self.run(*command)

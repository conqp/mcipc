"""Implementation of the teleport command."""

from mcipc.rcon.client import Client
from mcipc.rcon.types import Anchor, Rotation, Vec3


__all__ = ['teleport']


def teleport(self: Client, *, destination: str = None, location: Vec3 = None,
             targets: str = None, rotation: Rotation = None,
             facing_location: Vec3 = None, facing_entity: str = None,
             facing_anchor: Anchor = None) -> str:
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

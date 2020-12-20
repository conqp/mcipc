"""Implementation of the teleport command."""

from typing import Union

from mcipc.rcon.be.types import RelativeFloat
from mcipc.rcon.client import Client
from mcipc.rcon.types import Vec3


__all__ = ['teleport']


def extend_command(look_at_position: Vec3, look_at_entity: str,
                   y_rot: RelativeFloat, x_rot: RelativeFloat,
                   check_for_blocks: bool):
    """Extends the command with common sub commands."""

    if look_at_position is not None:
        yield'facing'
        yield look_at_position
    elif look_at_entity is not None:
        yield 'facing'
        yield look_at_entity
    else:
        if y_rot is not None:
            yield y_rot

        if x_rot is not None:
            yield x_rot

    yield check_for_blocks


def teleport(self: Client, *, destination: Union[Vec3, str] = None,
             victim: str = None, check_for_blocks: bool = None,
             y_rot: RelativeFloat = None, x_rot: RelativeFloat = None,
             look_at_position: Vec3 = None, look_at_entity: str = None) -> str:
    """Teleports the player."""

    command = ['teleport']

    if victim is not None:
        if destination is None:
            raise TypeError('Must spectify destination on victim.')

        command += [victim, destination, *extend_command(
            look_at_position, look_at_entity, y_rot, x_rot, check_for_blocks)]

    elif destination is not None:
        command += [destination, *extend_command(
            look_at_position, look_at_entity, y_rot, x_rot, check_for_blocks)]
    else:
        raise TypeError('Must specify either destination or victim.')

    return self.run(*command)

"""Implementation of the particle command."""

from mcipc.rcon.client import Client
from mcipc.rcon.je.types import ParticleMode
from mcipc.rcon.types import Vec3


__all__ = ['particle']


# pylint: disable=R0913
def particle(self: Client, name: str, speed: float, count: int,
             parameters: str = None, pos: Vec3 = None, delta: Vec3 = None,
             mode: ParticleMode = None, viewers: str = None) -> str:
    """Creates the respective particles."""

    args = ['particle', name]

    if parameters is not None:
        args.append(parameters)

    if pos is not None:
        args.append(pos)

        if delta is not None:
            args.append(delta)

    return self.run(*args, speed, count, mode, viewers)

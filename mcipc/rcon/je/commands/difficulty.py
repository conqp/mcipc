"""Implementation of the difficulty command."""

from mcipc.rcon.client import Client
from mcipc.rcon.functions import parsed
from mcipc.rcon.response_types.difficulty import parse
from mcipc.rcon.types import Difficulty


__all__ = ['difficulty']


# pylint: disable=W0621
@parsed(parse)
def difficulty(self: Client, difficulty: Difficulty) -> bool:
    """Sets the difficulty."""

    return self.run('difficulty', difficulty)

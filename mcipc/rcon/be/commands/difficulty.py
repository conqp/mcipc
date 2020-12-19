"""Implementation of the difficulty command."""

from typing import Union

from mcipc.rcon.client import Client
from mcipc.rcon.types import Difficulty


__all__ = ['difficulty']


# pylint: disable=W0621
def difficulty(self: Client, difficulty: Union[Difficulty, int]) -> str:
    """Sets the difficulty."""

    return self.run('difficulty', difficulty)

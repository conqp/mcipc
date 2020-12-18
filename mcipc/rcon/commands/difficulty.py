"""Difficulty setting."""

from mcipc.rcon.functions import boolmap
from mcipc.rcon.proto import Client
from mcipc.rcon.types import Difficulty


__all__ = ['difficulty']


SET = 'The difficulty has been set to (\\w+)'
UNCHANGED = 'The difficulty did not change; it is already set to (\\w+)'


# pylint: disable=W0621
def difficulty(self: Client, difficulty: Difficulty) -> bool:
    """Sets the difficulty."""

    text = self.run('difficulty', difficulty)
    return boolmap(text, SET, UNCHANGED)

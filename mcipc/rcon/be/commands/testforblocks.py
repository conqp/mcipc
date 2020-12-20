"""Implements the testforblocks command."""

from mcipc.rcon.be.types import MatchMode
from mcipc.rcon.client import Client
from mcipc.rcon.types import Vec3


__all__ = ['testforblocks']


def testforblocks(self: Client, begin: Vec3, end: Vec3, destination: Vec3,
                  match_mode: MatchMode = None) -> str:
    """Tests whether the blocks in two regions match."""

    return self.run('testforblocks', begin, end, destination, match_mode)

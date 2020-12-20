"""Implementation of the testfor command."""

from mcipc.rcon.client import Client


__all__ = ['testfor']


def testfor(self: Client, victim: str) -> str:
    """Counts entities matching specified conditions."""

    return self.run('testfor', victim)

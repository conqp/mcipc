"""Operators management."""

from mcipc.rcon.client import Client


__all__ = ['deop', 'op']


def deop(self: Client, player: str) -> str:
    """Revokes operator status from the respective player."""

    return self.run('deop', player)


def op(self: Client, player: str) -> str:     # pylint: disable=C0103
    """Makes the respective player an operator."""

    return self.run('op', player)

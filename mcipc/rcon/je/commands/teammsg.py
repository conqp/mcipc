"""Implementation of the teammsg and tm commands."""

from mcipc.rcon.client import Client


__all__ = ['teammsg', 'tm']


def teammsg(self: Client, message: str) -> str:
    """Sends a team message."""

    return self.run('teammsg', message)


def tm(self: Client, message: str) -> str:  # pylint: disable=C0103
    """Sends a team message."""

    return self.run('tm', message)

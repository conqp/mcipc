"""Implementation of the code command."""

from mcipc.rcon.client import Client


__all__ = ['code']


def code(self: Client) -> str:
    """Used to access code connection."""

    return self.run('code')

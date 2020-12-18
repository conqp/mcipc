"""Code connection."""

from mcipc.rcon.proto import Client


__all__ = ['code']


def code(self: Client) -> str:
    """Used to access code connection."""

    return self.run('code')

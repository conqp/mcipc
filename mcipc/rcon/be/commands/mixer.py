"""Implementation of the mixer command."""

from mcipc.rcon.client import Client


__all__ = ['mixer']


def mixer(self: Client) -> str:
    """Mixer control."""

    raise NotImplementedError()

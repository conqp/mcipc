"""Implementation of the kill command."""

from mcipc.rcon.proto import Client


__all__ = ['kill']


def kill(self: Client, targets: str):
    """Kills the targets."""

    return self.run('kill', targets)

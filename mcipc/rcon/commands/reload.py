"""Implementation of the reload command."""

from mcipc.rcon.proto import Client


__all__ = ['reload']


def reload(self: Client) -> str:
    """Reloads data packs in Java Edition and functions
    in behavior packs in Bedrock Edition.
    """

    return self.run('reload')

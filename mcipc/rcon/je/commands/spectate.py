"""Implementation of the spectate command."""

from typing import Optional

from mcipc.rcon.client import Client


__all__ = ['spectate']


def spectate(
        self: Client,
        target: Optional[str] = None,
        player: Optional[str] = None
) -> str:
    """Start or stop spectating."""

    return self.run('spectate', target, player)

"""Implementation of the mobevent command."""

from typing import Optional

from mcipc.rcon.client import Client


__all__ = ['mobevent']


def mobevent(self: Client, event: str, value: Optional[bool] = None) -> str:
    """Controls or queries what mob events are allowed to run."""

    return self.run('mobevent', event, value)

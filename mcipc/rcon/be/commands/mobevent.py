"""Implementation of the mobevent command."""

from mcipc.rcon.client import Client


__all__ = ['mobevent']


def mobevent(self: Client, event: str, value: bool = None) -> str:
    """Controls or queries what mob events are allowed to run."""

    return self.run('mobevent', event, value)

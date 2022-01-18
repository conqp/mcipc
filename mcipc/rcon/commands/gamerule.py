"""Implementation of th gamerule command."""

from typing import Optional, Union

from mcipc.rcon.client import Client


__all__ = ['gamerule']


def gamerule(
        self: Client,
        rule: str,
        value: Optional[Union[bool, int]] = None
) -> str:
    """Sets or queries a game rule value."""

    return self.run('gamerule', rule, value)

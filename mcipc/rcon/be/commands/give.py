"""Implementation of the give command."""

from typing import Optional

from mcipc.rcon.client import Client


__all__ = ['give']


def give(
        self: Client,
        target: str,
        item: str,
        amount: Optional[int] = None,
        data: Optional[int] = None,
        components: Optional[dict] = None
) -> str:
    """Gives an item to one or more players."""

    return self.run(target, item, amount, data, components)

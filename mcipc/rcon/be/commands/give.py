"""Implementation of the give command."""

from mcipc.rcon.proto import Client


__all__ = ['give_be']


def give(self: Client, target: str, item: str, amount: int = None,
         data: int = None, components: dict = None) -> str:
    """Gives an item to one or more players."""

    return self.run(target, item, amount, data, components)

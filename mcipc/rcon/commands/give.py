"""Implementation of the give command."""

from mcipc.rcon.proto import Client


__all__ = ['give_be', 'give_je']


# pylint: disable=R0913
def give_be(self: Client, target: str, item: str, amount: int = None,
            data: int = None, components: dict = None) -> str:
    """Gives an item to one or more players."""

    return self.run(target, item, amount, data, components)


def give_je(self: Client, target: str, item: str, count: int = None) -> str:
    """Gives an item to one or more players."""

    return give_be(self, target, item, count)

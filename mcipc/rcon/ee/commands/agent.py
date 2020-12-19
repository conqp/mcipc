"""Agent-related commands."""

from mcipc.rcon.client import Client
from mcipc.rcon.types import Direction


__all__ = [
    'collect',
    'createagent',
    'destroy',
    'detect',
    'detectredstone',
    'dropall',
    'move',
    'remove',
    'tpagent',
    'transfer',
    'turn'
]


def collect(self: Client, item: str) -> str:
    """Lets your agent collect all items within
    a one block from Agent in three dimensions.
    """

    return self.run('collect', item)


def createagent(self: Client) -> str:
    """Creates an Agent at the current player's position."""

    return self.run('createagent')


def destroy(self: Client, direction: Direction) -> str:
    """Makes your agent destroy a block or item in the specified direction."""

    return self.run('destroy', direction)


def detect(self: Client, direction: Direction) -> str:
    """Lets your agent detect if there is a
    collidable block in the specified direction.
    """

    return self.run('detect', direction)


def detectredstone(self: Client, direction: Direction) -> str:
    """Lets your agent detect a redstone signal in the specified direction."""

    return self.run('detectredstone', direction)


def dropall(self: Client, direction: Direction) -> str:
    """Makes an agent drop all its items from all slots
    onto the ground by one block in the specified direction.
    """

    return self.run('dropall', direction)


def move(self: Client, direction: Direction) -> str:
    """Moves an Agent in a specified direction."""

    return self.run('move', direction)


def remove(self: Client, target: str) -> str:
    """Removes an agent."""

    return self.run('remove', target)


def tpagent(self: Client) -> str:
    """Teleport the player to their Agent's position."""

    return self.run('tpagent')


def transfer(self: Client, src_slot_num: int, quantity: int,
             dst_slot_num: int) -> str:
    """Transfers a specified quantity of items from
    one slot to another of your Agent's inventory.
    """

    return self.run('transfer', src_slot_num, quantity, dst_slot_num)


def turn(self: Client, direction: Direction) -> str:
    """Rotates an Agent in a specified direction by 90 degrees."""

    return self.run('turn', direction)

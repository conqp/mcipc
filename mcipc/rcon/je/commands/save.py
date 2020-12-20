"""Implementation of the save-* commands."""

from mcipc.rcon.client import Client


__all__ = ['save_all', 'save_off', 'save_on']


def save_all(self: Client, flush: bool = False) -> str:
    """Saves the server to the data storage device."""

    return self.run('save-all', 'flush' if flush else None)


def save_off(self: Client) -> str:
    """Disables the server writing to the world files."""

    return self.run('save-off')


def save_on(self: Client) -> str:
    """Enables the server writing to the world files."""

    return self.run('save-on')

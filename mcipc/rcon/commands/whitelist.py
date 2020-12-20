"""Implementation of the whitelist command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['whitelist']


class WhitelistProxy(CommandProxy):
    """Proxy for whitelist commands."""

    def add(self, name: str) -> str:
        """Adds a player to the whitelist."""
        return self._run('add', name)

    def list(self) -> str:
        """Lists the whitelist."""
        return self._run('list')

    def off(self) -> str:
        """Turns the whitelist checking off."""
        return self._run('off')

    def on(self) -> str:
        """Turns the whitelist checking on."""
        return self._run('on')

    def reload(self) -> str:
        """Reloads the whitelist from the file."""
        return self._run('reload')

    def remove(self, name: str) -> str:
        """Removes a player from the whitelist."""
        return self._run('remove', name)


def whitelist(self: Client) -> str:
    """Delegates to a command proxy."""

    return WhitelistProxy(self, 'whitelist')

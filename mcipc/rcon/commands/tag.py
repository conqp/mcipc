"""Implementation of the tag command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['TagProxy', 'tag']


class TagProxy(CommandProxy):
    """Proxy for tag commands."""

    def add(self, name: str) -> str:
        """Adds a tag."""
        return self._run('add', name)

    def list(self) -> str:
        """Lists tags."""
        return self._run('list')

    def remove(self, name: str) -> str:
        """Removes a tag."""
        return self._run('remove', name)


def tag(self: Client, targets: str) -> TagProxy:
    """Delegates to a command proxy."""

    return TagProxy(self, 'tag', targets)

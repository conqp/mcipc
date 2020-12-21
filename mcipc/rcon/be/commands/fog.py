"""Implementation of the fog command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['FogProxy', 'fog']


class FogProxy(CommandProxy):
    """Proxy for fog-related commands."""

    def push(self, fog_id: str, user_provided_id: str) -> str:
        """Adds the respective fog."""
        return self._run('push', fog_id, user_provided_id)

    def pop(self, user_provided_id: str) -> str:
        """Pops the respective fog."""
        return self._run('pop', user_provided_id)

    def remove(self, user_provided_id: str) -> str:
        """Remove the respective fog."""
        return self._run('remove', user_provided_id)


def fog(self: Client, victim: str) -> FogProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.be.commands.fog.Proxy`
    """

    return FogProxy(self, 'fog', victim)

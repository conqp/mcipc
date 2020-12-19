"""Implementation of the event command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['event']


class EventProxy(CommandProxy):     # pylint: disable=R0903
    """Proxies event-related commands."""

    def entity(self, target: str, event_name: str) -> str:
        """Triggers an event on an entity."""
        return self._run('entity', target, event_name)


def event(self: Client) -> EventProxy:
    """Returns aproxy for event-related sub commands."""

    return EventProxy(self, 'event')

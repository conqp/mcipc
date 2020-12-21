"""Implementation of the trigger command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['TriggerProxy', 'trigger']


class TriggerProxy(CommandProxy):
    """Proxy for trigger commands."""

    def __call__(self, objective: str) -> str:
        """Adds 1 to the current value of <objective>."""
        return self._run('objective')

    def add(self, objective: str, value: int) -> str:
        """Adds <value> to the current value of <objective>."""
        return self._run('add', objective, value)

    def set(self, objective: str, value: int) -> str:
        """Sets the value of <objective> to <value>."""
        return self._run('set', objective, value)


def trigger(self: Client) -> TriggerProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.trigger.TriggerProxy`
    """

    return TriggerProxy(self, 'trigger')

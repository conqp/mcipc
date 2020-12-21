"""Implementation of the advancement command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['AdvancementProxy', 'AdvancementSubProxy', 'advancement']


class AdvancementSubProxy(CommandProxy):
    """Sub-proxy for advancement-related commands."""

    def everything(self) -> str:
        """Grants or revokes everyting."""
        return self._run('everything')

    # pylint: disable=W0621
    def only(self, advancement: str, criterion: str = None) -> str:
        """Only grants or revokes the given advancement."""
        return self._run(advancement, criterion)

    def from_(self, advancement: str) -> str:
        """Grants or revokes from the given advancement."""
        return self._run('from', advancement)

    def through(self, advancement: str) -> str:
        """Grants or revokes through the given advancement."""
        return self._run('through', advancement)

    def until(self, advancement: str) -> str:
        """Grants or revokes until the given advancement."""
        return self._run('until', advancement)


class AdvancementProxy(CommandProxy):
    """Proxy for advancements-related commands."""

    def grant(self, targets: str) -> AdvancementSubProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.advancement.AdvancementSubProxy`
        """
        return self._proxy(AdvancementSubProxy, 'grant', targets)

    def revoke(self, targets: str) -> AdvancementSubProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.advancement.AdvancementSubProxy`
        """
        return self._proxy(AdvancementSubProxy, 'revoke', targets)


def advancement(self: Client) -> AdvancementProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.advancement.AdvancementProxy`
    """

    return AdvancementProxy(self, 'advancement')

"""Implementation of the advancement command."""

from mcipc.rcon.proto import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['advancement']


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
        """Returns a proxy for the grant command."""
        return self._proxy(AdvancementSubProxy, 'grant', targets)

    def revoke(self, targets: str) -> AdvancementSubProxy:
        """Returns a proxy for the revoke command."""
        return self._proxy(AdvancementSubProxy, 'revoke', targets)


def advancement(self: Client) -> AdvancementProxy:
    """Returns a proxy for sub-commands."""

    return AdvancementProxy(self, 'advancement')

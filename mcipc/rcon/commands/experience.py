"""Implementation of the experience command."""

from mcipc.rcon.proto import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import XPUnit


__all__ = ['experience', 'xp_be', 'xp_je']


class ExperienceProxy(CommandProxy):
    """Proxy for Experience commands."""

    def add(self, targets: str, amount: int, unit: XPUnit = None) -> str:
        """Gives the target the specified amount of XP units."""
        return self._run('add', targets, amount, unit)

    def set(self, targets: str, amount: int, unit: XPUnit = None) -> str:
        """Sets the XP of the target to the specified amount and units."""
        return self._run('set', targets, amount, unit)

    def query(self, targets: str, amount: int, unit: XPUnit) -> str:
        """Queries the amount in given unit of XP of the targets."""
        return self._run('query', targets, amount, unit)


def experience(self: Client) -> ExperienceProxy:
    """Delegates to a command proxy."""

    return ExperienceProxy(self, 'experience')


def xp_be(self: Client, amount: int, player: str) -> str:
    """Gives the player the specified amount of XP."""

    return self.run('xp', amount, player)


def xp_je(self: Client) -> ExperienceProxy:
    """Delegates to a command proxy."""

    return ExperienceProxy(self, 'xp')

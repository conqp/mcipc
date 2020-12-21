"""Implementation of the experience and xp commands."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import XPUnit


__all__ = ['ExperienceProxy', 'experience', 'xp']


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
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.experience.ExperienceProxy`
    """

    return ExperienceProxy(self, 'experience')


def xp(self: Client) -> ExperienceProxy:    # pylint: disable=C0103
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.experience.ExperienceProxy`
    """

    return ExperienceProxy(self, 'xp')

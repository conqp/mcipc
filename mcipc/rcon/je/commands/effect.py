"""Implementation of the effect command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['EffectProxy', 'effect']


class EffectProxy(CommandProxy):
    """Proxy for effect commands on the Java Edition."""

    # pylint: disable=W0621
    def clear(self, targets: str = None, effect: str = None) -> str:
        """Clears effects."""
        return self._run('clear', targets, effect)

    def give(self, targets: str, effect: str,   # pylint: disable=R0913
             seconds: int = None, amplifier: int = None,
             hide_particles: bool = None) -> str:
        """Gives an effect."""
        return self._run('give', targets, effect, seconds, amplifier,
                         hide_particles)


def effect(self: Client) -> EffectProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.effect.EffectProxy`
    """

    return EffectProxy(self, 'effect')

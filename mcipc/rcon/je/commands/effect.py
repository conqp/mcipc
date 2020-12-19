"""Implementation of the effect command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['effect']


class EffectProxy(CommandProxy):
    """Proxy for effect commands on the Java Edition."""

    def clear(self, targets: str = None, effect: str = None) -> str:
        """Clears effects."""
        return self._run('clear', targets, effect)

    def give(self, targets: str, effect: str,   # pylint: disable=R0913
             seconds: int = None, amplifier: int = None,
             hide_particles: bool = None) -> str:
        """Gives an effect."""
        return self._run('give', targets, effect, seconds, amplifier,
                         hide_particles)


def effect(self: Client) -> EffectJEProxy:
    """Returns a proxy for available sub-commands."""

    return EffectProxy(self, 'effect')

"""Implementation of the effect command."""

from mcipc.rcon.proto import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['effect_be', 'effect_je']


class EffectJEProxy(CommandProxy):
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


def effect_be(self: Client, player: str,  # pylint: disable=R0913
              effect_or_clear: str, seconds: int = None, amplifier: int = None,
              hide_particles: bool = None) -> str:
    """Returns a proxy for available sub-commands."""

    command = ['effect', player, (mode := str(effect_or_clear))]

    if mode != 'clear':
        command += [seconds, amplifier, hide_particles]

    return self.run(*command)


def effect_je(self: Client) -> EffectJEProxy:
    """Returns a proxy for available sub-commands."""

    return EffectJEProxy(self, 'effect')

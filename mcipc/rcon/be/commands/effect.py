"""Implementation of the effect command."""

from mcipc.rcon.client import Client


__all__ = ['effect']


# pylint: disable=R0913
def effect(self: Client, player: str, effect_or_clear: str,
           seconds: int = None, amplifier: int = None,
           hide_particles: bool = None) -> str:
    """Returns a proxy for available sub-commands."""

    command = ['effect', player, (mode := str(effect_or_clear))]

    if mode != 'clear':
        command += [seconds, amplifier, hide_particles]

    return self.run(*command)

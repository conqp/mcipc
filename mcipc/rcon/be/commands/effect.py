"""Implementation of the effect command."""

from typing import Optional

from mcipc.rcon.client import Client


__all__ = ['effect']


def effect(
        self: Client,
        player: str,
        effect_or_clear: str,
        seconds: Optional[int] = None,
        amplifier: Optional[int] = None,
        hide_particles: Optional[bool] = None
) -> str:
    """Returns a proxy for available sub-commands."""

    command = ['effect', player, (mode := str(effect_or_clear))]

    if mode != 'clear':
        command += [seconds, amplifier, hide_particles]

    return self.run(*command)

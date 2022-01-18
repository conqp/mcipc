"""Implementation of the camerashake command."""

from typing import Optional

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import CamerashakeType


__all__ = ['CamerashakeProxy', 'camerashake']


class CamerashakeProxy(CommandProxy):   # pylint: disable=R0903
    """Proxy for camera shake commands."""

    def add(
            self,
            player: str,
            intensity: Optional[float] = None,
            seconds: Optional[float] = None,
            shake_type: Optional[CamerashakeType] = None
    ) -> str:
        """Used to enable a camera shaking effect."""
        return self._run('add', player, intensity, seconds, shake_type)


def camerashake(self: Client) -> CamerashakeProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.be.commands.camerashake.CamerashakeProxy`
    """

    return CamerashakeProxy(self, 'camerashake')

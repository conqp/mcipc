"""Implementation of the structure command."""

from mcipc.rcon.be.types import Mirror
from mcipc.rcon.be.types import Rotation
from mcipc.rcon.be.types import StructureAnimationMode
from mcipc.rcon.be.types import StructureSaveMode
from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import Vec3


__all__ = ['StructureProxy', 'structure']


class StructureProxy(CommandProxy):
    """Proxy for structure commands."""

    # pylint: disable=C0103,R0913
    def save(self, name: str, from_: Vec3, to: Vec3,
             save_mode: StructureSaveMode = None, includes_blocks: bool = None,
             *, includes_entities: bool = None) -> str:
        """Saves a structure."""

        command = ['save', name, from_, to]

        if includes_entities is not None:
            command.append(includes_entities)

        return self._run(*command, save_mode, includes_blocks)

    def load(self, name: str, to: Vec3, rotation: Rotation = None,
             mirror: Mirror = None, includes_entities: bool = None,
             includes_blocks: bool = None, integrity: float = None,
             seed: str = None, *,
             animation_mode: StructureAnimationMode = None,
             animation_seconds: float = None) -> str:
        """Loads a structure."""
        command = ['load', name, to, rotation, mirror]

        if animation_mode is not None and animation_seconds is not None:
            command += [animation_mode, animation_seconds]

        return self._run(*command, includes_entities, includes_blocks,
                         integrity, seed)


def structure(self: Client) -> StructureProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.be.commands.structure.StructureProxy`
    """

    return StructureProxy(self, 'structure')

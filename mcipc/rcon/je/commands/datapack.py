"""Implementation of the datapack command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import DatapackMode, DatapackState


__all__ = ['DatapackProxy', 'datapack']


class DatapackProxy(CommandProxy):
    """Proxy for datapack related commands."""

    def disable(self, name: str) -> str:
        """Disables a datapack."""
        return self._run('disable', name)

    def enable(self, name: str, mode: DatapackMode,
               existing: str = None) -> str:
        """Enables a datapack."""
        command = ['enable', name, mode]

        if mode in {DatapackMode.AFTER, DatapackMode.BEFORE}:
            if existing is None:
                raise ValueError('Missing value for existing datapack.')

            command.append(existing)

        return self._run(*command)

    def list(self, state: DatapackState = None) -> str:
        """Lists the enabled datapacks."""
        command = ['list']

        if state is not None:
            command.append(state)

        return self._run(*command)


def datapack(self: Client) -> DatapackProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.datapack.DatapackProxy`
    """

    return DatapackProxy(self, 'datapack')

"""Implementation of the data command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import TargetType, TargetValue


__all__ = ['DataProxy', 'DataModifyProxy', 'DataModifySubProxy', 'data']


class DataModifySubProxy(CommandProxy):
    """Sub-proxy for the modify method."""

    def from_(self, typ: TargetType, value: TargetValue, path: str) -> str:
        """Appends data."""
        return self._run('from', typ, value, path)

    def value(self, value: str) -> str:
        """Sets data value."""
        return self._run('value', value)


class DataModifyProxy(CommandProxy):
    """Proxy for data modification."""

    @property
    def append(self) -> DataModifySubProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.data.DataModifySubProxy`
        """
        return self._proxy(DataModifySubProxy, 'append')

    def insert(self, index: int) -> DataModifySubProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.data.DataModifySubProxy`
        """
        return self._proxy(DataModifySubProxy, 'insert', index)

    @property
    def merge(self) -> DataModifySubProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.data.DataModifySubProxy`
        """
        return self._proxy(DataModifySubProxy, 'merge')

    @property
    def prepend(self) -> DataModifySubProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.data.DataModifySubProxy`
        """
        return self._proxy(DataModifySubProxy, 'prepend')

    @property
    def set(self) -> DataModifySubProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.data.DataModifySubProxy`
        """
        return self._proxy(DataModifySubProxy, 'set')


class DataProxy(CommandProxy):
    """Proxy for data sub-commands."""

    def get(self, typ: TargetType, value: TargetValue, path: str = None,
            scale: float = None) -> str:
        """Read off the entire NBT data or the subsection of the NBT data
        from the targeted block position or entity to the executor with
        syntax highlighting, scaled by <scale> if specified.
        """
        return self._run('get', typ, value, path, scale)

    def merge(self, typ: TargetType, value: TargetValue, nbt: dict) -> str:
        """Merge the NBT data from the sourced block
        position or entity with the specified <nbt> data.
        """
        return self._run('merge', typ, value, nbt)

    def modify(self, typ: TargetType, value: TargetValue,
               path: str) -> DataModifyProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.data.DataModifyProxy`
        """
        return self._proxy(DataModifyProxy, 'modify', typ, value, path)

    def remove(self, typ: TargetType, value: TargetValue, path: str) -> str:
        """Removes NBT data at <path> from the targeted block
        position or entity. Player NBT data cannot be removed.
        """
        return self._run('remove', typ, value, path)


def data(self: Client) -> DataProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.data.DataProxy`
    """

    return DataProxy(self, 'data')

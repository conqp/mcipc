"""Implementation of the data command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import TargetType, TargetValue


__all__ = ['data']


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
        """Returns a proxy for append operations."""
        return self._proxy(DataModifySubProxy, 'append')

    def insert(self, index: int) -> DataModifySubProxy:
        """Returns a proxy for insert operations."""
        return self._proxy(DataModifySubProxy, 'insert', index)

    @property
    def merge(self) -> DataModifySubProxy:
        """Returns a proxy for merge operations."""
        return self._proxy(DataModifySubProxy, 'merge')

    @property
    def prepend(self) -> DataModifySubProxy:
        """Returns a proxy for prepend operations."""
        return self._proxy(DataModifySubProxy, 'prepend')

    @property
    def set(self) -> DataModifySubProxy:
        """Returns a proxy for set operations."""
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
        """Modifies blocks."""
        return self._proxy(DataModifyProxy, 'modify', typ, value, path)

    def remove(self, typ: TargetType, value: TargetValue, path: str) -> str:
        """Removes NBT data at <path> from the targeted block
        position or entity. Player NBT data cannot be removed.
        """
        return self._run('remove', typ, value, path)


def data(self: Client) -> DataProxy:
    """Returns a proxy for the several data commands."""

    return DataProxy(self, 'data')

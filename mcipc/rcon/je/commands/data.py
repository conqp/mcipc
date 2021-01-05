"""Implementation of the data command."""

from mcipc.rcon.client import Client
from mcipc.rcon.functions import ensure_one
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import Entity, Vec3


__all__ = ['DataProxy', 'DataModifyProxy', 'DataModifySubProxy', 'data']


class DataModifySubProxy(CommandProxy):
    """Sub-proxy for the modify method."""

    def from_(self, *, block: Vec3 = None, entity: Entity = None,
              storage: str = None, path: str) -> str:
        """Appends data."""
        key, value = ensure_one(block=block, entity=entity, storage=storage)
        return self._run('from', key, value, path)

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

    def get(self, *, block: Vec3 = None, entity: Entity = None,
            storage: str = None, path: str = None, scale: float = None) -> str:
        """Read off the entire NBT data or the subsection of the NBT data
        from the targeted block position or entity to the executor with
        syntax highlighting, scaled by <scale> if specified.
        """
        key, value = ensure_one(block=block, entity=entity, storage=storage)
        return self._run('get', key, value, path, scale)

    def merge(self, *, block: Vec3 = None, entity: Entity = None,
              storage: str = None, nbt: dict) -> str:
        """Merge the NBT data from the sourced block
        position or entity with the specified <nbt> data.
        """
        key, value = ensure_one(block=block, entity=entity, storage=storage)
        return self._run('merge', key, value, nbt)

    def modify(self, *, block: Vec3 = None, entity: Entity = None,
               storage: str = None, path: str) -> DataModifyProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.data.DataModifyProxy`
        """
        key, value = ensure_one(block=block, entity=entity, storage=storage)
        return self._proxy(DataModifyProxy, 'modify', key, value, path)

    def remove(self, *, block: Vec3 = None, entity: Entity = None,
               storage: str = None, path: str) -> str:
        """Removes NBT data at <path> from the targeted block
        position or entity. Player NBT data cannot be removed.
        """
        key, value = ensure_one(block=block, entity=entity, storage=storage)
        return self._run('remove', key, value, path)


def data(self: Client) -> DataProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.data.DataProxy`
    """

    return DataProxy(self, 'data')

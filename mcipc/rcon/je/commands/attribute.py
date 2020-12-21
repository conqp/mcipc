"""Implementation of the attribute command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import Action


__all__ = [
    'AttributeProxy',
    'BaseProxy',
    'ModifierProxy',
    'ValueProxy',
    'attribute'
]


class ValueProxy(CommandProxy):    # pylint: disable=R0903
    """Proxy for attribute value getter."""

    def get(self, uuid: str, scale: float = None) -> str:
        """Returns the value of the modifier with the specified UUID."""
        return self._run('get', uuid, scale)


class BaseProxy(CommandProxy):
    """Proxy to modify bases."""

    def get(self, scale: float = None) -> str:
        """Returns the base value of the specified attribute."""
        return self._run('get', scale)

    def set(self, value: str) -> str:
        """Overwrites the base value of the specified
        attribute with the given value.
        """
        return self._run('set', value)


class ModifierProxy(CommandProxy):
    """Proxy to modify attributes."""

    def add(self, uuid: str, name: str, value: str, action: Action) -> str:
        """Adds an attribute modifier with the specified properties
        if no modifier with the same UUID already existed.
        """
        return self._run('add', uuid, name, value, action)

    def remove(self, uuid: str) -> str:
        """Removes the attribute modifier with the specified UUID."""
        return self._run('remove', uuid)

    @property
    def value(self) -> ValueProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.attribute.ValueProxy`
        """
        return self._proxy(ValueProxy, 'value')


class AttributeProxy(CommandProxy):
    """Proxy for attribute actions."""

    @property
    def base(self) -> BaseProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.attribute.BaseProxy`
        """
        return self._proxy(BaseProxy, 'base')

    @property
    def modifier(self) -> ModifierProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.attribute.ModifierProxy`
        """
        return self._proxy(ModifierProxy, 'modifier')

    def get(self, scale: float = None) -> str:
        """Returns the total value of the specified attribute."""
        return self._run('get', scale)


# pylint: disable=W0621
def attribute(self: Client, target: str, attribute: str) -> AttributeProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.attribute.AttributeProxy`
    """

    return AttributeProxy(self, 'attribute', target, attribute)

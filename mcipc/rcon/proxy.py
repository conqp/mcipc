"""Command proxies."""

from typing import Type, TypeVar

from mcipc.rcon.functions import until_none
from mcipc.rcon.client import Client


__all__ = ['CommandProxy']


DelegatedType = TypeVar('DelegatedType')


class CommandProxy:
    """A basic command proxy."""

    __slots__ = ('_client', '_args')

    def __init__(self, client: Client, *args: str):
        """Sets the client and arguments."""
        self._client = client
        self._args = tuple(until_none(args))

    def __repr__(self):
        return f'{type(self).__name__}({self._client}, {self._args})'

    def _proxy(self, cls: Type[DelegatedType], *args: str) -> DelegatedType:
        """Returns a sub-proxy."""
        return cls(self._client, *self._args, *until_none(args))

    def _run(self, *args) -> str:
        """Runs the respective command."""
        return self._client.run(*self._args, *args)

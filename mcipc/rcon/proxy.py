"""Command proxies."""

from __future__ import annotations

from mcipc.rcon.proto import Client


__all__ = ['CommandProxy']


class CommandProxy:     # pylint: disable=R0903
    """A basic command proxy."""

    __slots__ = ('_client', '_args')

    def __init__(self, client: Client, *args: str):
        """Sets the client and arguments."""
        self._client = client
        self._args = args

    def _proxy(self, cls: type, *args: str) -> CommandProxy:
        """Returns a sub-proxy."""
        return cls(self._client, *self._args, *args)

    def _run(self, *args) -> str:
        """Runs the respective command."""
        return self._client.run(*self._args, *args)

"""Command proxies."""

from __future__ import annotations
from typing import NamedTuple

from mcipc.rcon.functions import until_none
from mcipc.rcon.client import Client


__all__ = ['CommandProxy']


class CommandProxy(NamedTuple):
    """A basic command proxy."""

    client: Client
    args: tuple[str] = ()

    def _proxy(self, cls: type, *args: str) -> CommandProxy:
        """Returns a sub-proxy."""
        return cls(self.client, *self.args, *until_none(args))

    def _run(self, *args) -> str:
        """Runs the respective command."""
        return self.client.run(*self.args, *args)

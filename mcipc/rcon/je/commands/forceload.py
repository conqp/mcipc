"""Implementation of the forceload command."""

from typing import Union

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import Vec2


__all__ = ['ForceloadProxy', 'forceload']


class ForceloadProxy(CommandProxy):
    """Provides forceload-related sub commands."""

    # pylint: disable=C0103
    def add(self, from_: Vec2, to: Vec2 = None) -> str:
        """Forces the chunk at the <from> position (through to <to> if set) in
        the dimension of the command's execution to be loaded constantly.
        """
        return self._run('add', from_, to)

    def remove(self, from_or_all: Union[Vec2, 'all'], to: Vec2 = None) -> str:
        """Unforces the chunk at the <from> position (through to <to> if set)
        in the dimension of the command's execution to be loaded constantly.
        """
        if from_or_all == 'all':
            return self._run('remove', 'all')

        if to is None:
            raise ValueError('To must be specified, if not removing all.')

        return self._run('remove', from_or_all, to)

    def query(self, pos: Vec2 = None) -> str:
        """If chunk coordinates are given, displays the specified chunk in the
        dimension of the command's execution is force loaded; otherwise, lists
        which chunks in the dimension of the command's execution are force
        loaded.
        """
        return self._run('query', pos)


def forceload(self: Client) -> ForceloadProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.forceload.ForceloadProxy`
    """

    return ForceloadProxy(self, 'forceload')

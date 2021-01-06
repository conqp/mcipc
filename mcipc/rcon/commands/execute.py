"""Implementation of the execute command."""

from __future__ import annotations

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import Anchor
from mcipc.rcon.types import BossbarSlot
from mcipc.rcon.types import DataType
from mcipc.rcon.types import IntRange
from mcipc.rcon.types import Rotation
from mcipc.rcon.types import ScanMode
from mcipc.rcon.types import StorageType
from mcipc.rcon.types import Vec3


__all__ = [
    'ConditionalProxy',
    'DataProxy',
    'ExecuteProxy',
    'ScoreProxy',
    'StoreProxy',
    'execute'
]


class ScoreProxy(CommandProxy):
    """Check a score against either another score or a given range."""

    # pylint: disable=W0622
    def matches(self, range: IntRange) -> ExecuteProxy:
        """Matches a range."""
        return self._proxy(ExecuteProxy, 'matches', range)

    # pylint: disable=C0103
    def lt(self, source: str, objective: str) -> ExecuteProxy:
        """Returns a < comparison."""
        return self._proxy(ExecuteProxy, '<', source, objective)

    def le(self, source: str, objective: str) -> ExecuteProxy:
        """Returns a <= comparison."""
        return self._proxy(ExecuteProxy, '<=', source, objective)

    def eq(self, source: str, objective: str) -> ExecuteProxy:
        """Returns a == comparison."""
        return self._proxy(ExecuteProxy, '==', source, objective)

    def ge(self, source: str, objective: str) -> ExecuteProxy:
        """Returns a >= comparison."""
        return self._proxy(ExecuteProxy, '>=', source, objective)

    def gt(self, source: str, objective: str) -> ExecuteProxy:
        """Returns a > comparison."""
        return self._proxy(ExecuteProxy, '>', source, objective)


class DataProxy(CommandProxy):
    """Checks whether the targeted block, entity
    or storage has any data for a given tag.
    """

    def block(self, pos: Vec3, path: str) -> ExecuteProxy:
        """Checks a block."""
        return self._proxy(ExecuteProxy, 'block', pos, path)

    def entity(self, target: str, path: str) -> ExecuteProxy:
        """Checks an entity."""
        return self._proxy(ExecuteProxy, 'entity', target, path)

    def storage(self, source: str, path: str) -> ExecuteProxy:
        """Checks a storage."""
        return self._proxy(ExecuteProxy, 'storage', source, path)


class ConditionalProxy(CommandProxy):
    """Proxies if and unless conditionals."""

    def block(self, pos: Vec3, block: str) -> ExecuteProxy:
        """Compares the block at a given position to a given block ID."""
        return self._proxy(ExecuteProxy, 'block', pos, block)

    def blocks(self, start: Vec3, end: Vec3, destination: Vec3,
               scan_mode: ScanMode) -> ExecuteProxy:
        """Compares the blocks in two equally sized volumes."""
        return self._proxy(ExecuteProxy, 'blocks', start, end, destination,
                           scan_mode)

    @property
    def data(self) -> DataProxy:
        """Delegates to a :py:class:`mcipc.rcon.commands.execute.DataProxy`"""
        return self._proxy(DataProxy, 'data')

    def entity(self, entities: str) -> ExecuteProxy:
        """Checks whether one or more <targets> exist."""
        return self._proxy(ExecuteProxy, 'entity', entities)

    def predicate(self, predicate: str) -> ExecuteProxy:
        """Checks whether the <predicate> evaluates to a positive result."""
        return self._proxy(ExecuteProxy, 'predicate', predicate)

    def score(self, target: str, target_objective: str) -> ScoreProxy:
        """Delegates to a score proxy."""
        return self._proxy(ScoreProxy, 'score', target, target_objective)


class StoreProxy(CommandProxy):
    """Proxy to handle store sub-command."""

    def block(self, target_pos: Vec3, path: str,
              type: DataType,   # pylint: disable=W0622
              scale: float) -> ExecuteProxy:
        """Saves the final command's return value
        as tag data within a block entity.
        """
        return self._proxy(ExecuteProxy, 'block', target_pos, path, type,
                           scale)

    def bossbar(self, ident: str, value: BossbarSlot) -> ExecuteProxy:
        """Saves the final command's return value in either
        a bossbar's current value or its maximum value.
        """
        return self._proxy(ExecuteProxy, 'bossbar', ident, value)

    def entity(self, target: str, path: str,
               type: DataType,  # pylint: disable=W0622
               scale: float) -> ExecuteProxy:
        """Save the final command's return value
        in one of an entity's data tags.
        """
        return self._proxy(ExecuteProxy, 'entity', target, path, type, scale)

    def score(self, targets: str, objective: str) -> ExecuteProxy:
        """Overrides the score held by <targets> on the given
        <objective> with the final command's return value.
        """
        return self._proxy(ExecuteProxy, 'score', targets, objective)

    def storage(self, target: str, path: str,
                type: DataType,     # pylint: disable=W0622
                scale: float) -> ExecuteProxy:
        """Uses the <path> within storage <target>
        to store the return value in.
        """
        return self._proxy(ExecuteProxy, 'storage', target, path, type, scale)


class ExecuteProxy(CommandProxy):
    """A proxy for execute sub-commands."""

    def __call__(self) -> str:
        """Runs the command in the current execution context."""
        return self._run()

    def align(self, axes: str) -> ExecuteProxy:
        """Aligns with the given axes and returns a sub-proxy."""
        return self._proxy(type(self), 'align', axes)

    def anchored(self, anchor: str) -> ExecuteProxy:
        """Stores the distance from the feet to the eyes of
        the entity that is executing the command in the anchor,
        which is part of the command context.
        """
        return self._proxy(type(self), 'anchored', anchor)

    def as_(self, targets: str) -> ExecuteProxy:
        """Executes the command as the given targets."""
        return self._proxy(type(self), 'as', targets)

    def at(self, targets: str) -> ExecuteProxy:     # pylint: disable=C0103
        """Executes the command at the given targets."""
        return self._proxy(type(self), 'at', targets)

    def facing(self, *, pos: Vec3 = None, targets: str = None,
               anchor: Anchor = None) -> ExecuteProxy:
        """Faces a position or entity."""
        if sum(item is not None for item in (pos, targets)) != 1:
            raise ValueError('Must specify either pos or targets.')

        if pos is not None:
            return self._proxy(type(self), 'facing', pos)

        if anchor is None:
            raise ValueError('No anchor specified.')

        return self._proxy(type(self), 'facing', 'entity', targets, anchor)

    def in_(self, dimension: str) -> ExecuteProxy:
        """Executes in the given dimension."""
        return self._proxy(type(self), 'in', dimension)

    def positioned(self, *, pos: Vec3 = None,
                   targets: str = None) -> ExecuteProxy:
        """Runs the command with a given positioning."""
        if sum(item is not None for item in (pos, targets)) != 1:
            raise ValueError('Must specify either pos or targets.')

        if pos is not None:
            return self._proxy(type(self), 'positioned', pos)

        return self._proxy(type(self), 'positioned', 'as', targets)

    def rotated(self, *, rot: Rotation = None,
                targets: str = None) -> ExecuteProxy:
        """Executes the command with the given rotation."""
        if sum(item is not None for item in (rot, targets)) != 1:
            raise ValueError('Must specify either rot or targets.')

        if rot is not None:
            return self._proxy(type(self), 'rotated', rot)

        return self._proxy(type(self), 'rotated', 'as', targets)

    def store(self, what: StorageType):
        """Stores the result or success."""
        return self._proxy(StoreProxy, 'store', what)

    @property
    def if_(self) -> ConditionalProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.commands.execute.ConditionalProxy`
        """
        return self._proxy(ConditionalProxy, 'if')

    @property
    def unless(self) -> ConditionalProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.commands.execute.ConditionalProxy`
        """
        return self._proxy(ConditionalProxy, 'unless')

    def run(self, *arguments: str) -> str:
        """Runs the a command with arguments
        in the current execution context.
        """
        return self._run('run', *arguments)


def execute(self: Client) -> ExecuteProxy:
    """Delegates to a :py:class:`mcipc.rcon.commands.execute.ExecuteProxy`"""

    return ExecuteProxy(self, 'execute')

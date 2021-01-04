"""Implementation of loot command."""

from typing import Union

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.types import Hand, Vec3


__all__ = ['LootProxy', 'ReplaceProxy', 'SourceProxy', 'loot']


class SourceProxy(CommandProxy):
    """Proxy for source commands."""

    def fish(self, loot_table: str, pos: Vec3,
             tool_or_hand: Union[Hand, str] = None) -> str:
        """Runs the command with the fish source."""
        return self._run('fish', loot_table, pos, tool_or_hand)

    def loot(self, loot_table: str) -> str:
        """Runs the command with a loot source."""
        return self._run('loot', loot_table)

    def kill(self, target: str) -> str:
        """Runs the command with a killed target as source."""
        return self._run('kill', target)

    def mine(self, pos: Vec3, tool_or_hand: Union[Hand, str] = None) -> str:
        """Runs the command with a mined resource as source."""
        return self._run('mine', pos, tool_or_hand)


class ReplaceProxy(CommandProxy):
    """Proxy for replace commands."""

    def entity(self, entities: str, slot: str,
               count: int = None) -> SourceProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.loot.SourceProxy`
        """
        return self._proxy(SourceProxy, 'entity', entities, slot, count)

    def block(self, target_pos: Vec3, slot: str,
              count: int = None) -> SourceProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.loot.SourceProxy`
        """
        return self._proxy(SourceProxy, 'block', target_pos, slot, count)


class LootProxy(CommandProxy):
    """Proxy for target-related commands."""

    def spawn(self, target_pos: Vec3) -> SourceProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.loot.SourceProxy`
        """
        return self._proxy(SourceProxy, 'spawn', target_pos)

    @property
    def replace(self) -> ReplaceProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.loot.ReplaceProxy`
        """
        return self._proxy(ReplaceProxy, 'replace')

    def give(self, players: str) -> SourceProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.loot.SourceProxy`
        """
        return self._proxy(SourceProxy, 'give', players)

    def insert(self, target_pos: Vec3) -> SourceProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.loot.SourceProxy`
        """
        return self._proxy(SourceProxy, 'insert', target_pos)


def loot(self: Client) -> LootProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.loot.LootProxy`
    """

    return LootProxy(self, 'loot')

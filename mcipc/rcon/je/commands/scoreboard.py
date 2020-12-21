"""Implementation of the scoreboard command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.je.types import RenderType


__all__ = [
    'ModifyProxy',
    'ObjectivesProxy',
    'PlayersProxy',
    'ScoreboardProxy',
    'scoreboard'
]


class ModifyProxy(CommandProxy):
    """Proxy for modify commands."""

    def displayname(self, objective: str, display_name: str) -> str:
        """Modifies the display name of the objective."""
        return self._run(objective, 'displayname', display_name)

    def rendertype(self, objective: str, render_type: RenderType):
        """Modifies the render type of the objective."""
        return self._run(objective, 'rendertype', render_type)


class ObjectivesProxy(CommandProxy):
    """Proxy for objectives sub commands."""

    def add(self, objective: str, criterion: str,
            display_name: str = None) -> str:
        """Adds an objective to the scoreboard."""
        return self._run('add', objective, criterion, display_name)

    def list(self) -> str:
        """Lists objectives on the scoreboard."""
        return self._run('list')

    def modify(self, objective: str) -> ModifyProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.scoreboard.ModifyProxy`
        """
        return self._proxy(ModifyProxy, 'modify', objective)

    def remove(self, objective: str) -> str:
        """Removes an objective from the scoreboard."""
        return self._run('remove', objective)

    def setdisplay(self, slot: str, objective: str = None):
        """Sets the display slot of an objective."""
        return self._run('setdisplay', slot, objective)


class PlayersProxy(CommandProxy):
    """Proxy for player commands."""

    def add(self, targets: str, objective: str, score: int) -> str:
        """Adds score for an objective for a player."""
        return self._run('add', targets, objective, score)

    def enable(self, targets: str, objective: str) -> str:
        """Enables an objective for the given targets."""
        return self._run('enable', targets, objective)

    def get(self, target: str, objective: str) -> str:
        """Gets a player's objective."""
        return self._run('get', target, objective)

    def list(self, target: str = None) -> str:
        """Lists scoreboard of an optional player."""
        return self._run('list', target)

    # pylint: disable=R0913
    def operation(self, targets: str, target_objective: str, operation: str,
                  source: str, source_objective: str) -> str:
        """Applies an arithmetic operation altering the target's/targets'
        score(s) in the target objective, using source target's/targets'
        score(s) in the source objective as input.
        """
        return self._run('operation', targets, target_objective, operation,
                         source, source_objective)

    def remove(self, targets: str, objective: str, score: int) -> str:
        """Decrements the target's/targets' score(s)
        in that objective by the given amount.
        """
        return self._run('remove', targets, objective, score)

    def reset(self, targets: str, objective: str = None) -> str:
        """Resets a player's score."""
        return self._run('reset', targets, objective)

    def set(self, targets: str, objective: str, score: int) -> str:
        """Sets a player's score."""
        return self._run('set', targets, objective, score)


class ScoreboardProxy(CommandProxy):
    """Proxy for scoreboard sub commands."""

    @property
    def objectives(self) -> ObjectivesProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.scoreboard.ObjectivesProxy`
        """
        return self._proxy(ObjectivesProxy, 'objectives')

    @property
    def players(self) -> PlayersProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.je.commands.scoreboard.PlayersProxy`
        """
        return self._proxy(PlayersProxy, 'players')


def scoreboard(self: Client) -> ScoreboardProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.scoreboard.ScoreboardProxy`
    """

    return ScoreboardProxy(self, 'scoreboard')

"""Implementation of the scoreboard command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy
from mcipc.rcon.je.types import RenderType


__all__ = ['scoreboard']


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
        """Delegates to a command proxy."""
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

    # TODO: Implement further commands and scoreboard for Bedrock Edition.


class ScoreboardProxy(CommandProxy):
    """Proxy for scoreboard sub commands."""

    @property
    def objectives(self) -> ObjectivesProxy:
        """Delegates to a command proxy."""
        return self._proxy(ObjectivesProxy, 'objectives')

    @property
    def players(self) -> PlayersProxy:
        """Delegates to a command proxy."""
        return self._proxy(PlayersProxy, 'players')


def scoreboard(self: Client) -> ScoreboardProxy:
    """Delegates to a command proxy."""

    return ScoreboardProxy(self, 'scoreboard')

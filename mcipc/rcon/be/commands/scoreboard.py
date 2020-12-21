"""Implementation of the scoreboard command."""

from typing import Union

from mcipc.rcon.be.types import Location, Operator, Order
from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['ObjectivesProxy', 'PlayersProxy', 'ScoreboardProxy', 'scoreboard']


class ObjectivesProxy(CommandProxy):
    """Proxy for objective commands."""

    def add(self, objective: str, display_name: str = None) -> str:
        """Adds an objective."""
        return self._run('add', objective, 'dummy', display_name)

    def list(self) -> str:
        """Lists objectives."""
        return self._run('list')

    def remove(self, objective: str) -> str:
        """Removes an objective."""
        return self._run('remove', objective)

    def setdisplay(self, location: Location, objective: str,
                   order: Order = None) -> str:
        """Sets a display."""
        command = ['setdisplay', location := Location(location), objective]

        if location in {Location.LIST, Location.SIDEBAR}:
            command.append(order)

        return self._run(*command)


class PlayersProxy(CommandProxy):
    """Proxy for player commands."""

    def list(self, playername: str = None) -> str:
        """Lists player scores."""
        return self._run('list', playername)

    def reset(self, player: str, objective: str = None) -> str:
        """Resets a player's score."""
        return self._run('reset', player, objective)

    # pylint: disable=W0622
    def test(self, player: str, objective: str, min: Union[int, str],
             max: Union[int, str] = None) -> str:
        """Tests whether a player's score is within the given boundaries."""
        return self._run('test', player, objective, min, max)

    def random(self, player: str, objective: str, min: int,
               max: int = None) -> str:
        """Sets a random score for the player's objective."""
        return self._run('random', player, objective, min, max)

    def set(self, player: str, objective: str, count: int) -> str:
        """Sets a player's score."""
        return self._run('set', player, objective, count)

    def add(self, player: str, objective: str, count: int) -> str:
        """Adds to a player's score."""
        return self._run('add', player, objective, count)

    def remove(self, player: str, objective: str, count: int) -> str:
        """Removes from a player's score."""
        return self._run('remove', player, objective, count)

    # pylint: disable=R0913
    def operation(self, target_name: str, target_objective: str,
                  operation: Operator, selector: str, objective: str) -> str:
        """Executes an operation."""
        return self._run('operation', target_name, target_objective,
                         operation, selector, objective)


class ScoreboardProxy(CommandProxy):
    """Proxy for scoreboard related commands."""

    @property
    def objectives(self) -> ObjectivesProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.be.commands.scoreboard.ObjectivesProxy`
        """
        return self._proxy(ObjectivesProxy, 'objectives')

    @property
    def players(self) -> PlayersProxy:
        """Delegates to a
        :py:class:`mcipc.rcon.be.commands.scoreboard.PlayersProxy`
        """
        return self._proxy(PlayersProxy, 'players')


def scoreboard(self: Client) -> ScoreboardProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.be.commands.scoreboard.ScoreboardProxy`
    """

    return ScoreboardProxy(self, 'scoreboard')

"""Implementation of the team command."""

from mcipc.rcon.client import Client
from mcipc.rcon.je.types import TeamOption, TeamValue
from mcipc.rcon.proxy import CommandProxy


__all__ = ['TeamProxy', 'team']


class TeamProxy(CommandProxy):
    """Proxy for team commands."""

    # pylint: disable=W0621
    def add(self, team: str, display_name: dict = None) -> str:
        """Adds a team."""
        return self._run('add', team, display_name)

    def empty(self, team: str) -> str:
        """Emties a team."""
        return self._run('empty', team)

    def join(self, team: str, members: str = None) -> str:
        """Joins a team."""
        return self._run('join', team, members)

    def leave(self, members: str = None) -> str:
        """Leaves the team."""
        return self._run('leave', members)

    def list(self, team: str = None) -> str:
        """Lists team members."""
        return self._run('list', team)

    def modify(self, team: str, option: TeamOption, value: TeamValue) -> str:
        """Modifies a team."""
        return self._run('modify', team, option, value)

    def remove(self, team: str) -> str:
        """Removes the given team."""
        return self._run('remove', team)


def team(self: Client) -> TeamProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.team.TeamProxy`
    """

    return TeamProxy(self, 'team')

"""Implementation of the spreadplayers command."""

from mcipc.rcon.client import Client
from mcipc.rcon.types import Vec2


__all__ = ['spreadplayers']


# pylint: disable=R0913
def spreadplayers(self: Client, center: Vec2, spread_distance: float,
                  max_range: float, respec_teams: bool, targets: str, *,
                  max_height: int = None) -> str:
    """Spreads players to resulting position under the maximum height."""

    command = ['spreadplayers', center, spread_distance, max_range]

    if max_height is not None:
        command += ['under', max_height]

    return self.run(*command, respec_teams, targets)

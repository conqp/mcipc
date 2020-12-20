"""Implementation of the spreadplayers command."""

from mcipc.rcon.be.types import RelativeFloat
from mcipc.rcon.client import Client


__all__ = ['spreadplayers']


# pylint: disable=C0103,R0913
def spreadplayers(self: Client, x: RelativeFloat, y: RelativeFloat,
                  spread_distance: float, max_range: float,
                  victim: str) -> str:
    """Spreads players."""

    return self.run('spreadplayers', x, y, spread_distance, max_range, victim)

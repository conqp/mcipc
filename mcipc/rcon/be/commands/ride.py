"""Implementation of the ride command."""

from typing import Optional

from mcipc.rcon.be.types import FillType, RideRules, TeleportRules
from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['RideProxy', 'ride']


class RideProxy(CommandProxy):
    """Proxy for ride related commands."""

    def start_riding(
            self,
            ride: str,
            teleport_rules: Optional[TeleportRules] = None,
            how_to_fill: Optional[FillType] = None
    ) -> str:
        """Makes <riders> ride on <ride>."""
        return self._run('start_riding', ride, teleport_rules, how_to_fill)

    def stop_riding(self) -> str:
        """Makes <riders> dismount."""
        return self._run('stop_riding')

    def evict_riders(self) -> str:
        """Makes entities that are riding on <rides> dismount."""
        return self._run('evict_riders')

    def summon_rider(
            self,
            entity_type: str,
            spawn_event: Optional[str] = None,
            name_tag: Optional[str] = None
    ) -> str:
        """Summons a rider."""
        return self._run('summon_rider', entity_type, spawn_event, name_tag)

    def summon_ride(
            self,
            entity_type: str,
            ride_rules: Optional[RideRules] = None,
            spawn_event: Optional[str] = None,
            name_tag: Optional[str] = None
    ) -> str:
        """Summons a ride."""
        return self._run('summon_ride', entity_type, ride_rules, spawn_event,
                         name_tag)


def ride(self: Client, riders_or_rides: str) -> RideProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.be.commands.ride.RideProxy`
    """

    return RideProxy(self, 'ride', riders_or_rides)

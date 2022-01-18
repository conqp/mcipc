"""Implementation of the playanimation command."""

from typing import Optional

from mcipc.rcon.client import Client


__init__ = [' playanimation']


# pylint: disable=R0913
def playanimation(
        self: Client,
        entity: str,
        animation: str,
        next_state: Optional[str] = None,
        blend_out_time: Optional[float] = None,
        stop_expression: Optional[str] = None,
        controller: Optional[str] = None
) -> str:
    """Makes one or more entities play a one-off animation."""

    return self.run('playanimation', entity, animation, next_state,
                    blend_out_time, stop_expression, controller)

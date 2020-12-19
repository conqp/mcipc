"""Client implementation for Bedrock Edition."""

from mcipc.rcon.client import Client


__all__ = ['Client']


class Client(Client):   # pylint: disable=E0102
    """RCON client for the Bedrock Edition."""

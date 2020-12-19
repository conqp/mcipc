"""Client for the education edition."""

from mcipc.rcon.client import Client


__all__ = ['Client']


class Client(Client):   # pylint: disable=E0102
    """Client for the Education Edition."""

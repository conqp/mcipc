"""Client implementation for Java Edition."""

from mcipc.rcon.client import Client
from mcipc.rcon.je.errors import check_result


__all__ = ['Client']


class Client(Client):   # pylint: disable=E0102
    """A high-level RCON client with methods for the Java Edition."""

    # pylint: disable=W0221
    def run(self, command: str, *arguments: str) -> str:
        """Runs a command and checks the return value for errors."""
        return check_result(super().run(command, *arguments))

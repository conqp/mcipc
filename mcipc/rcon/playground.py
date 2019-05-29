"""Experimental features that are subject to unannounced change."""

from datetime import datetime
from locale import LC_TIME, getdefaultlocale, setlocale
from subprocess import PIPE, check_output

from mcipc.config import FORTUNE

from mcipc.rcon.client import Client as _Client


__all__ = ['Client']


class Client(_Client):
    """Client with some more extras."""

    def fortune(self, short: bool = True, offensive: bool = False):
        """Sends a fortune to all players."""
        command = [FORTUNE]

        if short:
            command.append('-s')

        if offensive:
            command.append('-o')

        text = check_output(command, stderr=PIPE, text=True)
        return self.say(text)

    def datetime(self, frmt: str = '%c'):
        """Tells all players the current datetime."""
        setlocale(LC_TIME, getdefaultlocale())  # Fix loacale.
        text = datetime.now().strftime(frmt)
        return self.say(text)

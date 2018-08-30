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
        args = []

        if short:
            args.append('-s')

        if offensive:
            args.append('-o')

        response = check_output([FORTUNE] + args, stderr=PIPE)
        text = response.decode()
        return self.say(text)

    def datetime(self, frmt: str = '%c'):
        """Tells all players the current datetime."""
        setlocale(LC_TIME, getdefaultlocale())  # Fix loacale.
        text = datetime.now().strftime(frmt)
        return self.say(text)

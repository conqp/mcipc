"""Parsing responses from the difficulty command."""

from mcipc.rcon.functions import boolmap


__all__ = ['parse']


SET = 'The difficulty has been set to (\\w+)'
UNCHANGED = 'The difficulty did not change; it is already set to (\\w+)'


def parse(text: str) -> bool:
    """Parses a boolean value from the text
    returned by the difficulty command.
    """

    return boolmap(text, true=SET, false=UNCHANGED)

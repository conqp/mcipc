"""Parsing responses from the difficulty command."""

from mcipc.rcon.functions import parse_bool


__all__ = ['parse']


SET = r'The difficulty has been set to (\w+)'
UNCHANGED = r'The difficulty did not change; it is already set to (\w+)'


def parse(text: str) -> bool:
    """Parses a boolean value from the text
    returned by the difficulty command.
    """

    return parse_bool(text, true=SET, false=UNCHANGED)

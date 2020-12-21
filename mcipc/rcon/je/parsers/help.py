"""Parses a dict from a response text."""

from collections import defaultdict


__all__ = ['parse']


def parse(text: str) -> dict:
    """Creates the help object from a server response text."""

    help = defaultdict(list)    # pylint: disable=W0622

    for use_case in filter(None, text.split('/')):
        command, *arguments = use_case.split()
        help[command].append(arguments)

    return help

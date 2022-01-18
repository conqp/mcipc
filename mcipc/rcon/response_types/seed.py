"""Parses a seed value from a server response."""

from re import fullmatch


__all__ = ['parse']


REGEX = r'.*\[(-?\d+)\]'


def parse(text: str) -> int:
    """Returns an integer."""

    if (match := fullmatch(REGEX, text)) is None:
        raise ValueError('Unexpected seed response:', text)

    return int(match.group(1))

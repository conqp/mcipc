"""Represents a seed."""

from re import compile  # pylint: disable=W0622


__all__ = ['Seed']


REGEX = compile('.*\\[(-?\\d+)\\]')


class Seed(int):
    """A seed value."""

    @classmethod
    def from_response(cls, text):
        """Returns a seed from a server response."""
        match = REGEX.fullmatch(text)
        return cls(match.group(1))

    def to_json(self) -> int:
        """Returns a JSON-ish dict."""
        return int(self)

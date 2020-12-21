"""Result of a successful kick."""

from typing import NamedTuple


__all__ = ['KickedPlayer']


class KickedPlayer(NamedTuple):
    """Stores information about a kicked player."""

    name: str
    reason: str

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {'name': self.name, 'reason': self.reason}

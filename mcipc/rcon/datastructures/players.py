"""Information about online players."""

from __future__ import annotations
from re import Match, compile  # pylint: disable=W0622
from typing import NamedTuple, Tuple, Union


__all__ = ['Players']


REGEX_VANILLA = compile('.+ (\\d+) .+ (\\d+) .+: (.*)')
REGEX_PAPER = compile('.+ §c(\\d+)§6 .+ §c(\\d+)§6 .+\\.([\\s\\S]*)')
REGEX_PAPER_NAME = compile('.+: (?:§4)?(\\w+)(?:§r)?§f')


def extract_paper_name(name: str) -> Union[str, None]:
    """Extracts names from Paper server output."""

    if (match := REGEX_PAPER_NAME.fullmatch(name.strip())) is None:
        return None

    return match.group(1)


class Players(NamedTuple):
    """Online players information."""

    online: int
    max: int
    names: Tuple[str]

    @classmethod
    def from_vanilla(cls, match: Match) -> Players:
        """Creates the players information from a vanilla server match."""
        online, max_, names = match.groups()
        names = filter(None, map(lambda name: name.strip(), names.split(', ')))
        return cls(int(online), int(max_), tuple(names))

    @classmethod
    def from_paper(cls, match: Match) -> Players:
        """Creates the players information from a Paper server response.
        https://github.com/conqp/mcipc/issues/13#issuecomment-726145034
        """
        online, max_, names = match.groups()
        names = filter(None, map(extract_paper_name, names.split('\n')))
        return cls(int(online), int(max_), tuple(names))

    @classmethod
    def from_response(cls, text: str) -> Players:
        """Creates the players information from a server response."""
        if (match := REGEX_VANILLA.fullmatch(text)) is not None:
            return cls.from_vanilla(match)

        if (match := REGEX_PAPER.fullmatch(text)) is not None:
            return cls.from_paper(match)

        raise ValueError('Unexpected players response:', text)

    def to_json(self) -> dict:
        """Returns a JSON-ish dict."""
        return {'online': self.online, 'max': self.max, 'names': self.names}

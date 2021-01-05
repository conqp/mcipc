"""Named binary tags."""

from typing import Any, Dict, Union

from mcipc.rcon.enumerations import Item, TargetSelector
from mcipc.rcon.functions import stringify


__all__ = ['NBT']


def tags_to_str(tags: Dict[str, Any]) -> str:
    """Returns the tags as a string."""

    return ', '.join(f'{key}={stringify(val)}' for key, val in tags.items())


class NBT:
    """Represents a named binary tag."""

    __slots__ = ('target', 'tags')

    def __init__(self, target: Union[Item, TargetSelector, str], **tags):
        """Stores the object name and optional tags."""
        self.target = target
        self.tags = tags

    def __repr__(self):
        """Returns a str representation for eval()."""
        return f'{type(self).__name__}({self.target!r}, {self.tags!r})'

    def __str__(self):
        """Returns a str representation for RCON."""
        return f'{stringify(self.target)}[{tags_to_str(self.tags)}]'

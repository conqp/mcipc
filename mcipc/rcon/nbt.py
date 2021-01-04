"""Named binary tags."""

from typing import Union

from mcipc.rcon.item import Item


__all__ = ['NBT']


class NBT:
    """Represents a named binary tag."""

    def __init__(self, obj: Union[Item, str], **tags):
        """Stores the object name and optional tags."""
        self.obj = obj
        self.tags = tags

    def __repr__(self):
        """Returns a str representation for eval()."""
        return f'{type(self)}({self.obj!r}, {self.tagstr})'

    def __str__(self):
        """Returns a str representation for RCON."""
        return f'{self.obj}[{self.tagstr}]'

    @property
    def tagstr(self):
        """Returns the tags as a str."""
        return ', '.join(f'{key}={val!r}' for key, val in self.tags.items())

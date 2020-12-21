"""Implementation of the title comman."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['TitleProxy', 'title']


class TitleProxy(CommandProxy):
    """Proxy for title commands."""

    def clear(self) -> str:
        """Clears the title."""
        return self._run('clear')

    def reset(self) -> str:
        """Resets the title."""
        return self._run('reset')

    # pylint: disable=W0621
    def title(self, title: str) -> str:
        """Sets the title."""
        return self._run('title', title)

    def subtitle(self, title: str) -> str:
        """Sets the subtitle."""
        return self._run('subtitle', title)

    def actionbar(self, title: str) -> str:
        """Sets the action bar."""
        return self._run('actionbar', title)

    def times(self, fade_in: int, stay: int, fade_out: int) -> str:
        """    Changes the fade-in, stay, and fade-out times of all current
        and future screen titles for the specified player(s).
        """
        return self._run('times', fade_in, stay, fade_out)


def title(self: Client, targets: str) -> TitleProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.title.TitleProxy`
    """

    return TitleProxy(self, 'title', targets)

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

    def title(self, title_text: str) -> str:
        """Sets the title."""
        return self._run('title', title_text)

    def subtitle(self, title_text: str) -> str:
        """Sets the subtitle."""
        return self._run('subtitle', title_text)

    def actionbar(self, title_text: str) -> str:
        """Sets the action bar."""
        return self._run('actionbar', title_text)

    def times(self, fade_in: int, stay: int, fade_out: int) -> str:
        """    Changes the fade-in, stay, and fade-out times of all current
        and future screen titles for the specified player(s).
        """
        return self._run('times', fade_in, stay, fade_out)


def title(self: Client, player: str) -> TitleProxy:
    """Delegates to a
    :py:class:`mcipc.rcon.be.commands.title.TitleProxy`
    """

    return TitleProxy(self, 'title', player)

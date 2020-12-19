"""Implementation of the recipe command."""

from mcipc.rcon.proto import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['recipe']


class RecipeProxy(CommandProxy):
    """Proxy for recipe related commands."""

    # pylint: disable=W0621
    def give(self, targets: str, recipe: str = '*') -> str:
        """Gives or takes all recipes from that player."""
        return self._run('give', targets, recipe)

    def take(self, targets: str, recipe: str = '*') -> str:
        """Gives or takes a specified recipe from that player."""
        return self._run('take', targets, recipe)


def recipe(self: Client) -> RecipeProxy:
    """Delegates to a command proxy."""

    return RecipeProxy(self, 'recipe')

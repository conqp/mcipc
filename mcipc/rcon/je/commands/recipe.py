"""Implementation of the recipe command."""

from mcipc.rcon.client import Client
from mcipc.rcon.proxy import CommandProxy


__all__ = ['RecipeProxy', 'recipe']


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
    """Delegates to a
    :py:class:`mcipc.rcon.je.commands.recipe.RecipeProxy`
    """

    return RecipeProxy(self, 'recipe')

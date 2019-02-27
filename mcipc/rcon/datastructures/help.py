"""Datastructures to represent help on commands."""

from logging import getLogger


LOGGER = getLogger(__file__)


class Help(dict):
    """command: arguments key pairs."""

    @property
    def usage(self):
        """Returns a docopt-compliant usage string."""
        string = 'Usage:\n'

        for command, arguments in self.items():
            string += f'    {command} {arguments}\n'

        return string

    @property
    def pattern(self):
        """Returns a docopt pattern."""
        try:
            from docopt import printable_usage
            from docopt import parse_defaults
            from docopt import formal_usage
            from docopt import parse_pattern
        except ImportError:
            LOGGER.warning('docopt not installed.')
            LOGGER.warning('Command help pattern generation unavailable.')
            return None

        usage = printable_usage(self.usage)
        options = parse_defaults(self.usage)
        return parse_pattern(formal_usage(usage), options)

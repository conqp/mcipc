"""Datastructures to represent help on commands."""

from logging import getLogger


LOGGER = getLogger(__file__)


class Help(dict):
    """command: arguments key pairs."""

    @property
    def usage(self):
        """Returns a docopt-compliant usage string."""
        header = 'Usage:\n'
        options = '\n'.join(f'    {cmd} {args}' for cmd, args in self.items())
        return header + options

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

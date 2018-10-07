"""Exceptions."""


__all__ = ['CallbackExistsError', 'MissingPackageError']


class CallbackExistsError(Exception):
    """Indicates that an eponymous callback is already registered."""

    pass


class MissingPackageError(Exception):
    """Indicates that the respective package is missing."""

    def __init__(self, package):
        """Sets the message."""
        super().__init__('Missing pacakge.', package)

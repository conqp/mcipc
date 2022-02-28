"""RCON-related exceptions."""


__all__ = [
    'CommandError',
    'InvalidArgument',
    'InvalidInteger',
    'InvalidNameOrUUID',
    'LocationNotFound',
    'NoPlayerFound',
    'UnexpectedTrailingData',
    'UnknownCommand'
]


class CommandError(Exception):
    """Indicates an error with an RCON command."""


class InvalidArgument(TypeError, CommandError):
    """Represents an invalid argument error."""


class InvalidInteger(ValueError, CommandError):
    """Indicates an invalid integer value."""


class InvalidNameOrUUID(ValueError, CommandError):
    """Indicates an invalid name or UUID."""


class LocationNotFound(CommandError):
    """Indicates that the given location could not be found."""


class NoPlayerFound(CommandError):
    """Indicates that no player was found."""


class UnexpectedTrailingData(CommandError):
    """Indicates unexpected trailing data."""


class UnknownCommand(ValueError, CommandError):
    """Represents an unknown command error."""

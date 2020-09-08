"""RCON exceptions."""


__all__ = [
    'InvalidPacketStructure',
    'InvalidStructure',
    'NotALocation',
    'RequestIdMismatch',
    'WrongPassword'
]


class InvalidPacketStructure(ValueError):
    """Indicates an invalid packet structure."""

    def __init__(self, message, value, expected):
        """Sets an error message, the actual value and the expected value."""
        super().__init__(message, value, expected)
        self.message = message
        self.value = value
        self.expected = expected

    @property
    def description(self):
        """Returns an additional error description."""
        return f'Expected "{self.expected}", but got "{self.value}".'

    def __str__(self):
        """Returns a string representation."""
        return f'{self.message} {self.description}'


class InvalidStructure(ValueError):
    """Indicates that the given Minecraft structure is not valid."""

    def __init__(self, structure):
        """Sets the invalud structure's name."""
        super().__init__(structure)
        self.structure = structure


class NotALocation(ValueError):
    """Indicates that the given text is not a valid location value."""


class RequestIdMismatch(Exception):
    """Indicates that the sent and received request IDs do not match."""

    def __init__(self, sent, received):
        """Sets the sent and received request IDs."""
        super().__init__(sent, received)
        self.sent = sent
        self.received = received


class WrongPassword(Exception):
    """Indicates a wrong RCON password."""

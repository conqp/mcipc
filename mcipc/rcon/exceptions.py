"""RCON exceptions."""


__all__ = [
    'NotALocation',
    'RequestIdMismatch',
    'StructureNotFound',
    'WrongPassword'
]


class NotALocation(ValueError):
    """Indicates that the given text is not a valid location value."""


class RequestIdMismatch(Exception):
    """Indicates that the sent and received request IDs do not match."""

    def __init__(self, sent: int, received: int):
        """Sets the sent and received request IDs."""
        super().__init__(sent, received)
        self.sent = sent
        self.received = received


class StructureNotFound(ValueError):
    """Indicates that the given structure could not be found."""

    def __init__(self, structure):
        """Sets the invalid structure's name."""
        super().__init__(structure)
        self.structure = structure


class WrongPassword(Exception):
    """Indicates a wrong RCON password."""

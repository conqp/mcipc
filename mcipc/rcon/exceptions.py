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


class InvalidStructure(ValueError):
    """Indicates that the given Minecraft structure is not valid."""


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

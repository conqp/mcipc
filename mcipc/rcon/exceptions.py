"""RCON exceptions."""


__all__ = [
    'InvalidPacketStructureError',
    'RequestIdMismatchError',
    'InvalidCredentialsError']


class InvalidPacketStructureError(Exception):
    """Indicates an invalid packet structure."""


class RequestIdMismatchError(Exception):
    """Indicates that the sent and received request IDs do not match."""

    def __init__(self, sent, received):
        """Sets the sent and received request IDs."""
        super().__init__(sent, received)
        self.sent = sent
        self.received = received


class InvalidCredentialsError(Exception):
    """Indicates invalid RCON password."""

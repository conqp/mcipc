"""The actual server."""

from logging import getLogger
from socket import socket

from mcipc.server.datastructures import Handshake, SLPResponse
from mcipc.server.datatypes import VarInt
from mcipc.server.enumerations import State


__all__ = ['StubServer']


LOGGER = getLogger(__file__)


class StubServer:
    """A stub minecraft server."""

    def __init__(self, description, max_players=20, protocol=485):
        """Description, max players and protocol information."""
        self.description = description
        self.max_players = max_players
        self.protocol = protocol

    @property
    def slp_response(self):
        """Returns an SLP response."""
        json = {
            'version': {
                'name': '1.14.2',
                'protocol': self.protocol
            },
            'players': {
                'max': self.max_players,
                'online': 0
            },
            'description': {
                'text': self.description
            }
        }
        return SLPResponse(json)

    @staticmethod
    def _perform_handshake(connection):
        """Handle handshake requests."""
        header = connection.recv(1)
        size = VarInt.from_bytes(header)
        LOGGER.debug('Read size: %s', size)
        payload = connection.recv(size)
        handshake = Handshake.from_bytes(payload)
        LOGGER.debug('Got handshake: %s', handshake)

    def _perform_status(self, connection):
        """Handles status requests."""
        _ = connection.recv(1)  # Discard packet ID.
        response = bytes(self.slp_response)
        connection.send(response)

    def _process(self, connection):
        """Runs the connection processing."""
        state = State.HANDSHAKE

        with connection:
            if state == State.HANDSHAKE:
                LOGGER.debug('HANDSHAKE')
                self._perform_handshake(connection)
                self._perform_status(connection)
                state = State.STATUS
            elif state == State.STATUS:
                LOGGER.debug('STATUS')
                payload = connection.recv(1024)
                LOGGER.debug('Payload: %s', payload)

    def spawn(self, address, port):
        """Spawns the server on the respective socket."""
        with socket() as sock:
            sock.bind((address, port))
            sock.listen()

            while True:
                connection, address = sock.accept()
                LOGGER.debug('New connection from: %s', address)
                self._process(connection)

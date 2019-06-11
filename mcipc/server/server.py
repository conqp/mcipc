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
        return handshake.next_state

    def _perform_status(self, connection):
        """Handles status requests."""
        packet_id = connection.recv(1)

        if packet_id == b'\x01':
            LOGGER.debug('Got packet id: %s', packet_id)
            slp_response = bytes(self.slp_response)
            LOGGER.debug('Sending SLP response: %s', slp_response)
            connection.send(slp_response)

    def _perform_login(self, connection):
        """Handles the login response."""
        raise NotImplementedError()

    def _handle_login(self, connection):
        """Performs a login."""
        header = connection.recv(1)
        size = VarInt.from_bytes(header)
        payload = connection.recv(size)
        packet_id = VarInt.from_bytes(payload[0:1])
        LOGGER.debug('Got packet ID: %s', packet_id)
        user_name = payload[2:].decode('latin-1')
        LOGGER.debug('User "%s" logged in.', user_name)
        self._perform_login(connection)

    def _process(self, connection, state=State.HANDSHAKE):
        """Runs the connection processing."""
        if state == State.HANDSHAKE:
            LOGGER.debug('HANDSHAKE')
            state = self._perform_handshake(connection)
            self._process(connection, state=state)
        elif state == State.STATUS:
            LOGGER.debug('STATUS')
            self._perform_status(connection)
        elif state == State.LOGIN:
            LOGGER.debug('LOGIN')
            self._handle_login(connection)

    def spawn(self, address, port):
        """Spawns the server on the respective socket."""
        with socket() as sock:
            sock.bind((address, port))
            sock.listen()

            while True:
                connection, address = sock.accept()

                with connection:
                    LOGGER.debug('New connection from: %s', address)
                    self._process(connection)

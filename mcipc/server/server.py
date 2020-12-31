"""The actual server."""

from json import dumps
from logging import getLogger
from socket import socket
from typing import IO

from mcipc.server.datastructures import Handshake, SLPResponse
from mcipc.server.datatypes import VarInt
from mcipc.server.enumerations import State


__all__ = ['MAX_PLAYERS', 'PROTOCOL', 'VERSION', 'get_response', 'StubServer']


LOGGER = getLogger(__file__)
MAX_PLAYERS = 20
PROTOCOL = 485
VERSION = '1.16.4'


def get_response(text: str) -> bytes:
    """Returns the response text message."""

    payload = dumps({'text': text}).encode('latin-1')
    payload_length = bytes(VarInt(len(payload)))
    payload = bytes(VarInt(0)) + payload_length + payload
    payload_length = bytes(VarInt(len(payload)))
    return payload_length + payload


class StubServer:
    """A stub minecraft server."""

    def __init__(self, description: str, *, version: str = VERSION,
                 max_players: int = MAX_PLAYERS, protocol: int = PROTOCOL):
        """Description, max players and protocol information."""
        self.description = description
        self.version = version
        self.max_players = max_players
        self.protocol = protocol

    @property
    def slp_content(self) -> dict:
        """Returns the content of an SLP response."""
        return {
            'version': {
                'name': self.version,
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

    @property
    def slp_response(self) -> SLPResponse:
        """Returns an SLP response."""
        return SLPResponse(VarInt(0), self.slp_content)

    @staticmethod
    def _perform_handshake(rfile: IO) -> State:
        """Handle handshake requests."""
        handshake = Handshake.read(rfile)
        LOGGER.debug('Got handshake: %s', handshake)
        return handshake.next_state

    def _perform_status(self, rfile: IO, wfile: IO):
        """Handles status requests."""
        packet_id = rfile.read(1)

        if packet_id == b'\x01':
            LOGGER.debug('Got packet id: %s', packet_id)
            wfile.write(bytes(self.slp_response))

    def _perform_login(self, wfile: IO):
        """Handles the login response."""
        raise NotImplementedError()

    def _handle_login(self, rfile: IO, wfile: IO):
        """Performs a login."""
        size = VarInt.read(rfile)
        packet_id = VarInt.read(rfile)
        packet_id_length = len(bytes(packet_id))
        payload = rfile.read(size - packet_id_length)
        LOGGER.debug('Got packet ID: %s', packet_id)
        user_name = payload[2:].decode('latin-1')
        LOGGER.debug('User "%s" logged in.', user_name)
        self._perform_login(wfile)

    def _process(self, rfile: IO, wfile: IO, state: State = State.HANDSHAKE):
        """Runs the connection processing."""
        LOGGER.debug('Current state: %s', state)

        if state == State.HANDSHAKE:
            state = self._perform_handshake(rfile)
            self._process(rfile, wfile, state=state)
        elif state == State.STATUS:
            self._perform_status(rfile, wfile)
        elif state == State.LOGIN:
            self._handle_login(rfile, wfile)

    def _main_loop(self, sock: socket):
        """Runs the main server loop."""

        conn, addr = sock.accept()

        with conn.makefile('rb') as rfile, conn.makefile('wb') as wfile:
            LOGGER.debug('New connection from: %s', addr)
            self._process(rfile, wfile)

    def spawn(self, address: str, port: int):
        """Spawns the server on the respective socket."""
        with socket() as sock:
            sock.bind((address, port))
            sock.listen()

            while True:
                self._main_loop(sock)

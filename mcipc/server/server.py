"""The actual server."""

from logging import getLogger
from socket import socket

from mcipc.server.datastructures import Handshake, SLPResponse
from mcipc.server.datatypes import VarInt
from mcipc.server.enumerations import State


LOGGER = getLogger(__file__)


def get_slp_response(description, max_players=20, protocol=485):
    """Returns an SLP response."""

    json = {
        'version': {
            'name': '1.14.2',
            'protocol': protocol
        },
        'players': {
            'max': max_players,
            'online': 0
        },
        'description': {
            'text': description
        }
    }
    return SLPResponse(json)


def perform_handshake(connection):
    """Handle handshake requests."""

    header = connection.recv(1)
    size = VarInt.from_bytes(header)
    LOGGER.debug('Read size: %s', size)
    payload = connection.recv(size)
    handshake = Handshake.from_bytes(payload)
    LOGGER.debug('Got handshake: %s', handshake)


def perform_status(connection, slp_response):
    """Handles status requests."""

    _ = connection.recv(1)  # Discard packet ID.
    connection.send(bytes(slp_response))


def process(connection, slp_response):
    """Runs the connection processing."""

    state = State.HANDSHAKE

    with connection:
        if state == State.HANDSHAKE:
            LOGGER.debug('HANDSHAKE')
            perform_handshake(connection)
            perform_status(connection, slp_response)
            state = State.STATUS
        elif state == State.STATUS:
            LOGGER.debug('STATUS')
            payload = connection.recv(1024)
            LOGGER.debug('Payload: %s', payload)


def spawn(address, port, description, max_players=20, protocol=485):
    """Spawns the server on the respective socket."""

    slp_response = get_slp_response(
        description, max_players=max_players, protocol=protocol)

    with socket() as sock:
        sock.bind((address, port))
        sock.listen()

        while True:
            connection, address = sock.accept()
            LOGGER.debug('New connection from: %s', address)
            process(connection, slp_response)

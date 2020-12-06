RCON
====

The `RCON` protocol is used to remotely control a Minecraft server, i.e. execute
commands on a Minecraft server and receive the respective results.

.. warning::

   Enabling RCON on a public IP address may constitute a *information disclosure* and/or a *remote code execution* vulnerability.

To enable `RCON` on a Minecraft server, you must set `enable-rcon = true` in the
server's `server.properties` file.
Furthermore, you need to specify a port for the RCON server by setting `rcon.port = <port>`
and a password by setting `rcon.password = <password>` in the same file.
The following example assumes a server running on `127.0.0.1` and on the RCON port `5000` with password `'mysecretpassword'`:

.. code-block:: python

    from mcipc.rcon import Client

    with Client('127.0.0.1', 5000) as client:
        client.login('mysecretpassword')    # Perform initial login.
        seed = client.seed                  # Get the server's seed.
        players = client.players            # Get the server's players info.
        mansion = client.locate('Mansion')  # Get the next mansion's location.

    print(seed)
    print(players)
    print(mansion)

.. seealso::

    :py:class:`mcipc.rcon.client.Client`

JSON conversion
---------------

:py:class:`mcipc.rcon.datastructures.seed.Seed`, :py:class:`mcipc.rcon.datastructures.players.Players` and :py:class:`mcipc.rcon.datastructures.location.Location` objects provide a *to_json()* method to return their values in a JSON compatible format:

.. code-block:: python

    seed_as_json = seed.to_json()		# Is of type int.
    players_as_json = players.to_json() 	# Is of type dict.
    mansion_as_json = mansion.to_json() 	# Is of type dict.

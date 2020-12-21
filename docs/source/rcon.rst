RCON
====

The `RCON` protocol is used to remotely control a Minecraft server, i.e. execute
commands on a Minecraft server and receive the respective results.

.. warning::

   Enabling RCON on a public IP address may constitute a *information disclosure* and/or a *remote code execution* vulnerability.

To enable `RCON` on a Minecraft server, you must set :code:`enable-rcon = true` in the
server's :file:`server.properties` file.
Furthermore, you need to specify a port for the RCON server by setting :code:`rcon.port = <port>`
and a password by setting :code:`rcon.password = <password>` in the same file.
The following example assumes a server running on :code:`127.0.0.1` and on the RCON port :code:`5000` with password :code:`'mysecretpassword'`:

.. code-block:: python

	from mcipc.be.rcon import Client    # For Bedrock Edition servers.
	from mcipc.ee.rcon import Client    # For Education Edition servers.
	from mcipc.je.rcon import Client    # For Java Edition servers.

	with Client('127.0.0.1', 5000, passwd='mysecretpassword') as client:
	    seed = client.seed                  # Get the server's seed.
	    players = client.players            # Get the server's players info.
	    mansion = client.locate('mansion')  # Get the next mansion's location.

	print(seed)
	print(players)
	print(mansion)

Output of the above example for Java Edition clients:

.. code-block:: python

	-8217057902979500137
	Players(online=1, max=20, players=(Player(name='coNQP', uuid=None, state=None),))
	Location(name='mansion', x=-7216, y=None, z=-1952, distance=7479)

.. seealso::

    Bedrock Edition client: :py:class:`mcipc.rcon.client.be.Client`
    Education Edition client: :py:class:`mcipc.rcon.client.ee.Client`
    Java Edition client: :py:class:`mcipc.rcon.client.je.Client`

JSON conversion
---------------

:py:class:`mcipc.rcon.response_types.seed.Seed`, :py:class:`mcipc.rcon.response_types.players.Players` and :py:class:`mcipc.rcon.response_types.location.Location` objects provide a :code:`to_json()` method to return their values in a JSON compatible format:

.. code-block:: python

    seed_as_json = seed.to_json()		# Is of type int.
    players_as_json = players.to_json() 	# Is of type dict.
    mansion_as_json = mansion.to_json() 	# Is of type dict.

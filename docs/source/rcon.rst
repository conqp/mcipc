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

	from mcipc.rcon.je import Biome, Client     # For Java Edition servers.
	#from mcipc.rcon.be import Client           # For Bedrock Edition servers.
	#from mcipc.rcon.ee import Client           # For Education Edition servers.

	with Client('127.0.0.1', 5000, passwd='mysecretpassword') as client:
	    seed = client.seed					# Get the server's seed.
	    players = client.list()				# Get the server's players info.
	    mansion = client.locate('mansion')			# Get the next mansion's location.
	    badlands = client.locatebiome(Biome.BADLANDS)	# Get the next location of a badlands biome.

	print(seed)
	print(players)
	print(mansion)
	print(badlands)

Example output of the above commands with a Java Edition client:

.. code-block:: python

	-8217057902979500137
	Players(online=1, max=20, players=[Player(name='coNQP', uuid=None, state=None)])
	Location(name='mansion', x=-7216, y=None, z=-1952, distance=7479)
	Location(name='minecraft:badlands', x=1512, y=None, z=3388, distance=3634)

.. seealso::

    * Bedrock Edition client: :py:class:`mcipc.rcon.be.Client`
    * Education Edition client: :py:class:`mcipc.rcon.ee.Client`
    * Java Edition client: :py:class:`mcipc.rcon.je.Client`

JSON serialization
------------------

:py:class:`mcipc.rcon.response_types.players.Players` and :py:class:`mcipc.rcon.response_types.location.Location` objects can be serialized into a JSON-ish `dict` by passing them to the `dict()` constructor:

.. code-block:: python

    players_as_json = dict(players) 	# Is of type dict.
    mansion_as_json = dict(mansion) 	# Is of type dict.

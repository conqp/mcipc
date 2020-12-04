Query
=====

The `Query` protcol is used to query a Minecraft server for server information.
The Minecraft query protocol has two query modes: *basic stats* and *full stats*.

.. warning::

   Enabling Query on a public IP address may consitute a *information disclosure* vulnerability.

Basic stats
-----------

To get *basic stats* from a Minecraft server, it must enable the `Query` protocol.
You can enable the query protocol on a Minecraft server by setting `enable-query = true` in the server's `server.properties` file.
To specify a deviating port, you can set `query.port = <port>` in the same file.
The following example assumes a server running on `127.0.0.1` and on the default query port `25565`:

.. code-block:: python

    from mcipc.query import Client

    with Client('127.0.0.1', 25565) as client:
        basic_stats = client.basic_stats

    print(basic_stats)

The type of `basic_stats` is a named tuple with the following properties:

* `type`: The packet type (`Type`, protocol information).
* `session_id`: The query's session ID (`int`, protocol information).
* `motd`: The server's message of the day (`str`).
* `game_type`: The game type (`str`).
* `map`: The current map (`str`).
* `num_players`: The amount of online players (`int`).
* `max_players`: The amount of maximally allowed players (`int`).
* `host_port`: The server's port (`int`).
* `host_ip`: The server's IP address or hostname (`ipaddress.IPv4Address` or `ipaddress.IPv6Address` or `str`).

Full stats
----------

For retrieving full stats of a server, the same premises apply.

.. code-block:: python

    from mcipc.query import Client

    with Client('127.0.0.1', 25565) as client:
        full_stats = client.full_stats

    print(full_stats)

The type of `full_stats` is a named tuple with the following properties:

* `type`: The packet type (`Type`, protocol information).
* `session_id`: The query's session ID (`int`, protocol information).
* `host_name`: The server's message of the day (`str`, same as BasicStats.motd).
* `game_type`: The game type (`str`).
* `game_id`: The game ID (`str`).
* `version`: The game version (`str`).
* `plugins`: The used plugins (`dict`).
* `map`: The current map (`str`).
* `num_players`: The amount of online players (`int`).
* `max_players`: The amount of maximally allowed players (`int`).
* `host_port`: The server's port (`int`).
* `host_ip`: The server's IP address or hostname (`ipaddress.IPv4Address` or `ipaddress.IPv6Address` or `str`).
* `players`: The names of online players (`tuple` of `str`).

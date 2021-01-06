Query
=====

The `Query` protcol is used to query a Minecraft server for server information.
The Minecraft query protocol has two query modes: *basic stats* and *full stats*.

.. warning::

   Enabling Query on a public IP address may constitute a *information disclosure* vulnerability.

Basic stats
-----------

To get *basic stats* from a Minecraft server, it must enable the `Query` protocol.
You can enable the query protocol on a Minecraft server by setting :code:`enable-query = true` in the server's :file:`server.properties` file.
To specify a deviating port, you can set :code:`query.port = <port>` in the same file.
The following example assumes a server running on :code:`127.0.0.1` and on the default query port :code:`25565`:

.. code-block:: python

    from mcipc.query import Client

    with Client('127.0.0.1', 25565) as client:
        basic_stats = client.stats()

    print(basic_stats)

Full stats
----------

For retrieving full stats of a server, the same premises apply.

.. code-block:: python

    from mcipc.query import Client

    with Client('127.0.0.1', 25565) as client:
        full_stats = client.stats(full=True)

    print(full_stats)

.. seealso::

    :py:class:`mcipc.query.client.Client`

JSON serialization
------------------

Both :py:class:`mcipc.query.proto.basic_stats.BasicStats` and :py:class:`mcipc.query.proto.full_stats.FullStats` objects can be serialized into a JSON-ish `dict` by passing them to the `dict()` constructor:

.. code-block:: python

    basic_stats_as_json = dict(basic_stats)	# Is of type dict.
    full_stats_as_json = dict(full_stats)	# Is of type dict.

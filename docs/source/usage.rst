Usage
=====

The following is applicable to both, `RCON` and `Query` clients.

Handling connection timeouts.
-----------------------------
Since version 1.2.1, you can specify an optional :code:`timeout=<sec>` parameter on both `Query` and `RCON` clients.
If a timeout is reached during a connection attempt, it will raise a `socket.timeout <https://docs.python.org/3/library/socket.html#socket.timeout>`_ exception.
The following example will raise a connection timeout after 1.5 seconds:

.. code-block:: python

    try:
        with Client('127.0.0.1', 5000, timeout=1.5) as client:
            <do_stuff>
    except socket.timeout as timeout:
        <handle_connection_timeout>

.. _configuration:

Configuration
-------------
`queryclt` servers can be configured in :file:`/etc/mcipc.d/query.conf`.
`rconclt` servers can be configured in :file:`/etc/mcipc.d/rcon.conf`.
The configuration file format is:

.. code-block:: ini

    [<server_name>]
    host = <hostname_or_ip_address>
    port = <port>
    passwd = <password>

The :code:`passwd` entry is optional for :file:`rcon.conf` and unnecessary for :file:`query.conf`.

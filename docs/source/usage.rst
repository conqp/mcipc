Usage
=====

The following is applicable to both, `RCON` and `Query` clients.

Handling connection timeouts.
-----------------------------
Since version 1.2.1, you can specify an optional `timeout=<sec>` parameter on both `Query` and `RCON` clients.
If a timeout is reached during a connection attempt, it will raise a `socket.timeout` exception.
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
`queryclt` servers can be configured in `/etc/mcipc.d/query.conf`.\
`rconclt` servers can be configured in `/etc/mcipc.d/rcon.conf`.\
The configuration file format is:

.. code-block:: ini

    [<server_name>]
    host = <hostname_or_ip_address>
    port = <port>
    passwd = <password>

The `passwd` entry is optional for `rcon.conf` and unnecessary for `query.conf`.

Scripts
=======
This library also ships a couple of scripts intended as a proof-of-concept.

* :file:`queryclt`: A `Query` client.
* :file:`rconclt`: An `RCON` client.
* :file:`rconshell`: An interactive `RCON` shell.

queryclt
--------
`queryclt` is a Query client script to communicate with minecraft servers via the Query protocol using the shell.
To communicate with a server, run:

.. code-block:: bash

    queryclt <server> <stats_type> [<args>...] [options]

The placeholder :code:`<server>` can either be a pre-defined server's name (see :ref:`configuration`) or server socket identified by :code:`<host>:<port>`.

rconclt
-------
`rconclt` is an RCON client script to communicate with minecraft servers via the RCON protocol using the shell.
To communicate with a server, run:

.. code-block:: bash

    rconclt <server> <command> [<args>...] [options]

The placeholder :code:`<server>` can either be a pre-defined server's name (see :ref:`configuration`) or server socket identified by :code:`[<password>@]<host>:<port>`.\
If no password was specified in either the pre-defined server entry or the server socket, the script will interactively ask for the server's password.

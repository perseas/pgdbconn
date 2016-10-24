Welcome to PgDbConn's documentation!
====================================

PgDbConn is an offshoot from the Perseas project (started as Pyrseas)
to isolate and generalize the Postgres database connection code so
that it can be used in other Perseas products, such as a web
application to update Postgres tables.

Features
--------

- Connect to a Postgres database with minimal information, creating a
  DbConnection object

- Provide basic methods through the DbConnection object, e.g., fetch,
  execute, commit, rollback

- (planned) Connect using a pool of connections, so that it can be used,
  for example, in a web application


Requirements
------------

- `Postgres <http://www.postgresql.org/>`_  9.2 or higher

- `Python <http://www.python.org/>`_  2.7, or 3.4 or higher

- `Psycopg2 <http://initd.org/psycopg>`_ 2.5 or higher

Contents:

.. toctree::
   :maxdepth: 2

   dbconn


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

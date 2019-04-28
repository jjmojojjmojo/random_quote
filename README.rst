============
random_quote
============

A simple (but not trivial) example application for a blog post about branching and tests

Basic Setup
===========

After cloning this repository, first initialize a virtual environment, then activate it:

.. code:: console
    
    $ python -m venv .
    $ source bin/activate
    
Then install the application:

.. code:: console
    
    $ pip install -e .
    
And the development/testing requirements:

.. code:: console
    
    $ pip install -r requirements.txt
    
Running The Tests
=================
Tests are written with `pytest <https://docs.pytest.org/en/latest/>`__.

They can be invoked like this:

.. code:: console
    
    $ pytest src
    

Initializing The Database And Populating It With Some Quotes
============================================================
Assuming you have a text file called :code:`quotes.txt` with one quote per line, and you want to save your data in :code:`test.db`.

From a python prompt run:

.. code:: pycon
    
    >>> from random_quote import util
    >>> util.init("test.db")
    >>> util.ingest("quotes.txt", "test.db")
    
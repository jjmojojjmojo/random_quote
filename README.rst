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
    

Initializing The Database And Populating It With Some Quotes
============================================================
Assuming you have a text file called :code:`quotes.txt` with one quote per line, and you want to save your data in :code:`test.db`.

From a python prompt run:

.. code:: pycon
    
    >>> from random_quote import util
    >>> util.init("test.db")
    >>> util.ingest("quotes.txt", "test.db")
    
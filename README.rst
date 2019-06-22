============
random_quote
============

A simple (but not trivial) example application for a `blog post about git branching and writing tests with pytest <https://jjmojojjmojo.github.io/branching-git-with-pytest.html>`__.

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
First you will need a CSV file containing quotes and author names. Call it :code:`quotes.csv`.

You can create your own if you'd like. Ensure the first row contains the column names:

.. code:: text
    
    quote,author
    "When I get a little money I buy books; and if any is left, I buy food and clothes.", "Erasmus"
    "Various disguises are regrettable but necessary, If you’re going to make it through the day.", "NoMeansNo"
    
But a script is provided that will generate many (defaults to 1000):

.. code:: console
    
    $ python scripts/generate_quotes.py
    

From a python prompt run:

.. code:: pycon
    
    >>> from random_quote import util
    >>> conn = util.connection_factory("test.db")
    >>> util.init(conn)
    >>> util.ingest("quotes.csv", conn)
    
    
Running The Application
=======================
In :code:`requirements.txt`, `Gunicorn <https://gunicorn.org/>`__ is provided. There is also an example :code:`wsgi.py` file showing how to invoke the :code:`RandomQuoteApp` for use by Gunicorn. 

A basic web instance can be launched like this:

.. code:: console
    
    $ gunicorn wsgi:app
    
The web server will be available at http://127.0.0.1:8000.

Branches
========
To facilitate easier use of the guide that this application was written for, branches are provided in this repository that correspond to various points of progress: 

:code:`part1`
    All the changes from `part 1 <https://jjmojojjmojo.github.io/branching-git-with-pytest.html>`__.
:code:`part2`
    All the changes from `part 1 <https://jjmojojjmojo.github.io/branching-git-with-pytest.html>`__ and
    `part 2 <https://jjmojojjmojo.github.io/branching-git-with-pytest-2.html>`__
:code:`qotd`
    Developer **A**'s feature from `part 3 <https://jjmojojjmojo.github.io/branching-git-with-pytest-3.html>`__.
:code:`index-info`
    Developer **B**'s bug fix from `part 3 <https://jjmojojjmojo.github.io/branching-git-with-pytest-3.html>`__.
:code:`part3`
    All the changes from `part 1 <https://jjmojojjmojo.github.io/branching-git-with-pytest.html>`__, 
    `part 2 <https://jjmojojjmojo.github.io/branching-git-with-pytest-2.html>`__ *and* `part 3 <https://jjmojojjmojo.github.io/branching-git-with-pytest-3.html>`__!
    

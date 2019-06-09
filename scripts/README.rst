=========================================
Helper Scripts And Other Random Utilities
=========================================

This directory contains tools used to generate the ../quotes.csv file in the
parent directory, and a few helper scripts used for developing the guide that utilizes this repo.

The tools use a mix of random selection and a `Markov chain <https://en.wikipedia.org/wiki/Markov_chain>`__ to make realistic-looking data. They use the `markovify <https://github.com/jsvine/markovify>`__ library.

Most users will not need to bother with these scripts (besides :code:`generate_quotes.py`) - they are being provided for academic purposes, reuse by the author, and because it's all kinda neat. Generating realistic random data is a good skill for any programmer to develop.

Using :code:`generate_quotes.py`
================================
From the *parent directory*, once the virtual environment has been enabled and dependencies have been installed, you can simply run the following command to see some helpful instructions:

.. code:: console
    
    (random_quote) $ python scripts/generate_quotes.py --help
    usage: generate_quotes.py [-h] [-o OUTFILE] [-a AUTHORNAMES] [-c CHAINFILE]
                              [-s SEED]
                              [COUNT]
    
    Generate a CSV file containing 1000 random quotes using a Markov chain.
    
    positional arguments:
      COUNT                 Number of quotes to generate. Defaults to 1000.
    
    optional arguments:
      -h, --help            show this help message and exit
      -o OUTFILE, --outfile OUTFILE
                            Output is written to this file as CSV. Default:
                            quotes.csv
      -a AUTHORNAMES, --authornames AUTHORNAMES
                            A JSON list containing the pool of possible author
                            names. Default: scripts/names.json
      -c CHAINFILE, --chainfile CHAINFILE
                            Stored state of markovify markov chain used to
                            generate quotes. Default: scripts/chain.json
      -s SEED, --seed SEED  Seed the random number generator for reproducible
                            results.
                            
Most parameters are self-explanatory. 

Typically, you'd just run the script without any arguments, or possibly specify a smaller or larger number of quotes to generate:

.. code:: console
    
    (random_quote) $ python scripts/generate_quotes.py 10
    

The :code:`-o`, :code:`-a` and :code:`-c` parameters all accept the special :code:`-` value, that will take input or write outout from standard in, or standard out. It's really only useful for the outfile. You can use it like this:

.. code:: console
    
    (random_quote) $ python scripts/generate_quotes.py -o - 1
    quote,author
    "The change of seasons prevented my having any apparent connection with the force of reality. Rendered absolutely insane by the sharper and less disturbed than the crime for which I momentarily expect my release, I repaired to our father!” Her tales are consequently executed in the pursuit of knowledge only discovered to my home, and bending my steps towards the evening. The high mountains and streams and all would be ours on leaving Paris. Our first care after our marriage shall take place, for, my sweet pipings.",Ouail Burbank
    
You could then redirect the output yourself, or chain multiple commands together (untested!).

Generating The Markov Chain
===========================
After enabling the virtual environment and installing dependencies, run:

.. code:: console
    
    (random_quote) $ python scripts/build_markov_chain.py
    
This will overwrite the :code:`chain.json` file in this directory.

The source for the Markov chain is :code:`./source-text`. All files are read into the chain. See `Data Sources`_ for details about the sources provided.

Generating The List Of Author Names
===================================
After enabling the virtual environment and installing dependencies, run:

.. code:: console
    
    (random_quote) $ python scripts/generate_authors.py
    
This will overwrite the :code:`authors.json` file in this directory. See `Data Sources`_ for details about where the names came from.

Bootstrapping A Clone
=====================
Assuming you have this repository checked out with :code:`--bare`, you can use the :code:`init_workspace.sh` script to simulate all of the first few steps from the guide: cloning a working copy, initializing the virtual environment, installing everything and generating :code:`quotes.csv`.

It uses :code:`init_workspace_db.py` to create the database schema and ingest the generated quotes.

Finally, it runs the unit tests.

Data Sources
============

Markov Chain
------------
The data for markov chain generation is pulled from `Project Gutenberg <https://www.gutenberg.org/>`__, specifically all of `Mary Wollstonecraft Shelley <https://www.gutenberg.org/ebooks/author/61>`__'s works.

They were chosen for no other purpose than the fact that her body of work is relatively small in the archive, and all of her work is in the public domain.

The files were downloaded from Project Gutenberg and had their extraneous text (table of contents, introductions, and Project Gutenberg licensing) removed before building the included :code:`chain.json` serialization.

Author Names
------------
The :code:`first-names.txt` and :code:`surnames.txt` files were pulled from https://github.com/smashew/NameDatabases, https://github.com/smashew/NameDatabases/blob/master/NamesDatabases/first%20names/us.txt and https://github.com/smashew/NameDatabases/blob/master/NamesDatabases/surnames/us.txt respectively.

The README notes:

.. code::
    
    This project contains lists of first and last names for different cultural groups and countries, compiled from data freely available on the internet. There are individual lists for
    each country/culture, listed by the ISO language code for the associated language.
    
    Two sets of lists are maintained, if appropriate. The primary list is a normalized
    one, where all non-ASCII vowels have been replaced by their ASCII equivalents. This
    is because of the frequency with which vowels lose their accents when surnames are
    moved across cultural or national frontiers. I have maintained non-ASCII consonants,
    simply because these characters are more commonly retained. However, it would be a
    simple matter to replace these characters with their ASCII equivalents, should this
    be desired. I have also maintained non-normalized versions of these lists, if the
    original database/list maintained non-ASCII vowels.
    
    These lists have been retrieved from the internet, and thus are no more complete
    than the databases that are publicly available. In all cases, credit for the different
    lists is provided in the credits.txt file associated with this project. I have
    chosen publicly available lists where there is little likelihood of copyright
    violation.
    
    Erik Norvelle
    erik dot norvelle at neomailbox dot net
    




"""
API code for dealing with the quote database.
"""

import sqlite3

class RandomQuoteManager:
    def __init__(self, db_filename):
        pass
    
    def add(self, quote):
        """
        Add a quote to the database. Returns the quote's ID.
        """
        
    def get(self, id_):
        """
        Retrieve a specific quote from the database, identified by id_.
        
        Returns a dictionary.
        """
        
    def remove(self, id_):
        """
        Remove a quote from the database by the given id_.
        """
        
    def random(self):
        """
        Return a random quote from the database.
        """
        
    def all(self):
        """
        Return all quotes.
        """
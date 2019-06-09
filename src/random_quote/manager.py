"""
API code for dealing with the quote database.
"""

import datetime
import random

RAND_MIN = -9223372036854775808
RAND_MAX = 9223372036854775807

class RandomQuoteManager:
    def __init__(self, conn):
        self.conn = conn
        
    def _rand(self):
        """
        Return a random integer between RAND_MIN and RAND_MAX (simulates 
        the random() function in sqlite)
        """
        return random.randint(RAND_MIN, RAND_MAX)
        
    def add(self, quote, author="Unknown"):
        """
        Add a quote to the database. Returns the quote's ID.
        """
        c = self.conn.cursor()
        
        c.execute(
            "INSERT INTO quotes (author, quote, rand) VALUES (?, ?, ?)", 
            (author, quote, self._rand()))
        
        self.conn.commit()
        
        return c.lastrowid
        
    def get(self, id_):
        """
        Retrieve a specific quote from the database, identified by id_.
        
        Returns a dictionary.
        """
        c = self.conn.cursor()
        
        c.execute("SELECT id, author, quote, created FROM quotes WHERE id = ?", (id_,))
        
        result = c.fetchone()
        
        if result is None:
            return None
        else:
            return dict(result)
        
    def remove(self, id_):
        """
        Remove a quote from the database by the given id_.
        """
        c = self.conn.cursor()
        
        c.execute("DELETE FROM quotes WHERE id=?", (id_,))
        
        self.conn.commit()
        
    def random(self):
        """
        Return a random quote from the database.
        """
        c = self.conn.cursor()
        rand = self._rand()
        
        c.execute("SELECT id, author, quote, created FROM quotes ORDER BY ABS(rand - ?) LIMIT 1", (rand,))
        
        result = c.fetchone()
        
        if result is None:
            return None
        else:
            return dict(result)
        
    def all(self):
        """
        Return all quotes.
        """
        c = self.conn.cursor()
        
        c.execute("SELECT id, author, quote, created FROM quotes")
        
        result = []
        
        for row in c.fetchall():
            result.append(dict(row))
            
        return result
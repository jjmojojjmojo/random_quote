"""
API code for dealing with the quote database.
"""

import sqlite3

class RandomQuoteManager:
    def __init__(self, db_filename):
        self.db_filemame = db_filename
        self.conn = sqlite3.connect(db_filename)
        self.conn.row_factory = sqlite3.Row
    
    def add(self, quote):
        """
        Add a quote to the database. Returns the quote's ID.
        """
        c = self.conn.cursor()
        
        c.execute("INSERT INTO quotes (quote) VALUES (?)", (quote,))
        
        self.conn.commit()
        
        return c.lastrowid
        
    def get(self, id_):
        """
        Retrieve a specific quote from the database, identified by id_.
        
        Returns a dictionary.
        """
        c = self.conn.cursor()
        
        c.execute("SELECT rowid, quote, created FROM quotes WHERE rowid=?", (id_,))
        
        quote = dict(c.fetchone())
        
        return quote
        
    def remove(self, id_):
        """
        Remove a quote from the database by the given id_.
        """
        c = self.conn.cursor()
        
        c.execute("DELETE FROM quotes WHERE rowid=?", (id_,))
        
        self.conn.commit()
        
    def random(self):
        """
        Return a random quote from the database.
        """
        c = self.conn.cursor()
        
        c.execute("SELECT rowid, quote, created FROM quotes ORDER BY random() LIMIT 1")
        
        quote = dict(c.fetchone())
        
        return quote
        
    def all(self):
        """
        Return all quotes.
        """
        c = self.conn.cursor()
        
        c.execute("SELECT rowid, quote, created FROM quotes")
        
        result = []
        
        for row in c.fetchall():
            result.append(dict(row))
            
        return result
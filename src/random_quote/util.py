"""
Utility functions.
"""
import os
import sqlite3
import csv

def connection_factory(db_filename):
    connection = sqlite3.connect(db_filename)
    connection.row_factory = sqlite3.Row
    
    return connection

def schema():
    """
    Return the location of the SQL schema.
    """
    return os.path.join(os.path.dirname(__file__), "schema.sql")


def ingest(csvfile, db_connection):
    """
    Read a file of quotes and populate the database.
    """
    c = db_connection.cursor()
    
    with open(csvfile, "r", newline="") as quotes:
        reader = csv.DictReader(quotes)
        
        for row in reader:
            c.execute(
                "INSERT INTO quotes (quote, author) VALUES (?, ?)", 
                (row['quote'], row['author']))
            
    db_connection.commit()
    
    
def init(db_connection):
    """
    Create the database schema.
    """
    c = db_connection.cursor()
    
    with open(schema(), "r") as schema_fp:
        queries = schema_fp.read()
        
        c.executescript(queries)
        
    db_connection.commit()
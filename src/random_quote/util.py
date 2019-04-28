"""
Utility functions.
"""
import os
import sqlite3

def ingest(filename, db_filename):
    """
    Read a file of quotes and populate the database.
    """
    conn = sqlite3.connect(db_filename)
    
    c = conn.cursor()
    
    with open(filename, "r") as quotes:
        for line in quotes:
            c.execute("INSERT INTO quotes (quote) VALUES (?)", (line,))
            
    conn.commit()
    
    conn.close()
    
    
def init_with_connection(conn):
    """
    Initialize the database with a given sqlite3 connection object. 
    
    This is broken out to facilitate easier testing - we can initialize the
    database in a test fixture using a single connection.
    """
    c = conn.cursor()
    
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    
    with open(schema_path, "r") as schema_fp:
        queries = schema_fp.read()
        
        c.execute(queries)
        
    conn.commit()
    
def init(db_filename):
    """
    Create the database schema.
    """
    conn = sqlite3.connect(db_filename)
    
    init_with_connection(conn)
        
    conn.close()
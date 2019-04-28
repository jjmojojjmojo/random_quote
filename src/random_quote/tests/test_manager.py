"""
Tests for the RandomQuoteManager class
"""

import pytest
    
def test_add_quote(preconfigured_manager):
    """
    Add a single quote.
    """
    id_ = preconfigured_manager.add("This is a really cool quote")
    
    assert id_ == 4
    
def test_get_quote(preconfigured_manager):
    """
    Get a quote by id
    """
    quote = preconfigured_manager.get(2)
    
    assert quote["quote"] == 'Generic quote 2'
    
def test_remove_quote(preconfigured_manager):
    """
    Remove a single quote
    """
    preconfigured_manager.remove(3)
    
    c = preconfigured_manager.conn.cursor()
    
    c.execute("SELECT * FROM quotes WHERE rowid = ?", (3,))
    
    row = c.fetchone()
    
    assert not row
    
def test_random_quote(preconfigured_manager):
    """
    Retrieve a random quote.
    """
    
    quote = preconfigured_manager.random()
    
    assert quote["rowid"] in [1, 2, 3]
    
def test_all(preconfigured_manager):
    """
    Retrieve a list of all quotes in the DB.
    """
    
    quotes = preconfigured_manager.all()
    
    assert len(quotes) == 3
        
    assert quotes[0]["rowid"] == 1
    assert quotes[0]["quote"] == 'Generic quote 1'
    
    assert quotes[1]["rowid"] == 2
    assert quotes[1]["quote"] == 'Generic quote 2'
    
    assert quotes[2]["rowid"] == 3
    assert quotes[2]["quote"] == 'Generic quote 3'
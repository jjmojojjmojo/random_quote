"""
Tests for the RandomQuoteManager class
"""

import pytest
    
def test_add_quote(preconfigured_manager):
    """
    Add a single quote.
    """
    id_ = preconfigured_manager.add("This is a really cool quote")
    
    assert id_ == 21
    
def test_get_quote(preconfigured_manager):
    """
    Get a quote by id
    """
    quote = preconfigured_manager.get(2)
    
    assert quote["quote"] == 'Generic Quote 2'
    
def test_remove_quote(preconfigured_manager):
    """
    Remove a single quote
    """
    preconfigured_manager.remove(3)
    
    c = preconfigured_manager.conn.cursor()
    
    c.execute("SELECT * FROM quotes WHERE id = ?", (3,))
    
    row = c.fetchone()
    
    assert not row
    
def test_all(preconfigured_manager):
    """
    Retrieve a list of all quotes in the DB.
    """
    
    quotes = preconfigured_manager.all()
    
    assert len(quotes) == 20
        
    assert quotes[0]["id"] == 1
    assert quotes[0]["quote"] == 'Generic Quote 1'
    
    assert quotes[1]["id"] == 2
    assert quotes[1]["quote"] == 'Generic Quote 2'
    
    assert quotes[2]["id"] == 3
    assert quotes[2]["quote"] == 'Generic Quote 3'
    
    assert quotes[19]["id"] == 20
    assert quotes[19]["quote"] == 'Generic Quote 20'
    
def test_random_quote(preconfigured_manager):
    """
    Retrieve a random quote.
    """
    
    quote = preconfigured_manager.random()
    
    assert quote["id"] == 12
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
    
def test_random_quote(preconfigured_manager):
    """
    Retrieve a random quote.
    """
    
    quote = preconfigured_manager.random()
    
    assert quote["id"] == 12
    
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
    
def test_unknown_id(preconfigured_manager):
    """
    Try to get a quote by an unknown id.
    """
    quote = preconfigured_manager.get("zzzzz")

    assert quote is None
    
def test_random_large_number_of_quotes(manager_with_many_quotes):
    """
    Check the results from a large number of quotes.
    """
    random1 = manager_with_many_quotes.random()
    random2 = manager_with_many_quotes.random()
    random3 = manager_with_many_quotes.random()
    random4 = manager_with_many_quotes.random()
    random5 = manager_with_many_quotes.random()
    random6 = manager_with_many_quotes.random()
    random7 = manager_with_many_quotes.random()
    random8 = manager_with_many_quotes.random()
    random9 = manager_with_many_quotes.random()
    random10 = manager_with_many_quotes.random()
    
    assert random1["id"] == 522
    assert random2["id"] == 1742
    assert random3["id"] == 2764
    assert random4["id"] == 1903
    assert random5["id"] == 3586
    assert random6["id"] == 2930
    assert random7["id"] == 350
    assert random8["id"] == 2338
    assert random9["id"] == 3167
    assert random10["id"] == 2323
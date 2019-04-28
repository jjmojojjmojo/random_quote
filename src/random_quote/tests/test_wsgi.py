"""
Functional tests of the WSGI application.
"""

import pytest


def test_get_quote(preconfigured_wsgi_app):
    """
    Make a GET request for a single pre-existing quote.
    """
    response = preconfigured_wsgi_app.get("/quote/1")
    
    assert response.status == '200 OK'
    
    quote = response.json
    
    assert quote["rowid"] == 1
    assert quote["quote"] == 'Generic quote 1'
    
def test_all_quotes(preconfigured_wsgi_app):
    """
    Make a GET request to list all quotes.
    """
    response = preconfigured_wsgi_app.get("/quotes")
    
    assert response.status == '200 OK'
    
    quotes = response.json
    
    assert len(quotes) == 3
        
    assert quotes[0]["rowid"] == 1
    assert quotes[0]["quote"] == 'Generic quote 1'
    
    assert quotes[1]["rowid"] == 2
    assert quotes[1]["quote"] == 'Generic quote 2'
    
    assert quotes[2]["rowid"] == 3
    assert quotes[2]["quote"] == 'Generic quote 3'
    
def test_random_quote(preconfigured_wsgi_app):
    """
    Make a GET request for a single random quote
    """
    response = preconfigured_wsgi_app.get("/random")
    
    assert response.status == '200 OK'
    
    quote = response.json
    
    assert quote["rowid"] in [1, 2, 3]
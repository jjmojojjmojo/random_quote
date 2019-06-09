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
    
    assert quote["id"] == 1
    assert quote["quote"] == 'Generic Quote 1'
    
def test_all_quotes(preconfigured_wsgi_app):
    """
    Make a GET request to list all quotes.
    """
    response = preconfigured_wsgi_app.get("/quotes")
    
    assert response.status == '200 OK'
    
    quotes = response.json
    
    assert len(quotes) == 20
        
    assert quotes[0]["id"] == 1
    assert quotes[0]["quote"] == 'Generic Quote 1'
    
    assert quotes[1]["id"] == 2
    assert quotes[1]["quote"] == 'Generic Quote 2'
    
    assert quotes[2]["id"] == 3
    assert quotes[2]["quote"] == 'Generic Quote 3'
    
    assert quotes[14]["id"] == 15
    assert quotes[14]["quote"] == 'Generic Quote 15'
    
    assert quotes[19]["id"] == 20
    assert quotes[19]["quote"] == 'Generic Quote 20'

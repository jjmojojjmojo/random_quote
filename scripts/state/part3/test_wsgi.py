"""
Functional tests of the WSGI application.
"""

import pytest
import datetime

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
    
def test_random_quote(preconfigured_wsgi_app):
    """
    Make a GET request for a single random quote
    """
    response = preconfigured_wsgi_app.get("/random")

    assert response.status == '200 OK'

    quote = response.json

    assert quote["id"] == 12
    
def test_get_quote_unknown_id(preconfigured_wsgi_app):
    """
    Make a GET request for a single pre-existing quote, but the id doesn't exist.
    """
    response = preconfigured_wsgi_app.get("/quote/zzzzzz", status=404)

    assert response.status == '404 Not Found'
    
def test_get_root(preconfigured_wsgi_app):
    """
    Make a GET request for the root path.
    """
    response = preconfigured_wsgi_app.get("/")
    assert response.content_type == 'text/html'

def test_qotd_empty(preconfigured_wsgi_app):
    """
    Request the list of quotes of the day at /qotd-history - no existing quotes
    """
    response = preconfigured_wsgi_app.get("/qotd-history")

    quotes = response.json

    assert quotes == []

def test_qotd_listing(preconfigured_wsgi_app):
    """
    Request the list of quotes of the day at /qotd-history
    """
    today = datetime.datetime.now()
    quote1 = preconfigured_wsgi_app.app.manager.qotd.get(today)
    quote2 = preconfigured_wsgi_app.app.manager.qotd.get(datetime.datetime(year=2048, month=2, day=26))

    response = preconfigured_wsgi_app.get("/qotd-history")

    quotes = response.json

    assert len(quotes) == 2
    assert quotes[0] == quote1
    assert quotes[1] == quote2

def test_qotd(preconfigured_wsgi_app):
    """
    Retrieve the current quote of the day
    """
    response = preconfigured_wsgi_app.get("/qotd")

    json_quote = response.json

    today = datetime.datetime.now()
    quote = preconfigured_wsgi_app.app.manager.qotd.get(today)

    assert json_quote == quote
    
def test_get_root(preconfigured_wsgi_app):
    """
    Make a GET request for the root path.
    """
    response = preconfigured_wsgi_app.get("/")
    assert response.content_type == 'text/html'

def test_qotd_empty(preconfigured_wsgi_app):
    """
    Request the list of quotes of the day at /qotd-history - no existing quotes
    """
    response = preconfigured_wsgi_app.get("/qotd-history")

    quotes = response.json

    assert quotes == []

def test_qotd_listing(preconfigured_wsgi_app):
    """
    Request the list of quotes of the day at /qotd-history
    """
    today = datetime.datetime.now()
    quote1 = preconfigured_wsgi_app.app.manager.qotd.get(today)
    quote2 = preconfigured_wsgi_app.app.manager.qotd.get(datetime.datetime(year=2048, month=2, day=26))

    response = preconfigured_wsgi_app.get("/qotd-history")

    quotes = response.json

    assert len(quotes) == 2
    assert quotes[0] == quote1
    assert quotes[1] == quote2

def test_qotd(preconfigured_wsgi_app):
    """
    Retrieve the current quote of the day
    """
    response = preconfigured_wsgi_app.get("/qotd")

    json_quote = response.json

    today = datetime.datetime.now()
    quote = preconfigured_wsgi_app.app.manager.qotd.get(today)

    assert json_quote == quote

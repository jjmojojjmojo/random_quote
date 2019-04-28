from random_quote import manager, wsgi, util

import pytest
from webtest import TestApp

@pytest.fixture
def preconfigured_manager():
    """
    Create a RandomQuoteManager, and initialize an in-memory database.
    """
    rqm = manager.RandomQuoteManager(":memory:")
    
    util.init_with_connection(rqm.conn)
    
    c = rqm.conn.cursor()
    
    for quote in ['Generic quote 1', 'Generic quote 2', 'Generic quote 3']:
        c.execute("INSERT INTO quotes (quote) VALUES (?)", (quote,))
    
    rqm.conn.commit()
    
    yield rqm
    
    rqm.conn.close()
    
@pytest.fixture
def preconfigured_wsgi_app(preconfigured_manager):
    """
    Create an instance of RandomQuoteApp, with a preconfigured RandomQuoteManager,
    wrapped in a TestApp instance, ready for functional testing.
    """
    app = TestApp(wsgi.RandomQuoteApp(preconfigured_manager))
    
    yield app
from random_quote import manager, wsgi, util

import pytest
from webtest import TestApp
import random

@pytest.fixture
def preconfigured_manager():
    """
    Create a RandomQuoteManager, and initialize an in-memory database.
    """
    conn = util.connection_factory(":memory:")
    rqm = manager.RandomQuoteManager(conn)
    
    util.init(conn)
    
    c = conn.cursor()
    
    for i in range(1, 21):
        rand = random.randint(manager.RAND_MIN, manager.RAND_MAX)
        c.execute("INSERT INTO quotes (author, quote, rand) VALUES (?, ?, ?)", ("Unknown", f"Generic Quote {i}", rand))
    
    conn.commit()
    
    yield rqm
    
    conn.close()
    
@pytest.fixture
def preconfigured_wsgi_app(preconfigured_manager):
    """
    Create an instance of RandomQuoteApp, with a preconfigured RandomQuoteManager,
    wrapped in a TestApp instance, ready for functional testing.
    """
    
    app = TestApp(wsgi.RandomQuoteApp(preconfigured_manager.conn))
    
    yield app
from random_quote import manager, wsgi, util

import pytest
from webtest import TestApp
import random

@pytest.fixture
def fix_random():
    """
    Seed the random number generator so that we can get reliable, reproducible
    random results.
    """
    random.seed(1)
    yield
    random.seed()

@pytest.fixture
def preconfigured_manager(fix_random):
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
def manager_with_many_quotes(fix_random):
    """
    Create a RandomQuoteManager and add a *lot* of quotes
    """
    conn = util.connection_factory(":memory:")
    
    rqm = manager.RandomQuoteManager(conn)
    util.init(conn)
    
    c = conn.cursor()
    
    for i in range(4000):
        rqm.add(f"Big Quote {i}")
        
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
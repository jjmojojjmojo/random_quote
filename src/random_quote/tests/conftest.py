from random_quote import manager, wsgi, util

import pytest
from webtest import TestApp
import random
import tempfile
import os

@pytest.fixture
def fix_random():
    random.seed(1)
    yield
    random.seed()

@pytest.fixture
def temp_db():
    filehandle, path = tempfile.mkstemp(prefix="random_quote_")
    yield path
    os.unlink(path)

@pytest.fixture
def preconfigured_manager(temp_db, fix_random):
    """
    Create a RandomQuoteManager, and initialize the database.
    """
    rqm = manager.RandomQuoteManager(temp_db)
    
    util.init(temp_db)
    
    c = rqm.conn.cursor()
    
    for i in range(1, 21):
        rand = random.randint(manager.RAND_MIN, manager.RAND_MAX)
        c.execute("INSERT INTO quotes (author, quote, rand) VALUES (?, ?, ?)", ("Unknown", f"Generic Quote {i}", rand))
    
    rqm.conn.commit()
    
    yield rqm
    
    rqm.conn.close()
    
@pytest.fixture
def preconfigured_wsgi_app(temp_db, preconfigured_manager):
    """
    Create an instance of RandomQuoteApp, with a preconfigured RandomQuoteManager,
    wrapped in a TestApp instance, ready for functional testing.
    """
    app = TestApp(wsgi.RandomQuoteApp(temp_db))
    
    yield app
    
    app.app.manager.conn.close()
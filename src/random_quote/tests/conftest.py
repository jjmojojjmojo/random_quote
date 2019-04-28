from random_quote import manager, wsgi, util

import pytest

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
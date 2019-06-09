"""
Quick init tool for workspaces
"""

from random_quote import util

conn = util.connection_factory("test.db")
util.init(conn)
util.ingest("quotes.csv", conn)

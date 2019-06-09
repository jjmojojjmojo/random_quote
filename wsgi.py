from random_quote import wsgi, util

app = wsgi.RandomQuoteApp(util.connection_facotry("test.db"))
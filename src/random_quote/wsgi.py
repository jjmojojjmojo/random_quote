"""
WSGI Applications
"""
from webob import Request, Response

class RandomQuoteApp:
    def __init__(self, db_file=None):
        pass
    
    def __call__(self, environ, start_response):
        """
        Invoke the WSGI application - routing.
        
        Based on the request path, invokes the appropriate method, passing a 
        pre-constructed webob.Request object. 
        
        Expects each method to return a webob.Response object, which will be 
        invoked and returned as per the WSGI protocol.
        """
    
    def get(self, request):
        """
        Return a webob.Response object with a JSON payload containing the
        requested quote. The quote id is specified as the last part of the 
        request path:
            
            /quote/12345
            
        
        """
        
    def random(self, request):
        """
        Return a webob.Response object with a JSON payload containing a quote
        chosen at random.
        """
        
    def listing(self, request):
        """
        Return a webob.Response object with a JSON payload containing an array
        of all quote objects in the database
        """
"""
WSGI Applications
"""
from . import manager
from webob import Request, Response
from webob.exc import HTTPError, HTTPNotFound, HTTPMethodNotAllowed, HTTPBadRequest
import re

class RandomQuoteApp:
    def __init__(self, db_filename):
        self.manager = manager.RandomQuoteManager(db_filename)
    
    def __call__(self, environ, start_response):
        """
        Invoke the WSGI application - routing.
        
        Based on the request path, invokes the appropriate method, passing a 
        pre-constructed webob.Request object. 
        
        Expects each method to return a webob.Response object, which will be 
        invoked and returned as per the WSGI protocol.
        """
        request = Request(environ)
        
        try:
            if request.path == "/quotes":
                response = self.listing(request)
            elif request.path.startswith("/quote"):
                response = self.get(request)
            elif request.path == "/random":
                response = self.random(request)
            else: 
                raise HTTPNotFound()
                
            return response(environ, start_response)
        except HTTPError as error_response:
            return error_response(environ, start_response)
    
    def get(self, request):
        """
        Return a webob.Response object with a JSON payload containing the
        requested quote. The quote id is specified as the last part of the 
        request path:
            
            /quote/12345
            
        
        """
        match = re.search("/([^/]+)$", request.path)
        
        if not match:
            raise HTTPNotFound()
            
        quote = self.manager.get(match.group(1))
        
        if not quote:
            raise HTTPNotFound()
        
        response = Response()
        
        response.json = quote
        
        response.content_type = "application/json"
        
        return response
        
    def random(self, request):
        """
        Return a webob.Response object with a JSON payload containing a quote
        chosen at random.
        """
        response = Response()
        
        response.json = self.manager.random()
        
        response.content_type = "application/json"
        
        return response
        
    def listing(self, request):
        """
        Return a webob.Response object with a JSON payload containing an array
        of all quote objects in the database
        """
        response = Response()
        
        response.json = self.manager.all()
        
        response.content_type = "application/json"
        
        return response
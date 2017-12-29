from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from httphandler import *

class httpserver:
    port = 8888
    data = {}
    def __init__(self):
        server_address = ('', self.port)
        httpd = HTTPServer(server_address, httphandler)
        print 'Starting httpd...'
        httpd.serve_forever()

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from httphandler import *

class httpserver:
    port = 8888
    data = {}
    def __init__(self):
        try:
            server_address = ('', self.port)
            httpd = HTTPServer(server_address, httphandler)
            print 'Starting httpd... '+str(server_address)
            httpd.serve_forever()
        except:
            print "server hatasi"

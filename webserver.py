#!/usr/bin/env python
import cgi
import BaseHTTPServer,CGIHTTPServer
BaseHTTPServer.HTTPServer(( '', 8086 ), CGIHTTPServer.CGIHTTPRequestHandler).serve_forever()

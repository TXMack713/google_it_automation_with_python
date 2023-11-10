#!/usr/bin/env python3

# Google IT Automation with Python
# Configuration Management and the Cloud
# Debug a problem with a Cloud Deployment and Fix it - Qwiklabs Assessment
# Copyright 2019 Google LLC

'''    Testing program for socket
      Author: Jimmy
'''
import http.server
import socketserver
import http

port = 80


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(http.HTTPStatus.INTERNAL_SERVER_ERROR)
        self.end_headers()

        mystring = "500 Internal Server Error!\n"
        self.data = bytes(mystring, 'utf-8')
        self.wfile.write(self.data)


with socketserver.TCPServer(("", port), Handler) as httpd:
    httpd.serve_forever()

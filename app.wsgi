#! /usr/bin/env python

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
from socket import *


html = """
<html>
<body>
%s
</body>
</html>"""

def send_dire(dire):
  HOST = 'localhost'
  PORT = 50007
  s = socket(AF_INET, SOCK_STREAM)
  s.connect((HOST, PORT))
  s.sendall(dire)
  s.close()

def application(environ, start_response):

  # Returns a dictionary containing lists as values.
  d = parse_qs(environ['QUERY_STRING'])

  dire = d.get('dire', [''])[0] # Returns the direction value.

  # Escape input
  dire = escape(dire)

  if not dire in ("left","right","up","down"):
    response_body = ('&quot;%s&quot; ist nicht erlaubt' % dire )
  else:
    response_body = 'alles ok, %s' % dire
    send_dire(dire)

  status = '200 OK'
  response_headers = [('Content-Type', 'text/html'),
                 ('Content-Length', str(len(response_body)))]
  start_response(status, response_headers)

  return response_body

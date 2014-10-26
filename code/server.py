#!/usr/bin/env python

import socket

def server(q):
  HOST = 'localhost'
  PORT = 50007

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((HOST, PORT))
  s.listen(1)
  while 1:
    conn, addr = s.accept()
    print 'Connected by', addr
    while 1:
      data = conn.recv(1024)
      if not data: break
      if q.full():
        q.get_nowait()
      q.put(data)
  conn.close()

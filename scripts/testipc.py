#!/usr/bin/env python

import socket

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print "bind"
s.listen(1)
print "listen"
while 1:
  conn, addr = s.accept()
  print 'Connected by', addr
  while 1:
    data = conn.recv(1024)
    if not data: break
    print data
    #conn.sendall(data)
conn.close()

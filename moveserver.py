#!/usr/bin/python

from multiprocessing import Process, Queue
from server import server
from move import init_servo, move

# curr{4,17} is the current position of the servos, initalized with 1500
global curr17;
global curr4;


def worker(q):
  global curr4, curr17
  while 1:
    dire = q.get()
    curr4, curr17 = move(curr4, curr17, dire)


if __name__ == '__main__':
  curr4, curr17 = init_servo()

  q = Queue()
  server_process = Process(target=server, args=(q,))
  server_process.start()

  worker(q)

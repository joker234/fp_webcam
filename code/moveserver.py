#!/usr/bin/python

from multiprocessing import Process, Lock, Queue
from multiprocessing.sharedctypes import Value
from server import server
from move import init_servo, move
from time import time,sleep

# curr{4,17} is the current position of the servos, initalized with 1500
global curr17;
global curr4;


def worker(move_lock,last_updated,q):
  global curr4, curr17
  while 1:
    dire = q.get()
    move_lock.acquire()
    curr4.value, curr17.value = move(curr4.value, curr17.value, dire)
    move_lock.release()
    last_updated.value = time()


def suspend(move_lock,last_updated,q):
  global curr4, curr17
  suspendtime = 600 # time in seconds after that the raspi will "suspend"
  while 1:
    sleep(1)
    while curr4.value > 1000:
      if last_updated.value + suspendtime < time():
        move_lock.acquire()
        curr4.value, curr17.value = move(curr4.value, curr17.value, "right")
        move_lock.release()
      else:
        break
      sleep(.25)
    while curr17.value > 1000:
      if last_updated.value + suspendtime < time():
        move_lock.acquire()
        curr4.value, curr17.value = move(curr4.value, curr17.value, "down")
        move_lock.release()
      else:
        break
      sleep(.25)


if __name__ == '__main__':
  tmp1, tmp2 = init_servo()
  curr4 = Value('i', tmp1)
  curr17 = Value('i', tmp2)
  last_updated = Value('d',time())
  
  move_lock = Lock()

  q = Queue(5)

  server_process = Process(target=server, args=(q,))
  server_process.start()

  suspend_process = Process(target=suspend, args=(move_lock,last_updated,q,))
  suspend_process.start()

  worker(move_lock,last_updated,q)

#!/usr/bin/python

from RPIO import PWM
from time import sleep
from random import randint
from sys import argv
from os.path import isfile
from multiprocessing import Process, Queue
from server import server

# curr{4,17} is the current position of the servos, initalized with 1500
global curr17;
global curr4;

def init_servo():
  curr4 = 1500
  curr17 = 1500
  go_servo(4, curr4)
  go_servo(17, curr17)
  return curr4, curr17


def go_servo(pin, width):
  servo = PWM.Servo();
  servo.set_servo(pin, width);
  sleep(.3)


def move(direction, step=3):
  if not direction in ("left","right","up","down"):
    print "Ooops! I did it again.";
    print "You should use left, right, up or down.\n";
    return;
  if step < 1:
    print "Ooops! I did it again.";
    print "You should use step >= 1.\n";
    return;

  # tmp: position to move
  # nr:  Number of the GPIO-pin. 4 = vertical move, 17 = horizontal move.
  tmp = None;
  nr = None;
  global curr17;
  global curr4;
  print curr17;
  print curr4;
  step = 10*step;
  if direction == "left":
    print "move %s" % direction;
    nr = 4;
    if curr4 + step <= 2000:
      curr4 += step;
    else:
      curr4 = 2000;
    tmp = curr4;
  elif direction == "right":
    print "move %s" % direction;
    nr = 4;
    if curr4 - step >= 1000:
      curr4 -= step;
    else:
      curr4 = 1000;
    tmp = curr4;
  elif direction == "up":
    print "move %s" % direction;
    nr = 17;
    if curr17 + step <= 2000:
      curr17 += step;
    else:
      curr17 = 2000;
    tmp = curr17;
  elif direction == "down":
    print "move %s" % direction;
    nr = 17;
    if curr17 - step >= 1000:
      curr17 -= step;
    else:
      curr17 = 1000;
    tmp = curr17;
  else:
    print "false usage of move()";

  go_servo(nr, tmp);


def test_servos(max_step=10, iterations=30):
  for i in range(0,iterations):
    movv = ["up","down","left","right"];
    dire = randint(0, 5);
    print movv[dire];
    move(movv[dire],randint(1, max_step));


def worker(q):
  while 1:
    dire = q.get()
    move(dire)


if __name__ == '__main__':
  curr4, curr17 = init_servo()

  q = Queue()
  server_process = Process(target=server, args=(q,))
  server_process.start()

  worker(q)

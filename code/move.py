#!/usr/bin/python

from RPIO import PWM
from time import sleep
from random import randint

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


def move(curr4, curr17, direction, step=3):
  if not direction in ("left","right","up","down","defaultpos"):
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
  elif direction == "defaultpos":
    print "move %s" % direction;
    nr = 4;
    while curr4 > 1500:
      curr4 -= step;
      tmp = curr4;
      go_servo(nr, tmp);
    while curr4 < 1500:
      curr4 += step;
      tmp = curr4;
      go_servo(nr, tmp);
    nr = 17;
    while curr17 > 1500:
      curr17 -= step;
      tmp = curr17;
      go_servo(nr, tmp);
    while curr17 < 1500:
      curr17 += step;
      tmp = curr17;
      go_servo(nr, tmp);
  else:
    print "false usage of move()";

  go_servo(nr, tmp);

  return curr4, curr17


def test_servos(max_step=10, iterations=30):
  curr4, curr17 = init_servo()
  for i in range(0,iterations):
    movv = ["up","down","left","right"];
    dire = randint(0, 3);
    print movv[dire];
    curr4, curr17 = move(curr4, curr17, movv[dire], randint(1, max_step));


if __name__ == '__main__':
  test_servos()

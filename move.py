#!/usr/bin/python

from RPIO import PWM
from time import sleep
from random import randint
from sys import argv
from os.path import isfile


# curr{4,17} is the current position of the servos, initalized with 1500
#curr17;
#curr4;

def init_servo():
  curr4 = 1500
  curr17 = 1500
  go_servo(4, curr4)
  go_servo(17, curr17)
  return curr4, curr17


def get_curr():
  if not isfile('/tmp/curr417'):
    curr4, curr17 = init_servo()
  else: 
    try:
      f = open('/tmp/curr417','r')
      l4 = f.readline()
      l17 = f.readline()
      print f.read()
      curr4 = int(l4.strip())
      curr17 = int(l17.strip())
    except IOError as e:
      print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except ValueError:
      print "Could not convert data to an integer."
      curr4, curr17 = init_servo()
    except:
      print "Unexpected error:", sys.exc_info()[0]
      raise
  return curr4, curr17


def set_curr(curr4, curr17):
  try:
    f = open('/tmp/curr417','w')
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
  except ValueError:
    print "Could not convert data to an integer."
  except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
  f.write("%i\n%i" % (curr4, curr17))


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
  

if __name__ == '__main__':
  curr4, curr17 = get_curr()

  try:
    curr4
    curr17
  except NameError:
    curr4, curr17 = init_servo()

  print argv[1]

  move(argv[1]);
  set_curr(curr4, curr17)

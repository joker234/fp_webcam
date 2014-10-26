#!/usr/bin/python

from RPIO import PWM
from time import sleep
from sys import argv

servo = PWM.Servo()

nr    = int(argv[1])
time  = float(argv[2])
step  = int(argv[3])
start = int(argv[4])
dest  = int(argv[5])

print "Input from command line:\n  nr: %d\n  time: %d\n  step: %d\n  start: %d\n  dest: %d" % (nr,time,step,start,dest)

servo.set_servo(nr, start)
if dest<=start:
  r = range(dest/step, start/step)
  r.reverse()
else:
  r = range(start/step+1, dest/step+1)
print r

for i in r:
  curr = i*step
  servo.set_servo(nr, curr)
  print "state: %i" % (curr)
  if curr != dest:
    sleeptime = time/(abs(start-dest)/step)
    print "sleeptime: %f" % (sleeptime)
    sleep(sleeptime)

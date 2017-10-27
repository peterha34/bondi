#!/usr/bin/python

import subprocess

subprocess.call("raspistill -n -w %s -h %s -t 5 -o treatment2.bmp" % (640, 480), shell=True)
print "pic1"
subprocess.call("raspistill -n -w %s -h %s -t 1200 -o treatment1.bmp" % (640, 480), shell=True)
print "pic2"

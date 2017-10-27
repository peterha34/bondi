#!/usr/bin/python

import subprocess

subprocess.call("raspistill -n -w %s -h %s -t 5 -o withtray.bmp" % (640, 480), shell=True)
print "pic1 taken"
subprocess.call("raspistill -n -w %s -h %s -t 1200 -o baseline.bmp" % (640, 480), shell=True)
print "pic2 taken"

#!/usr/bin/python
import subprocess
from SimpleCV import Image
import time
subprocess.call("raspistill -n -w %s -h %s -o Listato3_1.png" % (640, 480), shell=True)
img = Image("Listato3_1.png")
img.show()
time.sleep(2)
img = img.binarize()
img.show()
time.sleep(2)
macchie = img.findBlobs()
img.show()
time.sleep(2)
print "Areas: ",macchie.area()
print "Angles: ", macchie.angle()
print "Centers: ", macchie.coordinates()
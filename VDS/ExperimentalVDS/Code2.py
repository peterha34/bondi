#!/usr/bin/python
import subprocess
from SimpleCV import Image
import time
subprocess.call("raspistill -n -w %s -h %s -o Listato2_1.png" % (640, 480), shell=True)
img = Image("Listato2_1.png")
img.show()
time.sleep(2)
img = img.binarize()
img.show()
img.save("Listato2_2.png")
time.sleep(2)
macchie = img.findBlobs()
img.save("Listato2_3.png")
img.show()
time.sleep(2)
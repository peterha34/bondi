#!/usr/bin/python
import subprocess
from SimpleCV import Color,Image
import time
subprocess.call("raspistill -n -w %s -h %s -o Listato5_1.png" % (640, 480), shell=True)
img = Image("Listato5_1.png")
img.show()

time.sleep(1)
cerchi = img.findCircle(canny=250,thresh=200,distance=11)
cerchi.draw(color=Color.BLACK, width=4)
cerchi.show()

time.sleep(1)
cerchi = cerchi.sortArea()
cerchi[0].draw(color=Color.Red, width=4)
img_with_circles = img.applyLayers()
img_with_circles.save("Listato5_2.png")
img_with_circles.show()
time.sleep(1)
#!/usr/bin/python
import subprocess
from SimpleCV import Color,Image
import time
subprocess.call("raspistill -n -w %s -h %s -t 1000 -o Listato4_1.png" % (640, 480), shell=True)
img = Image("Listato4_1.png")
img.show()

time.sleep(1)
color = (0, 0, 255)
blue_distance = img.colorDistance(color).invert()
blobs = blue_distance.findBlobs()
blobs.draw(color=Color.BLACK, width=4)
blue_distance.save("Listato4_Bb.png")
blue_distance.show()
time.sleep(1)
img.addDrawingLayer(blue_distance.dl())
img.save("Listato4_Bc.png")
img.show()
time.sleep(1)

img = Image("Listato4_1.png")
img.show()
time.sleep(1)
color = (0, 128, 0)
green_distance = img.colorDistance(color).invert()
blobs = green_distance.findBlobs()
blobs.draw(color=Color.BLACK, width=4)
green_distance.save("Listato4_Gb.png")
green_distance.show()
time.sleep(1)
img.addDrawingLayer(green_distance.dl())
img.save("Listato4_Gc.png")
img.show()
time.sleep(1)

img = Image("Listato4_1.png")
img.show()
time.sleep(1)
color = (255, 0, 0)
red_distance = img.colorDistance(color).invert()
blobs = red_distance.findBlobs()
blobs.draw(color=Color.BLACK, width=4)
red_distance.save("Listato4_Rb.png")
red_distance.show()
time.sleep(1)
img.addDrawingLayer(red_distance.dl())
img.save("Listato4_Rc.png")
img.show()
time.sleep(1)
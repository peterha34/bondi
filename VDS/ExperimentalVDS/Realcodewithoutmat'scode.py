#!/usr/bin/python
import subprocess
from SimpleCV import Color,Image
import time
import csv 
subprocess.call("raspistill -n -w %s -h %s -t 1000 -o Listato4_1.png" % (640, 480), shell=True)
img = Image("Listato4_1.png")
img.show()



#Red Color 

img.show()
time.sleep(1)
color = (255, 0, 0)
red_distance = img.colorDistance(color).invert()
red_distance.show()
blobs = red_distance.findBlobs()
blobs.draw(color=Color.BLUE, width=4)
red_distance.save("Listato4_Rb.png")
red_distance.show()
time.sleep(1)
img.addDrawingLayer(red_distance.dl())
img.save("Listato4_RED.png")
img.show()
blobs.center()
print blobs.center()
with open('Coordinates.csv', 'wb') as csvfile: # creates a new file called Coordinates.csv 
                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(['Color Red']) # writes Color Red in it
                spamwriter.writerow(blobs.center()) # writes all the centered values found earlier on the file

time.sleep(1)

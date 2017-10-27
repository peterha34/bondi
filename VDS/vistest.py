#!/usr/bin/python

import SimpleCV
import collections
import subprocess
import time
import math
import numpy

#subprocess.call("raspistill -n -w %s -h %s -t 500 -o treatment1.bmp" % (640, 480), shell=True)
PointPair = collections.namedtuple('PointPair',['distance','pointA','pointB'], verbose=False)

ColBound = collections.namedtuple('ColBound',['R','G','B'], verbose=False)

colBounds = {'blueLow': ColBound(0,0,100),
              'blueHigh': ColBound(80,200,255)}

# Pixel positions of waste tray comparments in image
col0 = 278
col1 = 333
col2 = 391
row0 = 122
row1 = 175
row2 = 230 

# Size of compartment from image in pizels
cropWide = 30
cropHigh = 30

# Load waste tray image, scale down for faster processing
withouttray = SimpleCV.Image("treatment1.bmp")
withtray = SimpleCV.Image("treatment2.bmp")
img = withouttray - withtray

def findRectPoints(corners):
    pointPairs = []
    i = 0
    for point in corners[i:]:
        for nextPoint in corners[i+1:]:
            pointPairs.append(PointPair(getDistance(point,nextPoint),point,nextPoint))
        i = i+1
    pointPairs.sort(key=lambda x:x[0])
    return pointPairs[-2:];

def getDistance(a, b):
    x1 = float(a.x)
    y1 = float(a.y)
    x2 = float(b.x)
    y2 = float(b.y)
    return math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2));

def getHorizAngle(a, b):
    x1 = float(a.x)
    y1 = float(a.y)
    x2 = float(b.x)
    y2 = float(b.y)
    return numpy.arctan2(y2-y1,x2-x1)

#Center the image to isolate the tray
img = img.crop(img.width/2,img.height/2,img.width/1.8,img.height/1.8,True)

img = img.smooth(algorithm_name='blur').binarize(thresh=(80,80,80))
corners = img.findCorners(mindistance=5,minquality=0.02)

corners = findRectPoints(corners)

for i in corners:
    i.pointA.draw(color=SimpleCV.Color.BLUE, width=4)
    i.pointB.draw(color=SimpleCV.Color.BLUE, width=4)

point1 = corners[0].pointA
point2 = corners[1].pointA
point3 = corners[0].pointB
point4 = corners[1].pointB
print point1, point2
ang = getHorizAngle(point1,point2)
print ang

print corners[0].distance
p12dist = getDistance(point1,point2)
for i in range (0,int(p12dist)+1,int(p12dist/6)):
    pointd1 = point1.x + i*math.cos(ang)
    pointd2 = point1.y + i*math.sin(ang)
    img.drawPoints([(pointd1,pointd2)], color=SimpleCV.Color.RED,width=2)
    
p23dist = getDistance(point2,point3)
for i in range (0,int(p23dist)+1,int(p23dist/6)):
    pointd1 = point2.x + i*math.cos(numpy.deg2rad(90)+ang)
    pointd2 = point2.y + i*math.sin(numpy.deg2rad(90)+ang)
    img.drawPoints([(pointd1,pointd2)], color=SimpleCV.Color.RED,width=2)

p34dist = getDistance(point3,point4)
for i in range (0,int(p34dist)+1,int(p34dist/6)):
    pointd1 = point3.x + i*math.cos(numpy.deg2rad(180)+ang)
    pointd2 = point3.y + i*math.sin(numpy.deg2rad(180)+ang)
    img.drawPoints([(pointd1,pointd2)], color=SimpleCV.Color.RED,width=2)

p41dist = getDistance(point4,point1)
for i in range (0,int(p41dist)+1,int(p41dist/6)):
    pointd1 = point4.x + i*math.cos(numpy.deg2rad(270)+ang)
    pointd2 = point4.y + i*math.sin(numpy.deg2rad(270)+ang)
    img.drawPoints([(pointd1,pointd2)], color=SimpleCV.Color.RED,width=2)
"""for i in range (0,19):
    pointd1 = point1.x + i*(corners[0].distance/18)*math.cos(ang+numpy.deg2rad(45))
    pointd2 = point1.y + i*(corners[0].distance/18)*math.sin(ang+numpy.deg2rad(45))
    img.drawPoints([(pointd1,pointd2)], color=SimpleCV.Color.RED,width=2)"""



img.show()
time.sleep(1)

img = img.toRGB()
# Cropping to isolate compartments and store in list
comp = []
comp.append(img.crop(col0,row0,cropWide,cropHigh,True))
comp.append(img.crop(col1,row0,cropWide,cropHigh,True))
comp.append(img.crop(col2,row0,cropWide,cropHigh,True))
comp.append(img.crop(col0,row1,cropWide,cropHigh,True))
comp.append(img.crop(col2,row1,cropWide,cropHigh,True))
comp.append(img.crop(col0,row2,cropWide,cropHigh,True))
comp.append(img.crop(col1,row2,cropWide,cropHigh,True))
comp.append(img.crop(col2,row2,cropWide,cropHigh,True))

# Iterate through each compartment and detect if disc and color
for i in range (0,len(comp)):
    temp = comp[i].meanColor()
    print "Comp%d: r:%d, g:%d, b:%d" %(i,temp[0],temp[1],temp[2])

    if temp[0]>=colBounds['blueLow'].R and temp[0]<=colBounds['blueHigh'].R and\
        temp[1]>=colBounds['blueLow'].G and temp[1]<=colBounds['blueHigh'].G and\
        temp[2]>=colBounds['blueLow'].B and temp[2]<=colBounds['blueHigh'].B:
            print "It's blue"
    else:
        print "WOT IS THIS SHIT(LITERALLY)"

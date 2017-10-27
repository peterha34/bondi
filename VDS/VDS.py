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
DiscBox = collections.namedtuple('DiscBox',['x','y'], verbose=False)

colBounds = {'blueLow': ColBound(0,0,100),
              'blueHigh': ColBound(80,200,255)}

# Load waste tray image
baseline = SimpleCV.Image("treatment1.bmp")
withtray = SimpleCV.Image("treatment2.bmp")

# Crop the image to isolate the tray and speed up processing
imgWidth = withtray.width
imgHeight = withtray.height
scale = 0.625
baseline = baseline.crop(imgWidth*0.5,imgHeight*0.5,imgWidth*scale,imgHeight*scale,True)
withtray = withtray.crop(imgWidth*0.5,imgHeight*0.5,imgWidth*scale,imgHeight*scale,True)

img = baseline - withtray

def findCornerPoints(corners):
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
    return numpy.arctan2(y2-y1,x2-x1);

def identifyRectPoints(corners):
    rect = {'topLeft': None,'topRight': None,
                   'bottomLeft': None,'bottomRight': None }
    for pair in corners:
        if pair.pointA.above(pair.pointB):
            if pair.pointA.left(pair.pointB):
                rect['topLeft'] = pair.pointA
                rect['bottomRight'] = pair.pointB
            else:
                rect['topRight'] = pair.pointA
                rect['bottomLeft'] = pair.pointB 
        else:
            if pair.pointA.left(pair.pointB):
                rect['bottomLeft'] = pair.pointA
                rect['topRight'] = pair.pointB
            else:
                rect['bottomRight'] = pair.pointA
                rect['topLeft'] = pair.pointB 

    return rect;

def getTraySlots(img):
    slots = []
    img = img.smooth(algorithm_name='blur').binarize(thresh=(80,80,80))
    corners = img.findCorners(mindistance=5,minquality=0.02)
    corners = findCornerPoints(corners)
    corners = identifyRectPoints(corners)
    angleOffset = getHorizAngle(corners['topLeft'],corners['topRight'])

    p12dist = getDistance(corners['topLeft'],corners['topRight'])        
    p23dist = getDistance(corners['topRight'],corners['bottomRight'])
    p34dist = getDistance(corners['bottomRight'],corners['bottomLeft'])
    p41dist = getDistance(corners['bottomLeft'],corners['topLeft'])

    slots.append((p12dist+p23dist+p34dist+p41dist)/20.0)
    for i in range(1,6,2):
        for j in range(1,6,2):
            x = corners['topLeft'].x + j*(p12dist/6.0)*math.cos(angleOffset) + i*(p23dist/6.0)*math.cos(numpy.deg2rad(90)+angleOffset)
            y = corners['topLeft'].y + j*(p12dist/6.0)*math.sin(angleOffset) + i*(p23dist/6.0)*math.sin(numpy.deg2rad(90)+angleOffset)
            img.drawPoints([(x,y)], color=SimpleCV.Color.RED,width=2)
            slots.append(DiscBox(x,y))
            img.show()
            time.sleep(2)

    return slots;

slotCoords = getTraySlots(img)

withtray = withtray.toRGB()
# Cropping to isolate compartments and store in list
comp = []
cropSize = slotCoords[0]
for i in range(1,len(slotCoords)):
    comp.append(withtray.crop(slotCoords[i].x,slotCoords[i].y,cropSize,cropSize,True))


# Iterate through each compartment and detect if disc and color
for i in range (0,len(comp)):
    comp[i].show()
    time.sleep(2)
    temp = comp[i].meanColor()
    print "Comp%d: r:%d, g:%d, b:%d" %(i,temp[0],temp[1],temp[2])

    if temp[0]>=colBounds['blueLow'].R and temp[0]<=colBounds['blueHigh'].R and\
        temp[1]>=colBounds['blueLow'].G and temp[1]<=colBounds['blueHigh'].G and\
        temp[2]>=colBounds['blueLow'].B and temp[2]<=colBounds['blueHigh'].B:
            print "It's blue"
    else:
        print "WOT IS THIS SHIT(LITERALLY)"

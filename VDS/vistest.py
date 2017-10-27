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
        x1 = pair.pointA.x
        y1 = pair.pointA.y
        x2 = pair.pointB.x
        y2 = pair.pointB.y
        if rect['topLeft']:
            if (x1-x2)>0 and (x1-rect['topLeft'].x)>0:
                rect['topRight'] = pair.pointA
                rect['bottomLeft'] = pair.pointB
            else:
                rect['topLeft'] = pair.pointB
                rect['bottomRight'] = pair.pointA
        elif (x1-x2)>0:
            rect['topLeft'] = pair.pointB
            rect['bottomRight'] = pair.pointA
            rect['topRight'] = pair.pointA
            rect['bottomLeft'] = pair.pointB
        else:
            rect['topLeft'] = pair.pointA
            rect['bottomRight'] = pair.pointB
            rect['topRight'] = pair.pointB
            rect['bottomLeft'] = pair.pointA

    return rect;

def getTraySlots(img):
    #Center the image to isolate the tray
    img = img.crop(img.width/2,img.height/2,img.width/1.8,img.height/1.8,True)
    img = img.smooth(algorithm_name='blur').binarize(thresh=(80,80,80))
    corners = img.findCorners(mindistance=5,minquality=0.02)
    corners = findCornerPoints(corners)
    corners = identifyRectPoints(corners)
    angleOffset = getHorizAngle(corners['topLeft'],corners['topRight'])

    p12dist = getDistance(corners['topLeft'],corners['topRight'])
    for i in range (0,7):
        pointd1 = corners['topLeft'].x + (p12dist/6.0)*i*math.cos(angleOffset)
        pointd2 = corners['topLeft'].y + (p12dist/6.0)*i*math.sin(angleOffset)
        img.drawPoints([(pointd1,pointd2)], color=SimpleCV.Color.RED,width=2)
        
    p23dist = getDistance(corners['topRight'],corners['bottomRight'])
    for i in range (0,7):
        pointd1 = corners['topRight'].x + (p23dist/6.0)*i*math.cos(numpy.deg2rad(90)+angleOffset)
        pointd2 = corners['topRight'].y + (p23dist/6.0)*i*math.sin(numpy.deg2rad(90)+angleOffset)
        img.drawPoints([(pointd1,pointd2)], color=SimpleCV.Color.RED,width=2)

    p34dist = getDistance(corners['bottomRight'],corners['bottomLeft'])
    for i in range (0,7):
        pointd1 = corners['bottomRight'].x + (p34dist/6.0)*i*math.cos(numpy.deg2rad(180)+angleOffset)
        pointd2 = corners['bottomRight'].y + (p34dist/6.0)*i*math.sin(numpy.deg2rad(180)+angleOffset)
        img.drawPoints([(pointd1,pointd2)], color=SimpleCV.Color.RED,width=2)

    p41dist = getDistance(corners['bottomLeft'],corners['topLeft'])
    for i in range (0,7):
        pointd1 = corners['bottomLeft'].x + (p41dist/6.0)*i*math.cos(numpy.deg2rad(270)+angleOffset)
        pointd2 = corners['bottomLeft'].y + (p41dist/6.0)*i*math.sin(numpy.deg2rad(270)+angleOffset)
        img.drawPoints([(pointd1,pointd2)], color=SimpleCV.Color.RED,width=2)

    columnx = (p12dist/6.0)*math.cos(angleOffset)
    columny= (p12dist/6.0)*math.sin(angleOffset)

    rowx = (p23dist/6.0)*math.cos(angleOffset)
    rowy= (p23dist/6.0)*math.sin(angleOffset)

    compart1x = corners['topLeft'].x + 1*(p12dist/6.0)*math.cos(angleOffset) + 1*(p23dist/6.0)*math.cos(numpy.deg2rad(90)+angleOffset)
    compart1y = corners['topLeft'].y + 1*(p12dist/6.0)*math.sin(angleOffset) + 1*(p23dist/6.0)*math.sin(numpy.deg2rad(90)+angleOffset)
    img.drawPoints([(compart1x,compart1y)], color=SimpleCV.Color.GREEN ,width=2)

    compart2x = corners['topLeft'].x + 3*(p12dist/6.0)*math.cos(angleOffset) + (1.0/6)*p23dist*math.cos(numpy.deg2rad(90)+angleOffset)
    compart1y = corners['topLeft'].y + 3*(p12dist/6.0)*math.sin(angleOffset) + (1.0/6)*p23dist*math.sin(numpy.deg2rad(90)+angleOffset)
    img.drawPoints([(compart2x,compart1y)], color=SimpleCV.Color.GREEN ,width=2)

    compart3x = corners['topLeft'].x + 5*(p12dist/6.0)*math.cos(angleOffset) + (1.0/6)*p23dist*math.cos(numpy.deg2rad(90)+angleOffset)
    compart1y = corners['topLeft'].y + 5*(p12dist/6.0)*math.sin(angleOffset) + (1.0/6)*p23dist*math.sin(numpy.deg2rad(90)+angleOffset)
    img.drawPoints([(compart3x,compart1y)], color=SimpleCV.Color.GREEN ,width=2)

    compart1x = corners['topLeft'].x + 1*(p12dist/6.0)*math.cos(angleOffset) + (3.0/6)*p23dist*math.cos(numpy.deg2rad(90)+angleOffset)
    compart2y = corners['topLeft'].y + 1*(p12dist/6.0)*math.sin(angleOffset) + (3.0/6)*p23dist*math.sin(numpy.deg2rad(90)+angleOffset)
    img.drawPoints([(compart1x,compart2y)], color=SimpleCV.Color.GREEN ,width=2)

    compart2x = corners['topLeft'].x + 3*(p12dist/6.0)*math.cos(angleOffset) + (3.0/6)*p23dist*math.cos(numpy.deg2rad(90)+angleOffset)
    compart2y = corners['topLeft'].y + 3*(p12dist/6.0)*math.sin(angleOffset) + (3.0/6)*p23dist*math.sin(numpy.deg2rad(90)+angleOffset)
    img.drawPoints([(compart2x,compart2y)], color=SimpleCV.Color.GREEN ,width=2)

    compart3x = corners['topLeft'].x + 5*(p12dist/6.0)*math.cos(angleOffset) + (3.0/6)*p23dist*math.cos(numpy.deg2rad(90)+angleOffset)
    compart2y = corners['topLeft'].y + 5*(p12dist/6.0)*math.sin(angleOffset) + (3.0/6)*p23dist*math.sin(numpy.deg2rad(90)+angleOffset)
    img.drawPoints([(compart3x,compart2y)], color=SimpleCV.Color.GREEN ,width=2)

    compart1x = corners['topLeft'].x + (1.0/6)*p12dist*math.cos(angleOffset) + (5.0/6)*p23dist*math.cos(numpy.deg2rad(90)+angleOffset)
    compart3y = corners['topLeft'].y + (1.0/6)*p12dist*math.sin(angleOffset) + (5.0/6)*p23dist*math.sin(numpy.deg2rad(90)+angleOffset)
    img.drawPoints([(compart1x,compart3y)], color=SimpleCV.Color.GREEN ,width=2)

    compart2x = corners['topLeft'].x + (3.0/6)*p12dist*math.cos(angleOffset) + (5.0/6)*p23dist*math.cos(numpy.deg2rad(90)+angleOffset)
    compart3y = corners['topLeft'].y + (3.0/6)*p12dist*math.sin(angleOffset) + (5.0/6)*p23dist*math.sin(numpy.deg2rad(90)+angleOffset)
    img.drawPoints([(compart2x,compart3y)], color=SimpleCV.Color.GREEN ,width=2)

    compart3x = corners['topLeft'].x + (5.0/6)*p12dist*math.cos(angleOffset) + (5.0/6)*p23dist*math.cos(numpy.deg2rad(90)+angleOffset)
    compart3y = corners['topLeft'].y + (5.0/6)*p12dist*math.sin(angleOffset) + (5.0/6)*p23dist*math.sin(numpy.deg2rad(90)+angleOffset)
    img.drawPoints([(compart3x,compart3y)], color=SimpleCV.Color.GREEN ,width=2)

    img.show()

slotCoords = getTraySlots(img)

withtray = withtray.toRGB()
# Cropping to isolate compartments and store in list
comp = []
comp.append(withtray.crop(col0,row0,cropWide,cropHigh,True))
comp.append(withtray.crop(col1,row0,cropWide,cropHigh,True))
comp.append(withtray.crop(col2,row0,cropWide,cropHigh,True))
comp.append(withtray.crop(col0,row1,cropWide,cropHigh,True))
comp.append(withtray.crop(col2,row1,cropWide,cropHigh,True))
comp.append(withtray.crop(col0,row2,cropWide,cropHigh,True))
comp.append(withtray.crop(col1,row2,cropWide,cropHigh,True))
comp.append(withtray.crop(col2,row2,cropWide,cropHigh,True))
withtray.show()
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

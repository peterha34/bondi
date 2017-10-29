#!/usr/bin/python

import SimpleCV
import collections
import subprocess
import time
import math
import numpy

PointPair = collections.namedtuple('PointPair',['distance','pointA','pointB'], verbose=False)
ColBound = collections.namedtuple('ColBound',['R','G','B'], verbose=False)
DiscBox = collections.namedtuple('DiscBox',['x','y'], verbose=False)

colBounds = {'blackLow': ColBound(0,0,0), 'blackHigh': ColBound(180,255,51),
             'blueLow': ColBound(85,25,60), 'blueHigh': ColBound(130,255,225),
             'redLow': ColBound(0,25,60), 'redHigh': ColBound(15,255,225),
             'red2Low': ColBound(170,25,60), 'red2High': ColBound(180,255,225),
             'greenLow': ColBound(40,25,60), 'greenHigh': ColBound(85,255,225)}
TRAY_CODE = 0
RED_CODE = 1
BLUE_CODE = 2
GREEN_CODE = 3
UNIDENTIFIED_CODE = 9

BASELINE_FILE_NAME = "baseline.bmp"
TRAYIMAGE_FILE_NAME = "trayImg.bmp"
CROP_SCALE = 0.625
 
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
    diagPoints = findCornerPoints(corners)
    rectPoints = identifyRectPoints(diagPoints)
    angleOffset = getHorizAngle(rectPoints['topLeft'],rectPoints['topRight'])
   
    p12dist = getDistance(rectPoints['topLeft'],rectPoints['topRight'])        
    p23dist = getDistance(rectPoints['topRight'],rectPoints['bottomRight'])
    p34dist = getDistance(rectPoints['bottomRight'],rectPoints['bottomLeft'])
    p41dist = getDistance(rectPoints['bottomLeft'],rectPoints['topLeft'])

    slots.append((p12dist+p23dist+p34dist+p41dist)/22.0)
    
    for i in range(1,6,2):
        for j in range(1,6,2):
            x = rectPoints['topLeft'].x + j*((p12dist+p34dist)/12.0)*math.cos(angleOffset) + i*((p23dist+p41dist)/12.0)*math.cos(numpy.deg2rad(90)+angleOffset)
            y = rectPoints['topLeft'].y + j*((p12dist+p34dist)/12.0)*math.sin(angleOffset) + i*((p23dist+p41dist)/12.0)*math.sin(numpy.deg2rad(90)+angleOffset)
            img.drawPoints([(x,y)], color=SimpleCV.Color.RED,width=2)
            slots.append(DiscBox(x,y))
    return slots;

def loadImages(): 
    # Load waste tray image
    baseline = SimpleCV.Image(BASELINE_FILE_NAME)
    trayImg = SimpleCV.Image(TRAYIMAGE_FILE_NAME)

    # Crop the image to isolate the tray and speed up processing
    imgWidth = trayImg.width
    imgHeight = trayImg.height
    baseline = baseline.crop(imgWidth*0.5,imgHeight*0.5,imgWidth*CROP_SCALE,imgHeight*CROP_SCALE,True)
    trayImg = trayImg.crop(imgWidth*0.5,imgHeight*0.5,imgWidth*CROP_SCALE,imgHeight*CROP_SCALE,True)
    diff = baseline - trayImg
    
    return baseline,trayImg,diff;

def formatVDSMessage(compartments):
    result = [0,0,0,0,0,0,0,0,0]  
    # Iterate through each compartment and identify colour
    for i in range (0,len(compartments)):
        # Convert image to RGB to match our colour space
        compartments[i] = compartments[i].toHSV()
        result[i] = str(identifyColour(compartments[i].meanColor()))
    result.pop(4)
    return "VISION_DATA:"+",".join(result);

def identifyColour(RGBvalue):
    
    if isColour(RGBvalue, "blue"):
            return BLUE_CODE;
    elif isColour(RGBvalue, "red"):
            return RED_CODE;
    elif isColour(RGBvalue, "red2"):
            return RED_CODE; 
    elif isColour(RGBvalue, "green"):
            return GREEN_CODE;       
    elif isColour(RGBvalue, "black"):
            return TRAY_CODE;
    return UNIDENTIFIED_CODE;

def isColour(RGBvalue, colour):
    colLow = colour+"Low"
    colHigh = colour+"High"

    if RGBvalue[0]>=colBounds[colLow].R and RGBvalue[0]<=colBounds[colHigh].R and\
    RGBvalue[1]>=colBounds[colLow].G and RGBvalue[1]<=colBounds[colHigh].G and\
    RGBvalue[2]>=colBounds[colLow].B and RGBvalue[2]<=colBounds[colHigh].B:
        return True;
    return False;
    
def detectWasteType():
    baseline,trayImg,diff = loadImages()
    #Attempt to identify waste tray compartment coords
    slotCoords = getTraySlots(diff)
    compartments = []
    # Retrieve compartment size stored as first element in list
    cropSize = slotCoords[0]
    # Then crop and store image area around compartment coordinates 
    for i in range(1,len(slotCoords)):
        compartments.append(trayImg.crop(slotCoords[i].x,slotCoords[i].y,cropSize,cropSize,True))

    return formatVDSMessage(compartments);
    
print detectWasteType()

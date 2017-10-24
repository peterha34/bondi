import SimpleCV
import collections


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
img = SimpleCV.Image("treatment.jpg")
img = img.scale(640,360)
img = img.toRGB()

""" This opens the image in an interactive view window
img.live() """

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

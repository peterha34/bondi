import SimpleCV

boundaries = [ #lower, upper values RGB
	([0, 0, 100], [80, 200, 255]), #blue
]

col0 = 278
col1 = 333
col2 = 391
row0 = 122
row1 = 175
row2 = 230

img = SimpleCV.Image("treatment.jpg")
img = img.scale(640,360)
img = img.toRGB()
# img.live()

comp = []
comp.append(img.crop(col0,row0,30,30,True))
comp.append(img.crop(col1,row0,30,30,True))
comp.append(img.crop(col2,row0,30,30,True))
comp.append(img.crop(col0,row1,30,30,True))
comp.append(img.crop(col2,row1,30,30,True))
comp.append(img.crop(col0,row2,30,30,True))
comp.append(img.crop(col1,row2,30,30,True))
comp.append(img.crop(col2,row2,30,30,True))

for i in range (0,8):
    temp = comp[i].meanColor()
    print "Comp%d: r:%d, g:%d, b:%d" %(i,temp[0],temp[1],temp[2])

    if temp[0]>=boundaries[0][0][0] and temp[1]>=boundaries[0][0][1] and temp[2]>=boundaries[0][0][2]\
        and temp[0]<=boundaries[0][1][0] and temp[1]<=boundaries[0][1][1] and temp[2]<=boundaries[0][1][2]:
            print "It's blue"
    else:
        print "WOT IS THIS SHIT(LITERALLY)"

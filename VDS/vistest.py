import SimpleCV

boundaries = [ #lower, upper values RGB
	([0, 0, 100], [80, 200, 255]), #blue
]

img = SimpleCV.Image("treatment.jpg")
img = img.scale(640,360)
img = img.toRGB()
# img.live()

comp = []
comp.append(img.crop(278,122,30,30,True))
comp.append(img.crop(333,122,30,30,True))
comp.append(img.crop(391,122,30,30,True))
comp.append(img.crop(278,175,30,30,True))
comp.append(img.crop(391,175,30,30,True))
comp.append(img.crop(277,230,30,30,True))
comp.append(img.crop(333,230,30,30,True))
comp.append(img.crop(391,230,30,30,True))

for i in range (0,8):
    temp = comp[i].meanColor()
    print "Comp%d: r:%d, g:%d, b:%d" %(i,temp[0],temp[1],temp[2])

    if temp[0]>=boundaries[0][0][0] and temp[1]>=boundaries[0][0][1] and temp[2]>=boundaries[0][0][2]:
        if temp[0]<=boundaries[0][1][0] and temp[1]<=boundaries[0][1][1] and temp[2]<=boundaries[0][1][2]:
            print "It's blue"

    else:
        print "WOT IS THIS SHIT(LITERALLY)"


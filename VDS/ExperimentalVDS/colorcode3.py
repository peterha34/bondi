#!/usr/bin/python
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])





	lower = np.array([110, 50, 50])
	upper = np.array([130,255,255])

	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)



cv2.imshow("image", np.hstack([image, output]))
#cv2.imwrite("T.png",np.hstack([image, output]))
cv2.waitKey(0)

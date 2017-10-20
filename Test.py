#!/usr/bin/python # shebang used for python
import subprocess # imports all subproccess that may be required for the code
import csv 
from SimpleCV import Color,Image, DrawingLayer, Camera # Imports specific modules from simpleCV
import time
import socket

imageCommand = "GET_IMAGE"
ip = 192.168.1.2
port = 8080
serversocket.listen(1)
while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if buf == imageCommand
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind((ip,port))
        subprocess.call("raspistill -n -w %s -h %s -t 1000 -o Normal.png" % (640, 480), shell=True) #Camera module takes a picture after 5 second
        img = Image("Normal.png") # Loads the image on the img variable
        img.show() #  Shows the image on screen 

        time.sleep(1) # pauses the program for 1 second
        blue_distance = img.colorDistance(Color.BLUE).invert() # finds the color blue within the image, finds how far other colors are from Blue and inverts them further.
        blobs = blue_distance.findBlobs() # finds the major blobs that meet the color values set earlier
        blobs.draw(color=Color.WHITE, width=3) # finds blobs of color Blue in the image and highlights them with a white color with a width of 4
        blue_distance.show() # shows the color blue and how far other colors are from it within the image
        blobs.center() # finds centre position of blobs found
        time.sleep(1)
        img.addDrawingLayer(blue_distance.dl()) # adds the original image on top of detection image as a drawing layer
        print blobs.center() # prints the centre of blobs on cmd with x & y co ordinates 
        img.save("Center.png") # Saves the combined image
        img.show() # Shows the final saved image
        with open('Coordinates.csv', 'wb') as csvfile: # creates a new file called Coordinates.csv 
                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(['Color Blue']) # writes Color Blue in it
                spamwriter.writerow(blobs.center()) # writes all the centered values found earlier on the file

        time.sleep(1) 


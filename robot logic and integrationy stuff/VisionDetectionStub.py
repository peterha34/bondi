#!/usr/bin/env python
'''
A stub used to emulate the behaviour of the completed vision detection sybsystem
Author: MM
'''

#!/usr/bin/python # shebang used for python
import subprocess # imports all subproccess that may be required for the code
import csv
from SimpleCV import Color,Image, DrawingLayer, Camera # Imports specific modules from simpleCV
import time
import socket

ROBOT_IP = "192.168.1.2"
IMAGE_COMMAND = "GET_IMAGE"
IP = "192.168.1.2"
SERVER_PORT = 8081
CLIENT_PORT = 8091

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((IP, SERVER_PORT))
serversocket.listen(1)
while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if buf == IMAGE_COMMAND:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect((ROBOT_IP, CLIENT_PORT))
        clientsocket.send("VISION_DATA:1,2,3,1,2,3,1,2")
        time.sleep(1)
        clientsocket.close()
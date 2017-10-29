#!/usr/bin/env python
'''
A stub used to emulate the behaviour of the completed vision detection sybsystem
Author: MM
'''

#!/usr/bin/python # shebang used for python
import subprocess # imports all subproccess that may be required for the code
import time
import socket
import VDS

ROBOT_IP = "192.168.1.5"
IMAGE_COMMAND = "GET_IMAGE"
BASELINE_COMMAND = "GET_BASELINE"
IP = "192.168.1.2"
SERVER_PORT = 8081
CLIENT_PORT = 8080

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((IP, SERVER_PORT))
serversocket.listen(1)
while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if buf == BASELINE_COMMAND:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect((ROBOT_IP, CLIENT_PORT))
        clientsocket.send(VDS.captureBaseline())
        time.sleep(1)
        clientsocket.close()
    if buf == IMAGE_COMMAND:
        VDS.captureTray()
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect((ROBOT_IP, CLIENT_PORT))
        clientsocket.send(VDS.detectWasteType())
        time.sleep(1)
        clientsocket.close()

import socket
import time
from threading import Thread
import motortest as conveyor

myIP = '192.168.1.3'

def stopmytits():
    port = 8090
    serversocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket1.bind((myIP, port))
    serversocket1.listen(1) # become a server socket, maximum 5 connections
    while True:
        print("loopin thread2\n")
        connection1, address1 = serversocket1.accept()
        buf1 = connection1.recv(64)
        if buf1 == "stop":
            print "stop"
            conveyor.stop()
        time.sleep(0.5)

Thread(target=stopmytits,args=()).start()
port = 8091
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((myIP, port))
serversocket.listen(1) # become a server socket, maximum 5 connections

while True:
    print("loopin")
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if buf == "left":
        print "left"
        conveyor.move(0,10)
    elif buf == "right":
        print "right"
        conveyor.move(1,10)
    else:
        print "This is my last resport"
    time.sleep(0.5)

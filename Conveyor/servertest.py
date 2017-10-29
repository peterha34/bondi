import socket
import time
from threading import Thread
import motortest as conveyor

myIP = '192.168.1.3'
movePort = 8091
stopPort = 8090
robotIP = '192.168.1.5'
robotPort = 8080
LEFT_COMMAND = "LEFT"
RIGHT_COMMAND = "RIGHT"
STOP_COMMAND = "STOP"
RETURN_MSG = ""

def start_thread_stop():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((myIP, stopPort))
    serversocket.listen(1) # become a server socket, maximum 5 connections

    while True:
        print("loopin stop thread\n")
        connection, address = serversocket.accept()
        buf = connection.recv(64)
        if buf == STOP_COMMAND:
            print STOP_COMMAND
            conveyor.stop()
        time.sleep(0.5)

def start_thread_main():
    # Also start stop thread listening for emergency stop
    Thread(target=start_thread_stop,args=()).start()
    
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((myIP, movePort))
    serversocket.listen(1) # become a server socket, maximum 5 connections

    while True:
        print("loopin main thread")
        connection, address = serversocket.accept()
        buf = connection.recv(64)
        if buf == LEFT_COMMAND:
            print LEFT_COMMAND
            conveyor.move(0,3.5)
            CONVEYOR_RETURNS = "Left move success"
        elif buf == RIGHT_COMMAND:
            print RIGHT_COMMAND
            conveyor.move(1,3.5)
            CONVEYOR_RETURNS = "Right move success"
        else:
            print "Invalid command"
            CONVEYOR_RETURNS = "Invalid command"
            
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect((robotIP, robotPort))
        clientsocket.send("CONVEYOR_DATA:" + CONVEYOR_RETURNS)
        time.sleep(0.5)
        

start_thread_main()

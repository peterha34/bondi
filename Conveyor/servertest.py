import socket
import time
import motortest as conveyor

robotIP = 'localhost'
port = 8090

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((robotIP, port))
serversocket.listen(1) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    print("loopin")
    if buff == "left":
        conveyor.move(0,10)
    else if buff == "right":
        conveyor.move(1,10)
    else if buff == "stop:
        conveyor.stop()
    time.sleep(0.5)

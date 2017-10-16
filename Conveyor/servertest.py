import socket
import time

robotIP = '192.168.1.5'
port = 8090

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((robotIP, port))
serversocket.listen(1) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    print("loopin")
    print buf
    time.sleep(1)

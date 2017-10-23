import socket
import time

conveyor = '192.168.1.18'
port = 8090

LEFT_COMMAND = "LEFT"
RIGHT_COMMAND = "RIGHT"
STOP_COMMAND = "STOP"

CONVEYOR_RETURNS = "CONVEYOR_DATA"

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((conveyor, port))
serversocket.listen(1)  # become a server socket, maximum 5 connections

return_message = ""
while True:
    connection, address = serversocket.accept()
    buff = connection.recv(64)
    if buff == LEFT_COMMAND:
        print("moving left")
        time.sleep(10)
        return_message = "LEFT_COMPLETE"
    elif buff == RIGHT_COMMAND:
        print("moving right")
        time.sleep(10)
        return_message = "RIGHT_COMPLETE"
    elif buff == STOP_COMMAND:
        print("Stopping")
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('192.168.1.18', 8080))
    clientsocket.send(CONVEYOR_RETURNS + "," + return_message)
    time.sleep(0.5)

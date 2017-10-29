import socket
import time

clientsocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket1.connect(('172.19.125.238', 8091))
clientsocket1.send("RIGHT")
time.sleep(1.8)
'''clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('172.19.125.238', 8090))
clientsocket.send("STOP")'''

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('172.19.125.238', 8091))
clientsocket.send("LEFT")
time.sleep(1.8)

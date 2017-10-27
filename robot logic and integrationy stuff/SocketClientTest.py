import socket
import time

clientsocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket1.connect(('192.168.1.3', 8091))
clientsocket1.send("RIGHT")
time.sleep(1.8)
'''clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.1.3', 8090))
clientsocket.send("STOP")'''

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.1.3', 8091))
clientsocket.send("LEFT")
time.sleep(1.8)

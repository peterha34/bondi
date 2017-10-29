import socket
import time
from threading import Thread

def socket_dude( pi_address):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((pi_address, 8080))
    serversocket.listen(1)  # become a server socket, maximum 5 connections

    while True:
        connection, address = serversocket.accept()
        buff = connection.recv(64)
        print("getting socket data: " + buff)
		
        next = int(buff.split(":")[1]) + 1
        print("checking that nexty guy: " + str(next))
        time.sleep(2)
        socket_call(next)

		
def socket_call(val):
	print("calling this boyo: " + str(val))
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientSocket.connect(('192.168.1.201', 5000))
	print("check 1")
	clientSocket.send(str(val))
	print("check 2")
	time.sleep(2)
	clientSocket.close()
	time.sleep(2)

	
pi_address = "192.168.1.30"
Thread(target=socket_dude, args=(pi_address,)).start()
socket_call(1)



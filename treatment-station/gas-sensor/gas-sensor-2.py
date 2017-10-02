import ModbusServer as server
from mq import *
import sys, time

__init__
#Initialise this function to connect to server
server.server_start(192.168.1.4)

# initialise server with register name and coil name
server.initialise_server(alcohol, doievenfkenneedone)


try:
    print("Press CTRL+C to abort.")
    
    mq = MQ();
    while True:
        perc = mq.MQPercentage()
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.write("Alcohol: %g ppm, CO: %g ppm" % (perc["ALCOHOL"], perc["CO"]))
        sys.stdout.flush()
        time.sleep(0.1)
		# Passing stuff to server
		server.update_register(alcohol, perc["ALCOHOL"])
		
		
except:
    print("\nAbort by user")
import ModbusServer as server
from mq import *
import sys, time

# initialise server with register name and coil name
server.initialise_server("alcohol", "doievenfkenneedone")

# initialise this function to connect to server
server.server_start("192.168.1.4")

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
        server.update_register("alcohol", (perc["ALCOHOL"])) 	# Passing stuff to server
		
		
except:
    print("\nAbort by user")

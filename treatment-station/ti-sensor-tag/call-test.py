from cc2650sensortag import *
import os
import time
import sys

# ---------------------------------------------------------------------------#
# Application Related Macros
# ---------------------------------------------------------------------------#
HEAT        = "24:71:89:E8:85:83"
UNDULATION  = "24:71:89:CC:1E:00"
ALCOHOL     = ""                    #tba


# ---------------------------------------------------------------------------#
# Sensor Connection
# ---------------------------------------------------------------------------#

print("Restarting bluetooth service")
os.system("sudo service bluetooth restart")
time.sleep(5)

print("Selecting Sensors")
SensorSelect(UNDULATION)
print ("Selected")

print('Connecting to ' + UNDULATION)
sensortag = SensorTag(UNDULATION)
print("Connected")

time.sleep(1)

# ---------------------------------------------------------------------------#
# Sensor Printing
# ---------------------------------------------------------------------------#

try:
    ''' For heat '''
##    while True:
##        print('Temp: ', sensortag.IRtemperature.read())
##        time.sleep(1.0)

    ''' For Undulation '''
    while True:
        print('Temp: ', sensortag.IRtemperature.read())
        print('Acceleration: ', sensortag.accelerometer.read())
        time.sleep(1.0)

    ''' For Alcohol '''
##    while True:
##        print('Temp: ', sensortag.IRtemperature.read())
##        time.sleep(1.0)
        
except:
    print(sys.exc_info())
    print("\nAbort by user")

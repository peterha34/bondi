'''
Sensor call script mainly for idividual testing purpose

Author: JT

'''

from cc2650sensortag import *
import os
import time
import sys
import csv
import datetime

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
time.sleep(2)

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
##        with open('ts1-sensordata.csv', 'a') as csvfile:
##            sensorwriter = csv.writer(csvfile)
##            time_now = datetime.datetime.now()
##            temp = sensortag.IRtemperature.read()
##            print('Time: {0} Temperature: {1}'.format(time_now, temp))
##            sensorwriter.writerow([time_now, temp])
##            time.sleep(1)

    ''' For Undulation '''
    while True:
        with open('ts2-sensordata.csv', 'a') as csvfile:
            sensorwriter = csv.writer(csvfile)
            time_now = datetime.datetime.now()
            temp = sensortag.IRtemperature.read()
            accel = sensortag.accelerometer.read()
            print('Time: {0} Temperature: {1} Acceleration: {3}' .format(time_now, temp, accel))
            sensorwriter.writerow([time_now, temp, accel])
            time.sleep(1)

##    ''' For Alcohol '''
##    while True:
##        with open('ts3-sensordata.csv', 'a') as csvfile:
##            sensorwriter = csv.writer(csvfile)
##            time_now = datetime.datetime.now()
##            temp = sensortag.IRtemperature.read()
##            print('Time: {0} Temperature: {1}'.format(time_now, temp))
##            sensorwriter.writerow([time_now, temp])
##            time.sleep(1)
        
except:
    print(sys.exc_info())
    print("\nAbort by user")

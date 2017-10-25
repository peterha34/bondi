import cc2650sensortagv3
import os

os.system("sudo service bluetooth restart")
os.system("sudo python cc2650sensortagv3.py")



##sensortag.main()
##try:
##    print("Press CTRL+C to abort mission.")
##
##    sensortag = cc2650sensortagv2
##    print("we here")
##    print('Call Temp: ', sensortag.IRTemperatureSensorTMP007().read())

##    while True:
##        print('call testing')
##        print('Call Temp: ', sensortag.IRTemperatureSensorTMP007().read())
##        print('call testing')
##        time.sleep(1.0)

##except:
##    print("\nAbort by user")

##print('Temp: ', IRtemperature().read())

# python programming in raspberry pi

##
##SENSOR_TEMP     =   True #Select sensor
##DEVICE =  "24:71:89:E8:85:83" # MAC of BT device
##POLL_TIME = 1.0 # time between polling
##
##
##
##print('Connecting to ' + DEVICE)
##    tag = SensorTag(DEVICE)  
### Enable selected sensor
##if SENSOR_TEMP
##    tag.IRtemperature.enable()
##
##time.sleep(1.0)
##
##tag.disconnect()
##del tag



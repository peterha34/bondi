Pi RTU information

username: pi

password: persianprince

Sensor tag ID: 

B0:91:22:F6:A8:86 CC2650 SensorTag (heat-ts)

24:71:89:CC:1E:00 CC2650 SensorTag (undulation-ts) 


---------------------------
Sensors Debugging - Terminal Commands

// Scan for sensor tags

sudo hcitool lescan

/* 
** The section below provides different method to the sensor tag 
** The sensors available are: accelerometer, barometer, 
** gyroscope, humidity, IRtemperature, lightmeter, magnetometer. 
*/
// Run the script boiii
sudo python sensortagcollector.py

// run with specific name of sensor-tag
sudo python sensortagcollector.py -d uid=friendlyname
e.g sudo python sensortagcollector.py -d B0:91:22:F6:A8:86=heat-ts

// run with multiple named sensor tags
sudo python sensortagcollector.py -d uid=friendlyname uid=friendlyname

// run with only specified sensor tags
sudo python sensortagcollector.py -o -d uid=friendlyname uid=friendlyname
e.g sudo python sensortagcollector.py -o -d B0:91:22:F6:A8:86=heat-ts 24:71:89:CC:1E:00=undulation-ts
  
// Command for heat and long treatment
sudo python sensortagcollector.py -o -d B0:91:22:F6:A8:86=heat-ts 24:71:89:CC:1E:00=undulation-ts -f IRtemperature accelerometer

---------------------------
Node-Red Commands

// start node red to debug in node red apps
node-red-start

// stop node red
node-red-stop

------------------------
Debug note
// Restart bluetooh
service bluetooth restart

// to swap from wireless to ethernet
sudo nano /etc/network/interfaces
--> comment out allow-hotplug eth0



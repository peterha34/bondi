-------------------------
Connection to IGSS info:
TS-1 Temp = Offset: 1
TS-2 Temp = Offset: 2
TS-2 Acceleration = Offeset: 3
TS-3 Temp = Offset: 4
TS-3 Alcohol Concerntration = Offset: 5

TS-1 Light = Offset: 6
TS-1 Humidity = Offset: 7

--------------------------
// to swap from wireless to ethernet
sudo nano /etc/network/interfaces
--> comment out allow-hotplug eth0

------------------
// check bluetooth status 
sudo service bluetooth status


---------------
/* Bluetooth fix 1 */

For this error: https://pastebin.com/BiejnzTw
Read this: https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=131999

Currently read this file: /lib/systemd/system/bluetooth.service
// edit this file
nano /lib/systemd/system/bluetooth.service

// line changed
ExecStart=/usr/lib/bluetooth/bluetoothd --noplugin=sap

/* Result 
** Fixed failed. 
** Still have to restart bluetooth after a while 
*/ 

------------------
/* Bluetooth fix 2 */

$ hciconfig hci0 down
$ hciconfig hci0 up
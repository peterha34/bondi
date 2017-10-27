-------------
Heat-Station MAC - 24:71:89:E8:85:83
Undulation-Station MAC - 24:71:89:CC:1E:00
Alcohol-Station MAC - C4:BE:84:70:14:8B

------------------------------
// Bluepy library creator notes and stuff!
https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=58622
https://github.com/IanHarvey/bluepy
// User manual
https://www.elinux.org/RPi_Bluetooth_LE


// check if the thingo is connected
sudo hcitool lecc <MAC address>
e.g sudo hcitool lecc B0:91:22:F6:A8:86


// Restart bluetooh
service bluetooth restart
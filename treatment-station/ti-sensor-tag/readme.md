-------------
Heat-Station MAC - 24:71:89:E8:85:83
Undulation-Station MAC - 24:71:89:CC:1E:00
Alcohol-Station MAC - C4:BE:84:70:14:8B

------------------------------
/* Terminal Debug Commands */
// Check if the sensor is attached
sudo hcitool lecc <MAC address>
e.g sudo hcitool lecc B0:91:22:F6:A8:86

/* Call test file is the main debugging file */
// Run call test to debug
sudo python call-test.py

/* References */
// Bluepy library creator notes and repository
https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=58622
https://github.com/IanHarvey/bluepy
// User manual
https://www.elinux.org/RPi_Bluetooth_LE

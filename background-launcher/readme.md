// Lanch script on startup
http://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/

// Make shell script executable
chmod 755 launcher.sh

// Test it
sh launcher.sh

// Open crontab
sudo crontab -e

// Add this line to the very bottom of crontab
@reboot sh /home/pi/bondi/background-launcher/launcher.sh >/home/pi/logs/cronlog 2>&1

// Make this folder to store your error log if shits doesnt launch
cd /home/pi
mkdir logs

// Check if your program is being run
- Open up terminal
pgrep -a python

# !/bin/sh
# conveyor-launcher.sh
# Back ground launcher for conveyor pi


# sleep to let eveything else kickoff first before starting
/bin/sleep 20

# navigate to bondi directory, then to this directory, then execute python script, then back home
cd /
cd /home/pi/Desktop/bondi/Conveyor
sudo python conveyorServer.py 
cd /home/pi/Desktop/bondi/emergency-system
sudo python switch.py
cd /



# do the same as above for your own code, change directory locatoin and script name..
#cd /
#cd /home/pi/Desktop/bondi/Conveyor
#sudo python conveyorServer
#cd /

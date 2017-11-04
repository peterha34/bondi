import abb

# Coordinates of treatment stations
heat = [0,0,0,0,90,0]
alcohol = [0,0,0,0,90,0]
undul = [0,0,0,0,90,0]

R=abb.Robot(ip='192.168.125.1')

# Pickup tray with robot R and place on convyor
R.set_joints([0,0,0,0,90,0])
set do10_6
R.set_joints([0,0,0,0,90,0])
reset d010_6

# Send command to VDS to take photo
for

# Set colour and position variables from received VDS data

# Move disc from tray to appropriate treatment station
R.set_joints([0,0,0,0,90,0])
set do10_6
R.set_joints([0,0,0,0,90,0])
reset d010_6


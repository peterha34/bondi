from bluepy import btle

# The following simple example shows
# how to connect to a device and display its services: 
print "Connecting..."
dev = btle.Peripheral("B0:91:22:F6:A8:86")
 
print "Services..."
for svc in dev.services:
    print str(svc)

# For a Sensortag, ensure the green LED is flashing before trying to connect.
# To connect to the SensorTag's "light level" service, and list the characteristics
lightSensor = btle.UUID("f000aa70-0451-4000-b000-000000000000")
 
lightService = dev.getServiceByUUID(lightSensor)
for ch in lightService.getCharacteristics():
    print str(ch)

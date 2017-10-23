#!/usr/bin/env python
'''
Pymodbus Server With Updating Callback
--------------------------------------------------------------------------

An asynch implementation of updating a modbus server while it's running
This is a modified version of some example code provided by riptideio.

'''
#---------------------------------------------------------------------------# 
# import the modbus libraries we need
#---------------------------------------------------------------------------# 
from pymodbus.server.async import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer

#---------------------------------------------------------------------------# 
# import the twisted libraries we need
# FYI: Twisted is a library that focuses on providing scalable tcp servers.
#---------------------------------------------------------------------------# 
from twisted.internet.task import LoopingCall

#---------------------------------------------------------------------------# 
# configure the service logging
#---------------------------------------------------------------------------# 

#---------------------------------------------------------------------------# 
# define your callback process
# FYI: This will run a 5 second delay -> This could also run as a background 
# thread if necessary.
#---------------------------------------------------------------------------# 
def updating_writer(a):
    context  = a[0]
    print("Checking context: " + str(context[0].getValues(1, 0)))

#---------------------------------------------------------------------------# 
# initialize your data store
#---------------------------------------------------------------------------# 
# A sequential datablock basically expects data in every slot of the block
# A sparse DataBlock allows you to lease slots empty
store = ModbusSlaveContext()
context = ModbusServerContext(slaves=store, single=True)

#---------------------------------------------------------------------------# 
# initialize the server information
#---------------------------------------------------------------------------# 
identity = ModbusDeviceIdentification()
identity.VendorName  = 'pymodbus'
identity.ProductCode = 'PM'
identity.VendorUrl   = 'http://github.com/bashwork/pymodbus/'
identity.ProductName = 'pymodbus Server'
identity.ModelName   = 'pymodbus Server'
identity.MajorMinorRevision = '1.0'

#---------------------------------------------------------------------------# 
# run the server you want
#---------------------------------------------------------------------------# 
time = 5 # 5 seconds delay
loop = LoopingCall(f=updating_writer, a=(context,))
loop.start(time, now=False) # initially delay by time
# This is the IP of my rasp pi
piAddress = "192.168.1.3"
StartTcpServer(context, identity=identity, address=(piAddress, 5020))

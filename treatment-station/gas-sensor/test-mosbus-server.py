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
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

#---------------------------------------------------------------------------# 
# define your callback process
# FYI: This will run a 5 second delay -> This could also run as a background 
# thread if necessary.
#---------------------------------------------------------------------------# 
def updating_writer(a):
    log.debug("updating the context")
    context  = a[0]
# register 3 is a modbus specific register for written data vals, represented
# in IGSS as the 3/16 Register option on a diagram object.
# Pretty sure each register is 16 bit.
    register = 3
# Slave ID is used as a context identifier, to show which slave table is
# being used, currently addressing the first slave
    slave_id = 0x00
# Address offset value - used to determine where in the register ths data is
# stored
    address  = 0x00
# retrieves values from the context table, with count = the number of vals
    values   = context[slave_id].getValues(register, address, count=1)
# increments all vals (incase count > 1)
    values   = [v + 1 for v in values]
    log.debug("new values: " + str(values))
# Writes vals to context table.
    context[slave_id].setValues(register, address, values)

#---------------------------------------------------------------------------# 
# initialize your data store
#---------------------------------------------------------------------------# 
# A sequential datablock basically expects data in every slot of the block
# A sparse DataBlock allows you to lease slots empty
store = ModbusSlaveContext(
    di = ModbusSequentialDataBlock(0, [17]*100),
    co = ModbusSequentialDataBlock(0, [17]*100),
    hr = ModbusSequentialDataBlock(0, [17]*100),
    ir = ModbusSequentialDataBlock(0, [17]*100))
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
piAddress = "192.168.1.4"
StartTcpServer(context, identity=identity, address=(piAddress, 5020))

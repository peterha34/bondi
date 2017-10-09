#!/usr/bin/env python
'''
An abstraction layer for the pimodbus libraries, to ensure controlled usage and garuntee software quality

Author: MM
'''
# ---------------------------------------------------------------------------#
# import the modbus libraries we need
# ---------------------------------------------------------------------------#
from pymodbus.server.async import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer
from twisted.internet.task import LoopingCall
from mq import *

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# slave id is set to 0x00 and always will be, due to the use of a single context
slave_id = 0x00
initialised = False
context = None
register_names = None
coil_names = None
mq = MQ();


# ---------------------------------------------------------------------------#
# updates a register value
# regname is the name of the register provided in the list at initialisation of the server
# regval is the new value you want this register to hold
# ---------------------------------------------------------------------------#
def update_register( regname, regval):
    register = 3
    address = 0x00 + register_names.index(regname)
    context[slave_id].setValues(register, address, [regval])

# ---------------------------------------------------------------------------#
# gets a register value
# regname is the name of the register provided in the list at initialisation of the server
# returns the current value of the named register
# ---------------------------------------------------------------------------#
def get_register( regname ):
    register = 3
    address = 0x00 + register_names.index(regname)
    return context[slave_id].getValues(register, address)


# ---------------------------------------------------------------------------#
# updates a coil value with a new value (should be 1 or 0)
# TODO: enforce the boolean nature of the coil on write
# coilname is the name of the coil provided in the list at initialisation of the server
# coilval is the new value you want this register to hold
# ---------------------------------------------------------------------------#
def update_coil( coilname, coilval):
    register = 1
    address = 0x00 + coil_names.index(coilname)
    context[slave_id].setValues(register, address, coilval)


# ---------------------------------------------------------------------------#
# gets a coil value
# coil is the name of the coil provided in the list at initialisation of the server
# returns the current value of the named coil (should be one or zero)
# ---------------------------------------------------------------------------#
def get_coil( coilname ):
    register = 1
    address = 0x00 + coil_names.index(coilname)
    return context[slave_id].getValues(register, address)

def updating_writer(a):
    context  = a[0]
    mq = a[1] 
    	
    # new stuff here
    perc = mq.MQPercentage()
    print("Alcohol: %g ppm, CO: %g ppm" % (perc["ALCOHOL"], perc["CO"]))
    update_register("alcohol",(perc["ALCOHOL"]))

# ---------------------------------------------------------------------------#
# initialize the data store
# ---------------------------------------------------------------------------#
# initialises a server instance, sets register and coil counts for this
# specific server instance
# regnames is a list of names that each register will have
# this is to abstract modbus functionality from calls to updating info
# please make each register and coil name unique within a single context element
# ---------------------------------------------------------------------------#
def initialise_server( regnames, coilnames ):

    global register_names
    register_names = regnames
    global coil_names
    coil_names = coilnames
    cosize = 0
    hrsize = 0
    if coilnames is not None:
        cosize = len(coilnames)

    if regnames is not None:
        hrsize = len(regnames)

    # co stands for coil, and emulates the multiple coil holding registers that will occupy register location 0
    # hr stands for holding register, and emulates the general holding registers, occupies location 3
    # DEV NOTE: tried only initialising certain block, at differing length to try save space and initialisation time
    #   result was errors being thrown, assuming due to fucked up address space - didn't dig into it, will just use
    #   these settings, no point in doing a RCA.
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [17] * 100),
        co=ModbusSequentialDataBlock(0, [17] * 100),
        hr=ModbusSequentialDataBlock(0, [17] * 100),
        ir=ModbusSequentialDataBlock(0, [17] * 100))

    global context
    # single is flagged, meaning only a single context will be created here
    context = ModbusServerContext(slaves=store, single=True)
    global initialised
    initialised = True
    print('initialised!')


# ---------------------------------------------------------------------------#
# initialize the server information
# ---------------------------------------------------------------------------#
identity = ModbusDeviceIdentification()
identity.VendorName  = 'pymodbus'
identity.ProductCode = 'PM'
identity.VendorUrl   = 'http://github.com/bashwork/pymodbus/'
identity.ProductName = 'pymodbus Server'
identity.ModelName   = 'pymodbus Server'
identity.MajorMinorRevision = '1.0'


# ---------------------------------------------------------------------------#
# Start an instance of the server, after initiating it to the vals you need
# ---------------------------------------------------------------------------#
def server_start( piAddress ):
    # This is the IP of my rasp pi
    if initialised:
	time = 2 # 5 seconds delay
	loop = LoopingCall(f=updating_writer, a=(context,mq,))
	loop.start(time, now=False) # initially delay by time
        StartTcpServer(context, identity=identity, address=(piAddress, 5020))
    else:
        print('Please Initialise the server before trying to start')

sensorList = ["alcohol"];
initialise_server(sensorList, "doievenfkenneedone")
time = 2 # 5 seconds delay
loop = LoopingCall(f=updating_writer, a=(context,mq,))
loop.start(time, now=False) # initially delay by time
StartTcpServer(context, identity=identity, address=("192.168.1.4", 5020))


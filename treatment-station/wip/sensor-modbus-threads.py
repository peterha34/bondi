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
from threading import Thread
from Queue import Queue
import time
import socket
from mq import *

#---------------------------------------------------------------------------# 
# configure the service logging
#---------------------------------------------------------------------------# 
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
register_vals = None

TREAT1 = "TEMP"
TREAT2 = "SHAKE"
TREAT3 = "ALCOHOL"

def pol_sensors( treatment, queue, context ):
    mq = None

   #initialises the gas sensor
    if treatment==TREAT3:
	mq = MQ();

    while True:
        if treatment==TREAT1:
	    # get temp val
	    temp = "TempVal"
	    update_register(register_names[0],temp, context)
	elif treatment==TREAT2:
	    temp = "TempVal"
	    shake = "ShakeVal"
	    # 1 is temp
	    # 2 is shake
	    update_register(register_names[1],temp, context)
	    update_register(register_names[2],temp, context)
	elif treatment ==TREAT3:
	    alc = "AlcoholVal"
	    temp = "TempVal"
	    # new stuff here
	    # yea
	    perc = mq.MQPercentage()
	    print("Alcohol: %g ppm, CO: %g ppm" % (perc["ALCOHOL"], perc["CO"]))
	    update_register("alcohol",(perc["ALCOHOL"]), context)
	    # 4 is alcohol content
	    #update_register(register_names[4],temp, context)
        time.sleep(2)
	

def treatment_servs( treatment, queue, context, ip ):
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#192.168.1.5 - ROBOT IP
	startCommand = ""
	coilname = ""
	port= ""
	sleepTime = "";
	
	if treatment == TREAT1:
		startCommand = "START T1"
		coilname = coil_names[0]
		port = 8080
		sleepTime = 30
	elif treatment == TREAT2:
		startCommand = "START T2"
		coilname = coil_names[1]
		port = 8081
		sleepTime = 50
	elif treatment == TREAT3:
		startCommand = "START T3"
		#TODO: swap this shit out for non-debug
		coilname = coil_names[0]
		port = 8082
		sleepTime = 60
	serversocket.bind((ip, port))
	serversocket.listen(1) # become a server socket, maximum 5 connections

	while True:
		connection, address = serversocket.accept()
		buf = connection.recv(64)
		if buf == startCommand:
			print("FUCKING TREATING LADS")
			update_coil(coilname, "1", context)
			time.sleep(sleepTime)
			update_coil(coilname, "0", context)
			print("TREATMENTS FUCKING DONE")
			# TODO: send s signal to the robots to do their thing
			

# ---------------------------------------------------------------------------#
# updates a register value
# regname is the name of the register provided in the list at initialisation of the server
# regval is the new value you want this register to hold
# ---------------------------------------------------------------------------#
def update_register( regname, regval, context):
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
def update_coil( coilname, coilval, context):
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
        time = 2
        register_queue = Queue()
	coil_queue = Queue()
		
        #Thread(target=pol_sensors, args=(TREAT1,register_queue, context)).start()
        #Thread(target=treatment_servs, args=(TREAT1,coil_queue, context, piAddress)).start()
		
        #Thread(target=pol_sensors, args=(TREAT2,register_queue, context)).start()
        #Thread(target=treatment_servs, args=(TREAT2,coil_queue, context, piAddress)).start()
		
        Thread(target=pol_sensors, args=(TREAT3,register_queue, context)).start()
        Thread(target=treatment_servs, args=(TREAT3,coil_queue, context, piAddress)).start()
			
        StartTcpServer(context, identity=identity, address=(piAddress, 5020))
    else:
        print('Please Initialise the server before trying to start')

sensorList = ["alcohol"];
coilList = ["treatment3"]
initialise_server(sensorList, coilList)
server_start("192.168.1.4")


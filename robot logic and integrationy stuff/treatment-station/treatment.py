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
from cc2650sensortag import *
import os
import csv
import datetime
from mq import *

# slave id is set to 0x00 and always will be, due to the use of a single context
slave_id = 0x00
initialised = False
context = None
register_names = None
coil_names = None
register_vals = None

TREAT1 = "TEMP"
TREAT2 = "ACCEL"
TREAT3 = "ALCOHOL"


def pol_sensors(treatment, context):
    mq = None
    sensortag = None
    
    if treatment==TREAT3:
        mq = MQ();
        print("Selecting Sensors") 
        SensorSelect("C4:BE:84:70:14:8B") # Heat TS
        print ("Selected")
        print('Connecting to ' + "C4:BE:84:70:14:8B")
        sensortag = SensorTag("C4:BE:84:70:14:8B")
        print("Connected")
        time.sleep(1)

    if treatment == TREAT1:
        print("Selecting Sensors") 
        SensorSelect("24:71:89:E8:85:83") # Heat TS
        print ("Selected")
        print('Connecting to ' + "24:71:89:E8:85:83")
        sensortag = SensorTag("24:71:89:E8:85:83")
        print("Connected")
        time.sleep(1)
        
    if treatment == TREAT2:
        print("Selecting Sensors")
        SensorSelect("24:71:89:CC:1E:00") # Undulation TS
        print ("Selected")
        print('Connecting to ' + "24:71:89:CC:1E:00")
        sensortag = SensorTag("24:71:89:CC:1E:00")
        print("Connected")
        time.sleep(1)

	
    while True:
        if treatment == TREAT1:
            # 0 is temp
            with open('ts1-sensordata.csv', 'a') as csvfile:
                sensorwriter = csv.writer(csvfile)
                time_now = datetime.datetime.now()
                temp = sensortag.IRtemperature.read()
                print('Time: {0} Temperature: {1}C'.format(time_now, temp))
                sensorwriter.writerow([time_now, temp])           
                update_register(register_names[0], temp, context)
                time.sleep(1) 
            
        elif treatment == TREAT2:
            # 1 is temp
            # 2 is accel
            with open('ts2-sensordata.csv', 'a') as csvfile:
                sensorwriter = csv.writer(csvfile)
                time_now = datetime.datetime.now()
                temp = sensortag.IRtemperature.read()
                accel = sensortag.accelerometer.read()
                print('Time: {0} Temperature: {1}C Acceleration: {2}g'.format(time_now, temp, accel))
                sensorwriter.writerow([time_now, temp, accel])
                update_register(register_names[1], temp, context)
                update_register(register_names[2], accel, context)
                time.sleep(1)

        elif treatment == TREAT3:
            # 3 is temp
            # 4 is alcohol
            with open('ts3-sensordata.csv', 'a') as csvfile:
                sensorwriter = csv.writer(csvfile)
                time_now = datetime.datetime.now()
                temp = sensortag.IRtemperature.read()
                perc = mq.MQPercentage()
                alc = (perc["ALCOHOL"])
                print('Time: {0} Temperature: {1}C Alcohol: {2} ppm '.format(time_now, temp, alc))
                update_register(register_names[3], temp, context)
                update_register(register_names[4], alc, context)
                sensorwriter.writerow([time_now, temp, alc])
                time.sleep(1)


def treatment_servs(treatment, context, ip):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 192.168.1.5 - ROBOT IP
    startCommand = ""
    coilname = ""
    port = ""
    sleepTime = ""
    unload = ""

    if treatment == TREAT1:
        startCommand = "START T1"
        coilname = coil_names[0]
        port = 8082
        sleepTime = 30
        unload = "UNLOAD_T1"
        
    elif treatment == TREAT2:
        startCommand = "START T2"
        coilname = coil_names[1]
        port = 8083
        sleepTime = 50
        unload = "UNLOAD_T2"
        
    elif treatment == TREAT3:
        startCommand = "START T3"
        coilname = coil_names[2]
        port = 8084
        sleepTime = 60

        unload = "UNLOAD_T3"
    serversocket.bind((ip, port))
    serversocket.listen(1)  # become a server socket, maximum 5 connections

    while True:
        connection, address = serversocket.accept()
        buf = connection.recv(64)
        if buf == startCommand:
            update_coil(coilname, [1], context)
            time.sleep(sleepTime)
            update_coil(coilname, [0], context)
            clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientsocket.connect(("192.168.1.5", 8080))
            clientsocket.send("TREATMENT_DATA:"+unload)
            time.sleep(1)
            clientsocket.close()


# ---------------------------------------------------------------------------#
# updates a register value
# regname is the name of the register provided in the list at initialisation of the server
# regval is the new value you want this register to hold
# ---------------------------------------------------------------------------#
def update_register(regname, regval, context):
    register = 3
    address = 0x00 + register_names.index(regname)
    context[slave_id].setValues(register, address, [regval])


# ---------------------------------------------------------------------------#
# gets a register value
# regname is the name of the register provided in the list at initialisation of the server
# returns the current value of the named register
# ---------------------------------------------------------------------------#
def get_register(regname):
    register = 3
    address = 0x00 + register_names.index(regname)
    return context[slave_id].getValues(register, address)


# ---------------------------------------------------------------------------#
# updates a coil value with a new value (should be 1 or 0)
# TODO: enforce the boolean nature of the coil on write
# coilname is the name of the coil provided in the list at initialisation of the server
# coilval is the new value you want this register to hold
# ---------------------------------------------------------------------------#
def update_coil(coilname, coilval, context):
    register = 1
    address = 0x00 + coil_names.index(coilname)
    context[slave_id].setValues(register, address, coilval)


# ---------------------------------------------------------------------------#
# gets a coil value
# coil is the name of the coil provided in the list at initialisation of the server
# returns the current value of the named coil (should be one or zero)
# ---------------------------------------------------------------------------#
def get_coil(coilname):
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
def initialise_server(regnames, coilnames):
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
    store = ModbusSlaveContext()

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
identity.VendorName = 'pymodbus'
identity.ProductCode = 'PM'
identity.VendorUrl = 'http://github.com/bashwork/pymodbus/'
identity.ProductName = 'pymodbus Server'
identity.ModelName = 'pymodbus Server'
identity.MajorMinorRevision = '1.0'


# ---------------------------------------------------------------------------#
# Start an instance of the server, after initiating it to the vals you need
# ---------------------------------------------------------------------------#
def server_start(piAddress):
    # This is the IP of my rasp pi
    if initialised:

        # JT - Restart bluetooth on Pi cause it usually fkes up everytime it reboots
        print("Restarting bluetooth service")
        os.system("sudo service bluetooth restart")
        time.sleep(2)
        
        Thread(target=pol_sensors, args=(TREAT1, context)).start()
        Thread(target=treatment_servs, args=(TREAT1, context, piAddress)).start()

        Thread(target=pol_sensors, args=(TREAT2, context)).start()
        Thread(target=treatment_servs, args=(TREAT2, context, piAddress)).start()

        Thread(target=pol_sensors, args=(TREAT3, context)).start()
        Thread(target=treatment_servs, args=(TREAT3, context, piAddress)).start()
        StartTcpServer(context, identity=identity, address=(piAddress, 5020))
    else:
    	print('Please Initialise the server before trying to start')


registerList = ["T1-temp", "T2-temp", "T2-accel", "T3-temp", "T3-alc"]
coilList = ["T1","T2","T3"]
initialise_server(registerList, coilList)
server_start("192.168.1.4")

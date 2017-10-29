#!/usr/bin/env python
'''
A server implementation that handles the necessary calls to the robot functions
Provides modbus connectivity and port listening for vision detection
and provides start functionality for treatment stations
Author: MM
'''

# ---------------------------------------------------------------------------#
# import the necessary libraries
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

# slave id is set to 0x00 and always will be, due to the use of a single context
slave_id = 0x00

# Conveyor Commands
LEFT_COMMAND = "LEFT"
RIGHT_COMMAND = "RIGHT"
STOP_COMMAND = "STOP"

# Return data headers on incomming socket data
CONVEYOR_RETURNS = "CONVEYOR_DATA"
ROBOT_RETURNS_LOAD = "LOADER_ROBOT_DATA"
ROBOT_RETURNS_STACK = "STACKER_ROBOT_DATA"
VISION_RETURNS = "VISION_DATA"
TREATMENT_RETURNS = "TREATMENT_DATA"

# Retrieve commands from loader robot to stacker robot
GET_T1 = "RETRIEVE_T1_TRAY"
GET_T2 = "RETRIEVE_T2_TRAY"
GET_T3 = "RETRIEVE_T3_TRAY"

STASH_T1 = "STOW_T1_TRAY"
STASH_T2 = "STOW_T2_TRAY"
STASH_T3 = "STOW_T3_TRAY"

UNLOAD_T1 = "UNLOAD_T1"
UNLOAD_T2 = "UNLOAD_T2"
UNLOAD_T3 = "UNLOAD_T3"
UNLOAD_F = "UNLOAD_F"

VISION_IP = "192.168.1.2"
CONVEYOR_IP = "192.168.1.3"
ROBOT_1_IP = "192.168.1.201"
ROBOT_2_IP = "192.168.1.200"
TREATMENT_IP = "192.168.1.4"
MY_IP = "192.168.1.5"

'''
A server implementation that handles the necessary calls to the robot functions
Provides modbus connectivity and port listening for vision detection
and provides start functionality for treatment stations
Author: MM
'''

# ---------------------------------------------------------------------------#
# import the necessary libraries
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


# The socket broker runs in it's own thread, and listens for incoming traffic on port 8080.
# This function also handles the delegation of incoming traffic to an appropriate queue
# The queues are used to pass data between the appropriate threads.
def socket_broker( pi_address, vision_queue, conveyor_queue, treatment_queue, load_robot_queue, stash_robot_queue ):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((pi_address, 8080))
    serversocket.listen(1)  # become a server socket, maximum 5 connections

    while True:
        connection, address = serversocket.accept()
        buff = connection.recv(64)
        print("getting socket data: " + buff)
        dataList = buff.split(":")
        if dataList[0] == CONVEYOR_RETURNS:
            conveyor_queue.put(dataList[1])
            print("conveyor")
        elif dataList[0] == ROBOT_RETURNS_LOAD:
            load_robot_queue.put(dataList[1])
            print("robot 1")
        elif dataList[0] == ROBOT_RETURNS_STACK:
            stash_robot_queue.put(dataList[1])
            print("robot 2")
        elif dataList[0] == VISION_RETURNS:
            vision_queue.put(dataList[1])
            print("vision")
        elif dataList[0] == TREATMENT_RETURNS:
            treatment_queue.put(dataList[1])
            print("treatment")
        else:
            print("Error lads -> just what are you putting in my sockets?")

			
def send_R1(command):
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ROBOT_1_IP, 5000))
    clientsocket.send(command)
	wait(2)
    clientsocket.close()
	
def send_R2(command):
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ROBOT_2_IP, 5000))
    clientsocket.send(command)
	wait(2)
    clientsocket.close()

# slave id is set to 0x00 and always will be, due to the use of a single context
slave_id = 0x00

# Conveyor Commands
LEFT_COMMAND = "LEFT"
RIGHT_COMMAND = "RIGHT"
STOP_COMMAND = "STOP"

# Return data headers on incomming socket data
CONVEYOR_RETURNS = "CONVEYOR_DATA"
ROBOT_RETURNS_LOAD = "LOADER_ROBOT_DATA"
ROBOT_RETURNS_STACK = "STACKER_ROBOT_DATA"
VISION_RETURNS = "VISION_DATA"
TREATMENT_RETURNS = "TREATMENT_DATA"

# Retrieve commands from loader robot to stacker robot
GET_T1 = "RETRIEVE_T1_TRAY"
GET_T2 = "RETRIEVE_T2_TRAY"
GET_T3 = "RETRIEVE_T3_TRAY"

STASH_T1 = "STOW_T1_TRAY"
STASH_T2 = "STOW_T2_TRAY"
STASH_T3 = "STOW_T3_TRAY"

UNLOAD_T1 = "UNLOAD_T1"
UNLOAD_T2 = "UNLOAD_T2"
UNLOAD_T3 = "UNLOAD_T3"
UNLOAD_F = "UNLOAD_F"

# The socket broker runs in it's own thread, and listens for incoming traffic on port 8080.
# This function also handles the delegation of incoming traffic to an appropriate queue
# The queues are used to pass data between the appropriate threads.
def socket_broker( pi_address, vision_queue, conveyor_queue, treatment_queue, load_robot_queue, stash_robot_queue ):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((pi_address, 8080))
    serversocket.listen(1)  # become a server socket, maximum 5 connections

    while True:
        connection, address = serversocket.accept()
        buff = connection.recv(64)
        print("getting socket data: " + buff)
        dataList = buff.split(":")
        if dataList[0] == CONVEYOR_RETURNS:
            conveyor_queue.put(dataList[1])
            print("conveyor")
        elif dataList[0] == ROBOT_RETURNS_LOAD:
            load_robot_queue.put(dataList[1])
            print("robot 1")
        elif dataList[0] == ROBOT_RETURNS_STACK:
            stash_robot_queue.put(dataList[1])
            print("robot 2")
        elif dataList[0] == VISION_RETURNS:
            vision_queue.put(dataList[1])
            print("vision")
        elif dataList[0] == TREATMENT_RETURNS:
            treatment_queue.put(dataList[1])
            print("treatment")
        else:
            print("Error lads -> just what are you putting in my sockets?")


# R1 Retrieves the unsorted tray and places on the conveyor
def get_tray_initial( context ):
    print("getting tray initial")
    update_coil(context, "R1S1", [0])
    update_coil(context, "R1S2", [1])
    send_R1(1)
    update_coil(context, "R1S2", [0])
    update_coil(context, "R1S1", [1])

# Sends a tcp message to the vision detection to request that it takes a picture
def get_vision_results():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((VISION_DATA, 8081))
    clientsocket.send("GET_IMAGE")
    clientsocket.close()
	
	# Sends a tcp message to the vision detection to request that it takes a picture
def get_vision_baseline():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((VISION_IP, 8081))
    clientsocket.send("GET_BASELINE")
    clientsocket.close()

# Takes the disc in the designated slot to treatment site 1 
def disc_to_t1( context, slot, queue ):
    print("disc_to_t1")
    update_coil(context, "R1S1", [0])
    update_coil(context, "R1S3", [1])
    send_R1(slot+10)
	queue.get()
    update_coil(context, "R1S1", [1])
    update_coil(context, "R1S3", [0])

# Takes the disc in the designated slot to treatment site 2
def disc_to_t2( context, slot, queue ):
    print("disc_to_t2")
    update_coil(context, "R1S1", [0])
    update_coil(context, "R1S4", [1])
    send_R1(slot+20)
	queue.get()
    update_coil(context, "R1S1", [1])
    update_coil(context, "R1S4", [0])

# Takes the disc in the designated slot to treatment site 3
def disc_to_t3( context, slot, queue ):
    print("disc_to_t3")
    update_coil(context, "R1S1", [0])
    update_coil(context, "R1S5", [1])
    send_R1(slot+30)
	queue.get()
    update_coil(context, "R1S1", [1])
    update_coil(context, "R1S5", [0])

# Takes the unidentified disc in the designated slot to quarantine zone
def disc_to_quarantine( context, slot ):
    update_coil(context, "R1S1", [0])
    update_coil(context, "R1S6", [1])
    time.sleep(10)
    update_coil(context, "R1S1", [1])
    update_coil(context, "R1S5", [0])

# returns empty unsorted tray to the place it was picked up from
def return_unsorted_tray(context, queue):
    print("returning unsorted")
    update_coil(context, "R1S1", [0])
    update_coil(context, "R1S7", [1])
    send_R1(2)
	queue.get()
    update_coil(context, "R1S1", [1])
    update_coil(context, "R1S7", [0])

#sends control commands to the conver via TCP socket
def control_conveyor( command):
    print("sliding dat conveyor: " + command)
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((CONVEYOR_IP, 8091))
    clientsocket.send(command)
    clientsocket.close()

#sends command to start treatment 1 via tcp to the sensor pi
def start_treatment_1():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((TREATMENT_IP, 8082))
    clientsocket.send("START T1")
    clientsocket.close()

#sends command to start treatment 2 via tcp to the sensor pi
def start_treatment_2():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((TREATMENT_IP, 8083))
    clientsocket.send("START T2")
    clientsocket.close()

#sends command to start treatment 3 via tcp to the sensor pi
def start_treatment_3():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((TREATMENT_IP, 8084))
    clientsocket.send("START T3")
    clientsocket.close()

#sends command to unload treatment 1 via tcp to the sensor pi
def unload_treatment_1( context, disc_count, queue):
    update_coil(context, "R1S1", [0])
    update_coil(context, "R1S8", [1])
    for x in range(0, disc_count):
        print("Getting disc: " + str(disc_count))
        send_R1(400+(x+10)+(disc_count-x))
		queue.get()
    update_coil(context, "R1S1", [1])
    update_coil(context, "R1S8", [0])

#sends command to unload treatment 2 via tcp to the sensor pi
def unload_treatment_2( context, disc_count, queue):
    update_coil(context, "R1S1", [0])
    update_coil(context, "R1S9", [1])
    for x in range(0, disc_count):
        print("Getting disc: " + str(disc_count))
        send_R1(500+(x+10)+(disc_count-x))
		queue.get()
    update_coil(context, "R1S1", [1])
    update_coil(context, "R1S9", [0])

#sends command to unload treatment 3 via tcp to the sensor pi
def unload_treatment_3(context, disc_count, queue):
    update_coil(context, "R1S1", [0])
    update_coil(context, "R1S10", [1])
    for x in range(0, disc_count):
        print("Getting disc: " + str(disc_count))
        send_R1(600+(x+10)+(disc_count-x))
		queue.get()
    update_coil(context, "R1S1", [1])
    update_coil(context, "R1S10", [0])

#sends command to unload a failed via tcp to the sensor pi
# TODO check which treatment site failed, have something here that will tell
# the robots which treatment site whould be unloaded
# I.e. if treatment 1 fails, don't unload it normally, but hit this instead
def unload_failed_treatment(context, disc_count):
    update_coil(context, "R1S1", [0])
    update_coil(context, "R1S11", [1])
    for x in range(0, disc_count):
        print("Getting disc: " + str(disc_count))
        time.sleep(10)
    update_coil(context, "R1S1", [1])
    update_coil(context, "R1S11", [0])


# Robot 2 retrieves treatment tray 1 from it's designated slot
def get_tray_1(context, queue):
    print("grabbing tray 1")
    update_coil(context, "R2S1", [0])
    update_coil(context, "R2S2", [1])
    send_R2(1)
	queue.get()
    update_coil(context, "R2S1", [1])
    update_coil(context, "R2S2", [0])

# Robot 2 retrieves treatment tray 2 from it's designated slot
def get_tray_2(context, queue):
    print("grabbing tray 2")
    update_coil(context, "R2S1", [0])
    update_coil(context, "R2S3", [1])
    send_R2(2)
	queue.get()
    update_coil(context, "R2S1", [1])
    update_coil(context, "R2S3", [0])

# Robot 2 retrieves treatment tray 3 from it's designated slot
def get_tray_3(context, queue):
    print("grabbing tray 3")
    update_coil(context, "R2S1", [0])
    update_coil(context, "R2S4", [1])
    send_R2(3)
	queue.get()
    update_coil(context, "R2S1", [1])
    update_coil(context, "R2S4", [0])

# Robot 2 stows treatment tray 1 back in the designated slot
def stash_tray_1(context, queue):
    print("stowing tray 1")
    update_coil(context, "R2S1", [0])
    update_coil(context, "R2S5", [1])
    send_R2(4)
	queue.get()
    update_coil(context, "R2S1", [1])
    update_coil(context, "R2S5", [0])

# Robot 2 stows treatment tray 2 back in the designated slot
def stash_tray_2(context, queue):
    print("stowing tray 2")
    update_coil(context, "R2S1", [0])
    update_coil(context, "R2S6", [1])
    send_R2(5)
	queue.get()
    update_coil(context, "R2S1", [1])
    update_coil(context, "R2S6", [0])

# Robot 2 stows treatment tray 3 back in the designated slot
def stash_tray_3(context, queue):
    print("stowing tray 3")
    update_coil(context, "R2S1", [0])
    update_coil(context, "R2S7", [1])
    send_R2(6)
	queue.get()
    update_coil(context, "R2S1", [1])
    update_coil(context, "R2S7", [0])

# Robot 2 stows ailed treatment tray back in the designated slot
def stash_tray_f(context):
    update_coil(context, "R2S1", [0])
    update_coil(context, "R2S8", [1])
    time.sleep(10)
    update_coil(context, "R2S1", [1])
    update_coil(context, "R2S8", [0])

# State machine for the loader robot
# handles the logic for a complete 'Cycle' for loader robot 1
# handles partial control logic for an entire cycle. e.g. tells treatments to start
# Works syncronously with stacker robot, conveyor and treatment sites
# to ensure that a strict order of events is maintained
def loader_State_Machine(context, visionQueue, conveyorQueue, treatmentQueue, loader_robot_queue, stack_robot_queue):
    time.sleep(10)
    print("Setting intial state R1")
    update_coil(context, "R1S1", [1])
    time.sleep(10)
	get_vision_baseline()
	visionQueue.get()
    get_tray_initial(context, loader_robot_queue)
    get_vision_results()
    results = visionQueue.get()
    print("Checking that visionQueue shit: " + str(results))
    count = 1
    t1 = []
    t2 = []
    t3 = []
    for treatmentType in results.split(","):
        if treatmentType == "1":
            disc_to_t1(context, count, loader_robot_queue)
            t1.append(count)
        elif treatmentType == "2":
            disc_to_t2(context, count, loader_robot_queue)
            t2.append(count)
        elif treatmentType == "3":
            disc_to_t3(context, count, loader_robot_queue)
            t3.append(count)
        else:
            disc_to_quarantine(count)
        count += 1
    return_unsorted_tray(context, loader_robot_queue)
    stackrobotqueue.put(GET_T1)
    treatment_count = 0
    if len(t1) > 0:
        start_treatment_1()
        treatment_count += 1
    if len(t2) > 0:
        start_treatment_2()
        treatment_count += 1
    if len(t3) > 0:
        start_treatment_3()
        treatment_count += 1

    for x in range(0, treatment_count):
        unload = treatmentQueue.get()
        if unload == UNLOAD_T1:
            loader_robot_queue.get()
            unload_treatment_1(context, len(t1), loader_robot_queue)
            control_conveyor(RIGHT_COMMAND)
            stackrobotqueue.put("T1_COMPLETE")
        elif unload == UNLOAD_T2:
            loader_robot_queue.get()
            unload_treatment_2(context, len(t2), loader_robot_queue)
            control_conveyor(RIGHT_COMMAND)
            stackrobotqueue.put("T2_COMPLETE")
        elif unload == UNLOAD_T3:
            loader_robot_queue.get()
            unload_treatment_3(context, len(t3), loader_robot_queue)
            control_conveyor(RIGHT_COMMAND)
            stackrobotqueue.put("T3_COMPLETE")
        elif unload == UNLOAD_F:
            # TODO INSERT HERE TO CHECK WHAT SHIT FUCKED UP AND FAILED
            unload_failed_treatment(context)
            stackrobotqueue.put("TF_COMPLETE")
        else:
            print("What is happening in the unload phase guys???")


# State machine for the stacker robot
# works syncronously with loader robot to ensure a strict series of events
# Handles some extra control logic, such as commands to rol lthe conveyor
def stacker_State_Machine( context, stack_robot_queue, loader_robot_queue, conveyor_queue):
    time.sleep(10)
    print("Setting intial state R2")
    update_coil(context, "R2S1", [1])
    stack_robot_queue.get()
    get_tray_1(context, stack_robot_queue)
    control_conveyor(LEFT_COMMAND)
    conveyor_queue.get()
    loader_robot_queue.put(UNLOAD_T1)
    conveyor_queue.get()
    if stack_robot_queue.get() == "T1_COMPLETE":
        stash_tray_1(context, stack_robot_queue)
    else:
        print("Just what the hell kinda stash order is this? Tray 1 goes here")
    # This is grossly copy pasted TODO make this nice if i get the time

    get_tray_2(context, stack_robot_queue)
    control_conveyor(LEFT_COMMAND)
    conveyor_queue.get()
    loader_robot_queue.put(UNLOAD_T2)
    conveyor_queue.get()
    if stack_robot_queue.get() == "T2_COMPLETE":
        stash_tray_2(context, stack_robot_queue)
    else:
        print("Just what the hell kinda stash order is this? Tray 2 goes here")
    # This is grossly copy pasted TODO make this nice if i get the time

    get_tray_3(context, stack_robot_queue)
    control_conveyor(LEFT_COMMAND)
    conveyor_queue.get()
    loader_robot_queue.put(UNLOAD_T3)
    conveyor_queue.get()
    if stack_robot_queue.get() == "T3_COMPLETE":
        stash_tray_3(context, stack_robot_queue)
    else:
        print("Just what the hell kinda stash order is this? Tray 2 goes here")

# ---------------------------------------------------------------------------#
# updates a register value
# regname is the name of the register provided in the list at initialisation of the server
# regval is the new value you want this register to hold
# ---------------------------------------------------------------------------#
def update_register( context, regname, regval):
    register = 3
    address = 0x00 + register_names.index(regname)
    context[slave_id].setValues(register, address, [regval])

# ---------------------------------------------------------------------------#
# gets a register value
# regname is the name of the register provided in the list at initialisation of the server
# returns the current value of the named register
# ---------------------------------------------------------------------------#
def get_register(context, regname ):
    register = 3
    address = 0x00 + register_names.index(regname)
    return context[slave_id].getValues(register, address)


# ---------------------------------------------------------------------------#
# updates a coil value with a new value (should be 1 or 0)
# TODO: enforce the boolean nature of the coil on write
# coilname is the name of the coil provided in the list at initialisation of the server
# coilval is the new value you want this register to hold
# ---------------------------------------------------------------------------#
def update_coil( context, coilname, coilval):
    register = 1
    address = 0x00 + coil_names.index(coilname)
    context[slave_id].setValues(register, address, coilval)


# ---------------------------------------------------------------------------#
# gets a coil value
# coil is the name of the coil provided in the list at initialisation of the server
# returns the current value of the named coil (should be one or zero)
# ---------------------------------------------------------------------------#
def get_coil( context, coilname ):
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
# This is boilerplate - please delete me, I'm worthless
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
def server_start(pi_address):
    # This is the IP of my rasp pi
    if initialised:
        time = 2
        vision_queue = Queue()
        conveyor_queue = Queue()
        treatment_queue = Queue()
        load_robot_queue = Queue()
        stack_robot_queue = Queue()
        Thread(target=socket_broker, args=(pi_address, vision_queue, conveyor_queue, treatment_queue, load_robot_queue, stack_robot_queue)).start()
        Thread(target=loader_State_Machine, args=(context, vision_queue, conveyor_queue, treatment_queue, load_robot_queue, stack_robot_queue)).start()
        Thread(target=stacker_State_Machine, args=(context, stack_robot_queue, load_robot_queue, conveyor_queue)).start()
        StartTcpServer(context, identity890=identity, address=(pi_address, 5021))
    else:
        print('Please Initialise the server before trying to start')


sensorList = ["alcohol"];
# -------------------------------------------------------------------------
# The following states have been derrived from the System Design Document,
# whereas some states have been added to expand upon the proposed
# states to ensure functionality
# R1 refers to the loader robot
# R2 refers to the stacker robot
# |State    |Description
# -----------------------------
# |R1S1     |Wait/Rest State
# |R1S2     |Unsorted waste tray to conveyor
# |R1S3     |Identified T1 wate discs to treatment area
# |R1S4     |Identified T2 wate discs to treatment area
# |R1S5     |Identified T3 wate discs to treatment area
# |R1S6     |Unidentified wate discs to quarantine area
# |R1S7     |Unsorted waste tray back to holding area
# |R1S8     |Unload T1 waste Treatment site to tray
# |R1S9     |Unload T2 waste Treatment site to tray
# |R1S10    |Unload T3 waste Treatment site to tray
# |R1S11    |Unload failed waste Treatment site to tray
# |R1S12    |Failed robot state
# |R2S1     |Wait/RestState
# |R2S2     |Retrieve T1 Tray from storage, place on conveyor
# |R2S3     |Retrieve T2 Tray from storage, place on conveyor
# |R2S4     |Retrieve T3 Tray from storage, place on conveyor
# |R2S5     |Retrieve Failed Tray from storage, place on conveyor
# |R2S6     |Stash T1 Tray in storage
# |R2S7     |Stash T2 Tray in storage
# |R2S8     |Stash T3 Tray in storage
# |R2S9     |Stash Failed Tray in storage
# |R2S10    |Failed robot State

coilList = ["R1S1", "R1S2", "R1S3", "R1S4", "R1S5", "R1S6", "R1S7", "R1S8", "R1S9", "R1S10", "R1S11", "R2S1", "R2S2",
            "R2S3", "R2S4", "R2S5", "R2S6", "R2S7", "R2S8", "R2S9", "R2S10"]
registerList = [""]
initialise_server(sensorList, coilList)
server_start(MY_IP)

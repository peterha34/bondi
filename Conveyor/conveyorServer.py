import socket
import time
from threading import Thread
import motortest as conveyor
from pymodbus.server.async import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer

myIP = '192.168.1.3'
##myIP = '172.19.125.238'
movePort = 8091
stopPort = 8090
robotIP = '192.168.1.5'
robotPort = 8080
LEFT_COMMAND = "LEFT"
RIGHT_COMMAND = "RIGHT"
STOP_COMMAND = "STOP"
RETURN_MSG = ""
context = None
slave_id = 0x00

def start_thread_stop(passedContext):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((myIP, stopPort))
    serversocket.listen(1) # become a server socket, maximum 5 connections

    while True:
        print("loopin stop thread\n")
        connection, address = serversocket.accept()
        buf = connection.recv(64)
        if buf == STOP_COMMAND:
            print STOP_COMMAND
            conveyor.stop()
            update_coil("stopped", [1], passedContext)
        time.sleep(0.5)

def start_thread_main(passedContext):
    # Also start stop thread listening for emergency stop
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((myIP, movePort))
    serversocket.listen(1) # become a server socket, maximum 5 connections

    while True:
        print("loopin main thread")
        connection, address = serversocket.accept()
        buf = connection.recv(64)
        if buf == LEFT_COMMAND:
            print LEFT_COMMAND
            update_coil("stopped", [0], passedContext)
            update_coil("left", [1], passedContext)
            conveyor.move(0,3.5)
            update_coil("left", [0], passedContext)
            update_coil("stopped", [1], passedContext)
            CONVEYOR_RETURNS = "Left move success"
        elif buf == RIGHT_COMMAND:
            print RIGHT_COMMAND
            update_coil("stopped", [0], passedContext)
            update_coil("right", [1], passedContext)
            conveyor.move(1,3.5)
            update_coil("right", [0], passedContext)
            update_coil("stopped", [1], passedContext)
            CONVEYOR_RETURNS = "Right move success"
        else:
            print "Invalid command"
            CONVEYOR_RETURNS = "Invalid command"
            
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect((robotIP, robotPort))
        clientsocket.send("CONVEYOR_DATA:" + CONVEYOR_RETURNS)
        time.sleep(0.5)


def update_register( regname, regval, context, ):
    register = 3
    address = 0x00 + register_names.index(regname)
    context[slave_id].setValues(register, address, [regval])

# ---------------------------------------------------------------------------#
# gets a register value
# regname is the name of the register provided in the list at initialisation of the server
# returns the current value of the named register
# ---------------------------------------------------------------------------#
def get_register(regname, context ):
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
def get_coil(coilname, context ):
    register = 1
    address = 0x00 + coil_names.index(coilname)
    return context[slave_id].getValues(register, address)

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

coilList = ["right", "left", "stopped"]
initialise_server( "null", coilList)
update_coil("stopped", [1], context)
Thread(target=start_thread_main, args=(context,)).start()
Thread(target=start_thread_stop,args=(context, )).start()
StartTcpServer(context, identity=identity, address=(myIP, 5020))


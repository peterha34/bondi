#!/usr/bin/python

##
## Licensed Material - Property of IBM
## (c) Copyright IBM Corp. 2017.  All Rights Reserved.
##

import bluepy
import threading
import time
import re
import argparse
import sys

gworg = ''
gwdevtype = ''
gwdevid = ''
gwtoken = ''

# this name is the BTLE characteristic which gives the device type
BTNAME='Complete Local Name'

# I have never had this many sensortags, there may be a lower limit in the bluetooth stack/hardware
MAXDEVICES=16

# the interval in seconds for fast/medium/slow reading of sensors
FAST = 0.2
MEDIUM = 1.0
SLOW = 5.0

SENSORTYPES = [
    'accelerometer'
    ,'barometer'
#    ,'battery'
    ,'gyroscope'
    ,'humidity'
    ,'IRtemperature'
#    ,'keypress'
    ,'lightmeter'
    ,'magnetometer'
]

# devicenames maps a device mac address like to a friendly name
# it is initialised from devices.txt. If a device isn't present, 
# a device name is created (in class _paireddevice) of the format of ST-n
# where n is the number of known device names+1
# which means you can design your IoTP for names liek ST-1, ST-2, ST-3 etc.
devicenames = {}
DEVICENAMESFILE = 'devices.txt'

# from http://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float-in-python
def is_float(text):
    try:
        float(text)
        # check for nan/infinity etc.
        if str(text).isalpha():
            return False
        return True
    except ValueError:
        return False
    except TypeError:
        return False

class _paireddevice():
    def __init__( self, dev, devdata ):
        if args.info:
            print "devdata=",devdata
        self.devdata = devdata
        self.name = self.devdata[ BTNAME ]
        if dev.addr not in devicenames:
            # the devices are named in order of discovery
            # remember automatically-assigned names so if the device goes away
            # and comes back in the same run it gets the same name
            devicenames[dev.addr] = args.name + chr(48+len(devicenames)+1)
        self.friendlyname = devicenames[dev.addr]
        self.addr = dev.addr
        self.addrType = dev.addrType
        self.rssi = dev.rssi
        self.report("status","found")
        if args.info:
            print "created _paireddevice"
#    # pair
#    def pair(self):
#        print "pairing"
#        pass
    def unpair(self):
        if args.info:
            print "unpairing", self
        self.running = False
        for thread in self.threads:
            thread.join()
        pass
    def _sensorlookup(self, sensorname):
        if not hasattr(self.tag, sensorname):
            if args.info:
                print "not found",sensorname
            return None
        return getattr(self.tag,sensorname)
        
    # do whatever it takes to kick off threads to read the sensors in f,m,s 
    # at read rates FAST, MEDIUM, SLOW
    def start(self, f,m,s):
        """
        f,m,s are list of sensor names to run at FAST, MEDIUM and SLOW read rates
        """
        if args.info:
            print "starting",f,m,s
        self.running = True
        self.threads = []
        for sensors,interval in zip([f,m,s],[FAST,MEDIUM,SLOW]):
            if sensors:
                self.threads.append(threading.Thread(target=self.runner,args=(sensors,interval)))
#                print "setting daemon"
                self.threads[-1].daemon = True
                self.threads[-1].start()
    def runinit(self, sensors):
        if args.info:
            print "initializing for run", sensors
        return False
    def runread(self,sensors):
        if args.info:
            print('Doing something important in the background', self, sensors)
        return False
    def runner(self,sensors,interval):
        """ Method that runs forever """
        if not self.runinit(sensors):
            return
        while self.running:
            # Do something
            if not self.runread(sensors):
                break
#            print "pausing for",self.interval
            time.sleep(interval)
        if args.info:
            print "Aborting"
    def report(self,tag,value=None):
#        print "report",self.addr, self.friendlyname, tag, value
        if is_float(value):
            print '{"deviceuid":"'+self.addr+'","devicename":"'+self.friendlyname+'","'+tag+'":'+str(value)+'}'
        else:
            if not isinstance(value, basestring):
                # a lit of numbers
#                print "["+",".join([str(x) for x in value])+"]"
                print '{"deviceuid":"'+self.addr+'","devicename":"'+self.friendlyname+'","'+tag+'":'+"["+",".join([str(x) for x in value])+"]"+'}'
            else:
                # a simple string
                print '{"deviceuid":"'+self.addr+'","devicename":"'+self.friendlyname+'","'+tag+'":"'+str(value)+'"}'
        sys.stdout.flush()

# this is a generic sensortag
class _SensorTag(_paireddevice):
    def __init__( self, dev, devdata):
        if args.info:
            print "creating _SensorTag"
        self.tag = bluepy.sensortag.SensorTag(dev.addr)
        _paireddevice.__init__( self, dev, devdata )
        self.devicetype = "SensorTag generic"
        if args.info:
            print "created _SensorTag"
        return True
    def runinit(self, sensors):
        if args.info:
            print "_Sensortag runinit", sensors
        self.report("status","enabled "+repr(sensors))
        for sensor in sensors:
            if args.info:
                print "enabling",sensor
            tagfn = self._sensorlookup(sensor)
            if tagfn:
                tagfn.enable()
#        time.sleep( 1.0 )
        return True
    def runread(self, sensors):
        try:
            for sensor in sensors:
                tagfn = self._sensorlookup(sensor)
                if tagfn:
                    self.report(sensor, tagfn.read())
        except bluepy.btle.BTLEException:
            self.report("status","lost")
            return False
        return True

# this is a CC2650 sensortag        
class _ST2650(_SensorTag):
    def __init__( self, dev, devdata ):
        if args.info:
            print "creating _ST2650"
        _SensorTag.__init__( self, dev, devdata )
        self.devicetype = "Sensortag CC2650"
        self.report("status","started")
        if args.info:
            print "created _ST2650"
        
# this is a CC2540
class _ST(_SensorTag):
    def __init__( self, dev, devdata ):
        if args.info:
            print "creating _ST"
        _SensorTag.__init__( self, dev, devdata )
        self.devicetype = "Sensortag CC2540"
        self.report("status","started")
        if args.info:
            print "created _ST"
# depending on the bluetooth device type, this
# creates an instance of the appropriate class
def paireddevicefactory( dev ):
    # get the device name to decide which type of device to create
    devdata = {}
    for (adtype, desc, value) in dev.getScanData():
        devdata[desc]=value
    if BTNAME not in devdata.keys():
        devdata[BTNAME] = 'Unknown!'
    if args.info:
        print "Found",devdata[BTNAME]
    if devdata[BTNAME] == 'SensorTag':
        return _ST( dev, devdata )
    elif devdata[BTNAME] == 'CC2650 SensorTag':
        return _ST2650( dev, devdata)
    return None
    
# this scandelegate handles discovery of new devices
class ScanDelegate(bluepy.btle.DefaultDelegate):
    def __init__(self):
        bluepy.btle.DefaultDelegate.__init__(self)
        self.activedevlist = []
#        self.gw = gateway
    def handleDiscovery(self, dev, isNewDev, isNewData):
        global args
        if isNewDev:
            if args.info:
                print "found", dev.addr
            if args.only:
                if args.info:
                    print "only", dev.addr, devicenames
                if dev.addr not in devicenames:
                    # ignore it!
                    if args.info:
                        print "ignoring only",dev.addr
                    return
            if len(self.activedevlist)<MAXDEVICES:
                thisdev = paireddevicefactory(dev)
                if args.info:
                    print "thisdev=",thisdev
                if thisdev:
                    self.activedevlist.append(thisdev)
    #                thisdev.pair()
                    thisdev.start(args.fast,args.medium,args.slow)
                if args.info:
                    print "activedevlist=",self.activedevlist
            else:
                if args.info:
                    print "TOO MANY DEVICES - IGNORED",dev.addr
            # launch a thread which pairs with this device and reads temperatures
        elif isNewData:
            if args.info:
                print "Received new data from", dev.addr
            pass
            
    def shutdown( self ):
        if args.info:
            print "My activedevlist=",self.activedevlist
        # unpair the paired devices
        for dev in self.activedevlist:
            if args.info:
                print "dev=",dev
            dev.unpair()

    
# specify commandline options       
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name",help="basename for default device names if uid not specified in -d option (only used if -o not specified) default is 'ST-' followed by a digit")
parser.add_argument("-f", "--fast",nargs='*', choices=SENSORTYPES, help="list of sensors for fast read rate - defaults to fast read of accelerometer and lightmeter if none of -f/-m/-s are specified")
parser.add_argument("-m", "--medium", nargs='*', choices=SENSORTYPES, help="list of sensors for medium read rate - defaults to fast read of accelerometer and lightmeter if none of -f/-m/-s are specified")
parser.add_argument("-s", "--slow", nargs='*', choices=SENSORTYPES, help="list of sensors for slow read rate - defaults to fast read of accelerometer and lightmeter if none of -f/-m/-s are specified")
parser.add_argument("-i", "--info", action="store_true", help='turn on debugging prints (only use from command line)') 
parser.add_argument("-o", "--only", action="store_true", help='restrict recognized devices to only those specified with -d')
parser.add_argument("-d", "--device", nargs='*',help="Give device with uid a friendly name, in format: uid=friendlyname e.g. a0:e6:f8:b6:34:83=SHOULDER")

args = parser.parse_args()
if not args.name:
    args.name = "ST-"
if args.info:
    print "only=",args.only
    
if not args.fast and not args.medium and not args.slow:
    # no setting specified - use the defaults
    args.medium = None
    args.slow = None
    args.fast = ['accelerometer','lightmeter']
    
if args.info:
    print args.fast
    print args.medium
    print args.slow

if args.device:
    devicenames = {}
    for dev in args.device:
        (uid,devname) = dev.split("=",2)
        if not uid or not devname:
            print "could not split device",dev
            burp
        devicenames[uid.lower()] = devname
        
if args.info:
    print "specified devices:",devicenames    

scandelegate = ScanDelegate()
scanner = bluepy.btle.Scanner().withDelegate(scandelegate)

#while keepScanning:
# scan for a while - until ^C is pressed
try:
    while True:
        try:
            devices = scanner.scan(timeout=30.0)
        except bluepy.btle.BTLEException:
            if args.info:
                print "Aargh BTLE execption. Not panicing. Carrying on."
except KeyboardInterrupt:
    pass
    
if args.info:
    print "finishing"
    
scandelegate.shutdown()

if args.info:
    print "finished"

# -*- coding: utf-8 -*-
import wiringpi
from time import sleep

#Moves the conveyor in a direction for a set time
#dir 1: forwards
#    0: backwards
#time : time motor is on in seconds
def move(direction, time):
    try:
        wiringpi.wiringPiSetup()
        wiringpi.pinMode(0,1) #GPIO0 PiPin11
        wiringpi.pinMode(1,1) #GPIO1 PiPin12

        sleep(1) #So i dont break the motor

        if (direction):
            wiringpi.digitalWrite(0,1)
        else:
            wiringpi.digitalWrite(1,1)
        sleep(time) #time to leave motor running
        wiringpi.digitalWrite(0,0)
        wiringpi.digitalWrite(1,0)
        wiringpi.pinMode(0,0)
        wiringpi.pinMode(1,0)
    except:
        print "External Interrupt"
        wiringpi.digitalWrite(0,0)
        wiringpi.digitalWrite(1,0)
        wiringpi.pinMode(0,0)
        wiringpi.pinMode(1,0)
    return;

def stop():
        wiringpi.digitalWrite(0,0)
        wiringpi.digitalWrite(1,0)
        wiringpi.pinMode(0,0)
        wiringpi.pinMode(1,0)
    return;


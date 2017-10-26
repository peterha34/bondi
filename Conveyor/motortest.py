# -*- coding: utf-8 -*-
import wiringpi
from time import sleep

#Moves the conveyor in a direction for a set time
#dir 1: forwards
#    0: backwards
#time : time motor is on in seconds
def conveyor_init():
    wiringpi.wiringPiSetup()

def move(direction, time):
    try:
        conveyor_init()
        wiringpi.pinMode(0,1) #GPIO0 PiPin11
        wiringpi.pinMode(1,1) #GPIO1 PiPin12

        sleep(0.8) #So i dont break the motor

        if (direction):
            wiringpi.digitalWrite(0,1)
        else:
            wiringpi.digitalWrite(1,1)
            
        idle(time) #time to leave motor running
        stop()
    except:
        print "External Interrupt"
        stop()
    return;

def idle(time):
    seconds = 0
    while float(seconds) < float(time):
        if wiringpi.digitalRead(0) or wiringpi.digitalRead(1):
            seconds += 0.5
            sleep(0.5)
        else:
            return
    return;

def stop():
    wiringpi.digitalWrite(0,0)
    wiringpi.digitalWrite(1,0)
    wiringpi.pinMode(0,0)
    wiringpi.pinMode(1,0)
    return;

move(1,3)
move(0,3)

# -*- coding: utf-8 -*-
import wiringpi
from time import sleep

"""Moves the conveyor in a direction for a set time
dir: 1 forwards, 0 backwards
time: time motor is on in seconds """
def move(direction, time):
    #Set both pins to 1: output mode
    wiringpi.pinMode(0,1) #GPIO-0 or PiPin-11
    wiringpi.pinMode(1,1) #GPIO-1 or PiPin-12

    #Set pinout high(1) to control forward or reverse 
    if (direction):
        wiringpi.digitalWrite(0,1)
    else:
        wiringpi.digitalWrite(1,1)
        
    sleep(time) #time to leave motor running for

    #Then reset the pins for another day
    wiringpi.pinMode(0,0)
    wiringpi.pinMode(1,0)
    sleep(2) #So i dont break the motor...again...
    return;

wiringpi.wiringPiSetup()

move(1,5) #Sample use of move function, forwards for 5 seconds
 



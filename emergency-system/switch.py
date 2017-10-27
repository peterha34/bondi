'''
Emergency stop functionality test code
Acknowledgement: http://razzpisampler.oreilly.com/ch07.html
'''
import RPi.GPIO as GPIO
import time
import datetime
import csv

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    with open ('debuglog.csv', 'a') as csvfile:
        debugwriter = csv.writer(csvfile)
        debug_time = datetime.datetime.now()        
        input_state = GPIO.input(24)
        if input_state == False:
            print('Button Pressed')
            debugwriter.writerow([debug_time, 'Button Pressed'])
            time.sleep(0.2)

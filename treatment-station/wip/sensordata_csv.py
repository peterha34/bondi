import csv
import datetime
import random
import time

with open('sensordata.csv', 'a') as csvfile:
    sensorwriter = csv.writer(csvfile)
    sensorwriter.writerow(['Time', 'Temperature (C)', 'Acceleration']) 
    while True:
        time_now = datetime.datetime.now()
        temp = random.uniform(-32, 100) # add in proper temp datahere
        acceleration = random.uniform(0, 10) # tba proper data
        print('Time: {0} Temperature: {1} Acceleration: {2}'.format(time_now, temp, acceleration))
        sensorwriter.writerow([time_now, temp, acceleration])
        time.sleep(1)

import sensortag
import os

os.system("sudo service bluetooth restart")
os.system("sudo python sensortag.py -t 1.0 -T 24:71:89:E8:85:83")

print('Temp: ', sensortag.tag.IRtemperature.read())

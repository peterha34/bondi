Main file: treatment.py - Authours: Mathew Mason, John Thai

TI sensor tag file: cc2650sensortag.py - Authour: John Thai, Acknowledgement: Ian Harvey 

Gas sensor files: mq.py, MCP3008.py - Authour: tutRPi

## Operation Ovewview ##
* Sensors measure temperature, acceleration, alcohol, light and humidity. 
* Automatically start taking in treatment value from sensor on boot up.
** System initialise to a set state when boot up.
** Sensor recover to current state after power outage.
* Persistent sensor data are stored in the each RTU.
* Treatment RTU communicates with robots PLC.
* Treatment RTU communicates with server.

## Hardwares ##
* Raspberry Pi 3
* TI Sensor Tags
* MQ 3 Gas Sensor

## Installation Guide ## 
* Set-up MQ 3 Gas sensor according to the diagram below.

![MQ gas sensor wiring](../Raspberry-Pi-Gas-Sensor-MQ2-Steckplatine.png)

* Edit device MAC Address according to the sensor MAC Address in treament.py and cc2650sensortag.py file.
* Setup IP address for the RTU and its connection in treament.py file accordingly. View Appendix A for our IP assignment.
* Turn on the TI sensor tags.
* Reboot the Raspberry Pi.

## Maintenance ##
* Turn on the TI sensor tags before switching on the Raspberry Pi.
* Check csv files located in treatment-station folder to view data received from sensors.
* Manually end the monitoring process of the sensor.
** To receive the process id 
```bash
pgrep -a python
```

To end the process 

```bash
kill -9 <process id>
```

Run treatment station file

```bash
python treatment.py
```
## To be added ##
* Each sensor monitor each other

## References ##
[MQ-x Gas Sensor Guide](https://tutorials-raspberrypi.com/configure-and-read-out-the-raspberry-pi-gas-sensor-mq-x/)

[Bluepy Library for TI Sensor Tag Guide](https://github.com/IanHarvey/bluepy)

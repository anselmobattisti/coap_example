#!/usr/bin/env python
# python sensor.py s1 15
# the first parameter is the sensor name
# the second parameter is it's threshold

import getopt
import socket
import sys
import time

from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri

from sense_emu import SenseHat

sense = SenseHat()

red = (255, 0, 0)
white = (255, 255, 255)

h_lim = int(sys.argv[4])
path = "coap://"+sys.argv[1]+":"+sys.argv[2]+"/"+sys.argv[3]
host, port, path = parse_uri(path)

# print path
# print host
# print port
# print path
# print h_lim

client = HelperClient(server=(host, port))

# use example
# response = client.get(path)
# print response.payload

while True:    
    time.sleep(1)
    response = client.get(path)  
    humidity = 0
    try:
        humidity = int(response.payload)
        pixels = [red if humidity > h_lim else white for i in range(64)]
        sense.set_pixels(pixels)        
    except:
        print('Humidity is not defined or is not a number')


client.stop()
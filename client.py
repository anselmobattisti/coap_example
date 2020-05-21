#!/usr/bin/env python
# python client.py 127.0.0.1 5683 s1 10 0
# 1 - CoaP server IP
# 2 - CoaP port
# 3 - Sensor ID, CoaP resource
# 4 - Humidity Limit
# 5 - Led that will blink at SenseHat

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
led = int(sys.argv[5])
pixels = [None]*64

# print path
# print host
# print port
# print path
# print h_lim

client = HelperClient(server=(host, port))

while True:    
    time.sleep(1)
    response = client.get(path)  
    humidity = 0
    try:
        humidity = int(response.payload)
        for i in range(64):
            pixels[i] = white
        if (humidity > h_lim):
            pixels[led] = red
        sense.set_pixels(pixels)        
    except:
        print('Humidity is not defined or is not a number')


client.stop()
	
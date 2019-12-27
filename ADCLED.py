import smbus
import time
from flask import Flask, escape, request
## Get I2C bus
bus = smbus.SMBus(1)

## AD5669 address 0x56
## select DAC and input and register, (0x2F(47)
## select all DAC channels 0x8000(32768)

## asks for user data input

y = input("input voltage from 0-5V:")

vol = (255*((y-0.034)/(1.032)))/5.000
vol = int(round(vol))

x = (hex(vol))

data = [int(x , 16), 0x00]

channel = input("input channel here:")
hchanu = hex(channel)

hchanr= int(hchanu , 16)


bus.write_i2c_block_data(0x56, hchanr, data)

time.sleep(0.5)

##converts signal to voltage

voltage = 5.0*((data[0] * 256 +data[1])/ 65536.0) 


print "Voltage :%.2f V" %voltage
 
print x

print vol

#!/usr/bin/python
import time
import serial
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial= GPIO.LOW)

Ser1 = serial.Serial('/dev/ttyUSB1',9600)
                   
Ser1.flushInput()

while True:
    if Ser1.inWaiting():
        mdata = Ser1.read().decode()

        if mdata == Ser1.readline().decode().strip():
            mdata = mdata.split('#')
            sensor = int (mdata[1])
            print ("ID : {}, Intensitas : {}".format (mdata[0], sensor))

Ser1.close()
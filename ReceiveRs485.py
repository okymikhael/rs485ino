#!/usr/bin/python
import time
import serial
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial= GPIO.LOW)

Ser1 = serial.Serial('/dev/ttyUSB0',9600)
                   
Ser1.flushInput()

while True:
    print("Waiting")
    if Ser1.inWaiting():
        mdata = Ser1.read().decode()
        print(mdata)

        if mdata == Ser1.readline().decode().strip():
            mdata = mdata.split('#')
            sensor = int (mdata[1])
            print ("ID : {}, Intensitas : {}".format (mdata[0], sensor))

    sleep(1)
# Ser1.close()
import time
import serialy
import os
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

send = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

send.flush()
while True:
    line = send.readline().decode('utf-8').rstrip()
    print(len(line))
    id_arduino = line[1:3]
    data = line[4:]
    print ("ID : {}, Intensitas : {}".format (id_arduino, data))

    if len(line) == 0:
        os.system('python3 ReceiveRs485.py')

    sleep(1)
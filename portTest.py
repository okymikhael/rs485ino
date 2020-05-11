import time
import serial
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

send = serial.Serial(
    port='/dev/serial0',
    baudrate = 9600,
    # parity=serial.PARITY_NONE,
    # stopbits=serial.STOPBITS_ONE,
    # bytesize=serial.EIGHTBITS,
    timeout=10
)

while True:
    try:
        mdata = send.read().decode()
        print(mdata)
        print(send.readline())
    except:
        print("Data Loss")
    
    
    # if mdata == send.readline().decode().strip():
    #     mdata = mdata.split('#')
    #     sensor = int (mdata[1])
    #     print ("ID : {}, Intensitas : {}".format (mdata[0], sensor))

    time.sleep(1)

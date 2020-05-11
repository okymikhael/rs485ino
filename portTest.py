import time
import serial
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

send.flushInput()
send.flushOutput()

while True:
    bytesToRead = send.inWaiting()
    send.read(bytesToRead)
# while True:
    # try:
    # if send.in_waiting:
    #     mdata = send.read().decode()
    #     print(mdata)
    #     print(send.readline())
        
    #     if mdata == send.readline().decode().strip():
    #         mdata = mdata.split('#')
    #         sensor = int (mdata[1])
    #         print ("ID : {}, Intensitas : {}".format (mdata[0], sensor))

    # print(send.readline())
    sleep(1)

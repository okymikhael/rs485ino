import time
import serial
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
# send = serial.Serial('/dev/ttyUSB0', 4800, 8, 'N', 1, timeout=1)

# send.reset_input_buffer()
# send.flush()


send.flush()
# send.reset_input_buffer()
while True:
    line = send.readline().decode('utf-8').rstrip()
    print(line)

    if len(line) == 0:
        os.system('python my_file.py')
        exit()

    sleep(1)


# send.reset_output_buffer()
# flushinput()
# while True:
#     # try:
#     if send.inWaiting():
#         # mdata = send.read().decode()
#         # send.flushInput()
#         # print(mdata)
#         print(send.readline())
#         print(send.readline().decode('utf-8').rstrip())
#         send.flush()
#         # if mdata == send.readline().decode().strip():
#         #     mdata = mdata.split('#')
#         #     sensor = int (mdata[1])
#         #     print ("ID : {}, Intensitas : {}".format (mdata[0], sensor))

#     # send.close()
#     sleep(3)

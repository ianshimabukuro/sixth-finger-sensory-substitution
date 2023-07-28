import serial
import math
import keyboard
import time
from functionfile import *

time.sleep(5)
arduino = serial.Serial('/dev/cu.usbmodem1201', 9600, timeout=2)#Connect to the Arduino Serial
holder='a'

keys = ['a', 'w', 's', 'e', 'd', 'f', 't', 'g', 'y', 'h', 'u', 'j']
scale=[2, 3, 7, 9, 11]

anglerange= 180/len(scale)

while True:
    # --------------Connecting to arduino and getting data from serial---------#
    buffer = arduino.in_waiting  # Check how much info is getting delayedeghj
    arduino_data = arduino.readline()  # Read line from the Arduino Serial
    Angle = int(arduino_data[0:len(arduino_data)].decode("utf-8"))  # Decode data
    section = int((Angle / anglerange) - 1)
    print(section)
    keyInd= scale[section]
    key = keys[keyInd]
    currentkey = key
    prevk = holder
    holder = currentkey

    if (prevk != currentkey):
        keyboard.release(prevk)
        keyboard.press(currentkey)










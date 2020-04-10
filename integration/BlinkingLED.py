import time
import serial
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

def readByte(sentence):
        line = ""
        while not line == sentence:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').rstrip()

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

while True: # Run forever
    #readByte("on")
    GPIO.output(3, GPIO.HIGH) # Turn on
    sleep(1) # Sleep for 1 second
    GPIO.output(3, GPIO.LOW) # Turn off
    sleep(1) # Sleep for 1 second


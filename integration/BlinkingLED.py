import time
import serial
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

ser = serial.Serial('/dev/ttyACM0',9600)

def readByte(sentence, ser): # tests if Raspi can read from Arduino
        line = ""
        while line != sentence:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').rstrip()
        GPIO.output(3, GPIO.HIGH) # Turn on LED
        sleep(1) 
        GPIO.output(3, GPIO.LOW) # Turn off LED

def sendByte(sentence, ser):
        ser.write(sentence.encode('ascii'))
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        

while True: 
    #readByte("on", ser)
    sendByte("start\n", ser)
    time.sleep(5)
    
    


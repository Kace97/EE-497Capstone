#
from datetime import datetime
import RPi.GPIO as GPIO
import time

stillMoving = True # moving the pill pack
readyToTakePill = False # comes from user's input data
powerArduinoPin = 3
readArduinoPin = 5
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(powerArduinoPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(readArduinoPin, GPIO.IN)


while True:
    now = datetime.now()
    curr_time = int(now.strftime("%H%M%S"))
    scheduled_time = 90000 # this will be a number from the database of their desired prescription time
    stillMoving = GPIO.input(readArduinoPin)
    if (stillMoving):
        GPIO.output(powerArduinoPin,GPIO.HIGH)
        stillMoving = GPIO.input(readArduinoPin)
    else:
        GPIO.output(powerArduinoPin,GPIO.LOW)
    
        # insert Steve's code to take picture of tomorrow's pills

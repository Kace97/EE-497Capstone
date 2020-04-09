#
from datetime import datetime
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)

# datetime object containing current date and time
now = datetime.now()
 
str_time = now.strftime("%H:%M:%S")
print("time =", str_time)

for i in range(5):
    GPIO.output(3,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(3,GPIO.LOW)
    time.sleep(1)

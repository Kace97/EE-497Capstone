#
from datetime import datetime
import RPi.GPIO as GPIO
import time

# datetime object containing current date and time
now = datetime.now()
 
str_time = now.strftime("%H:%M:%S")
print("time =", str_time)

for i in range(5):
    GPIO.output(3,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(3,GPIO.LOW)
    time.sleep(1)

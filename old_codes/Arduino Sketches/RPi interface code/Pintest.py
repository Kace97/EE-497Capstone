import RPi.GPIO as GPIO
from time import sleep

testpin = 4 #set the pin to be tested as pin 4

#set up initial configurations for test
GPIO.setwarnings(Fasle)#ignore warnings
GPIO.setmode(GPIO.BCM)#set the GPIO mode to BCM
GPIO.setup(testpin, GPIO.OUT)#set the test pin to be an output

#Create a for loop to blink the LED
i = 0
while i < 10:
    GPIO.output(testpin, GPIO.HIGH)#turn on the LED
    sleep(1)#wait 1 second
    GPIO.output(testpin, GPIO.HIGH)#turn off the LED
    sleep(1)#wait 1 second
    i += 1

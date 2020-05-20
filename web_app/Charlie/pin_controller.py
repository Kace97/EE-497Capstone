import RPi.GPIO as GPIO
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 4)

GPIO.setmode(GPIO.BCM)
StepPins = [17,22,23,24]
 
# Set all pins as output
for pin in StepPins:
    print("Setup pins")
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)
  
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]
       
       
def backlight_on():
    pixels[0] = (255, 255, 255)
    pixels[1] = (255, 255, 255)


def backlight_off():
    pixels[0] = (0, 0, 0)
    pixels[1] = (0, 0, 0)
	
def frontlight_on():
    pixels[2] = (255, 255, 255)
    pixels[3] = (255, 255, 255)

def frontlight_off():
    pixels[2] = (0, 0, 0)
    pixels[3] = (0, 0, 0)

def step_motor(mdir, steps, speed):
    StepCount = len(Seq)
    StepDir = mdir # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise
     
    # Initialise variables
    StepCounter = 0

    for i in range(steps):
        
        for pin in range(0, 4):
            xpin = StepPins[pin]
            if Seq[StepCounter][pin]!=0:
                #print(" Enable GPIO %i" %(xpin))
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        StepCounter += StepDir

        # If we reach the end of the sequence
        # start again
        if (abs(StepCounter) == StepCount):
            StepCounter = 0
        elif (StepCounter == 0):
            StepCounter = StepCount+StepDir

        # Wait before moving on
        time.sleep(speed)

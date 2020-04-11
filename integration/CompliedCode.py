from datetime import datetime
import time
import serial
from time import sleep


def sendByte(sentence, ser):
        sentence = sentence + "\n"
        ser.write(sentence.encode('ascii'))

def readByte(sentence, ser):
        line = ""
        while line != sentence:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').rstrip()


def takePhotos(ser): # takes photos of next day's pills
        # backlight photo
        readByte("backlight on", ser) 
        time.sleep(2) # Replace this with code to take contour photo Raspi  
        print("took contour photo")

        # front light photo
        sendByte("took contour", ser)
        readByte("front light on", ser) 
        time.sleep(2)# Replace this with code to take contour photo Raspi 
        print("took front photo")

        # send confirmation
        sendByte("took front photo", ser) 

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    while True:
            time.sleep(1) # need a delay to send first byte
            sendByte("start", ser)
            print("starting test")
            takePhotos(ser)
            # add Steve's imaging processing stuff here
            print("done")
            time.sleep(5)

            
"""
This code will be added once the webapp stuff is completed

bool sentConfirmation = False 

def sendReminder(): # add from Zhongyi's code

def confirmTakePills(): # receive notice from web app that the user agrees to take pills.
        return takePills # bool
while 1 :
        now = datetime.now()
        currTime = int(now.strftime("%H%M%S")) # 24 hr clock
        schedTime = currTime # filler for now. Will be an input time from user.
        if (schedTime == currTime): # can also add an OR statement that adds receivedReminder
                
                sendReminder() 
                while not sentConfirmation:
                        sentConfirmation = confirmTakePills

                sentConfirmation = False # reset boolean for tomorrow's meds
                
                # send code to Arduino to send pills
                # while loop reading from Arduino
                        # Arduino sends signals that says pill is dipense and backlight is lit
                
                # at this point, the packet should have dispensed to the user right now
                takePhotos()
                
                # do other imaging stuff here. Add steve's code.
                time.sleep(1000)
"""

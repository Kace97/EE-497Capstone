from datetime import datetime
import time
import serial
from time import sleep


def sendByte(sentence, ser):
        ser.write(sentence.encode('ascii'))

def readByte(sentence, ser):
        line = ""
        while line != sentence:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').rstrip()


def takePhotos(ser): # takes photos of next day's pills
        time.sleep(2) # Raspi takes picture with backlight
        sendByte("took contour\n", ser) # Raspi sends a signal back saying that it took the picture
        readByte("front light on", ser) # Arduino sends signals that says the front light is lit

        time.sleep(2)
        # Raspi takes picture with front light
        sendByte("took front photo", ser) # send confirmation code to Arduino that front photo was taken

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    while True:
            time.sleep(2)
            sendByte("on\n", ser)
            print("starting test")
            #readByte("back", ser)
            #takePhotos(ser)
            # add Steve's imaging stuff here
            print("I took a photo")
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

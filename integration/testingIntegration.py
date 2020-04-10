from datetime import datetime
import RPi.GPIO as GPIO
import time
import serial


def sendByte(sentence, ser):
        ser.write(sentence.encode('ascii'))
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)

def readByte(sentence):
        line = ""
        while not line == sentence:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').rstrip()


def takePhotos(): # takes photos of next day's pills
        # Raspi takes picture with backlight
        sendByte("took contour\n", ser) # Raspi sends a signal back saying that it took the picture
        readByte("front light on") # Arduino sends signals that says the front light is lit
        
        # Raspi takes picture with front light
        sendByte("took front photo\n", ser) # send confirmation code to Arduino that front photo was taken

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    
    sendByte("start\n", ser)
    readByte("backlight on")

    takePhotos()
    # add Steve's imaging stuff here





            
"""
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

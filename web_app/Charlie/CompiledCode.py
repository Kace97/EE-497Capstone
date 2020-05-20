from datetime import datetime
import time
import shutil
from time import sleep
import pill_analyzer as pa
import pill_segmenter as ps
from picamera import PiCamera
import cv2
import qr_reader as qr
import pin_controller as pins

# SETUP
print("Setting up system")
seg = ps.PillSegmenter()
an = pa.PillAnalyzer()
seg.thresh_thresh = 110 #100-170
seg.circle_thresh = 10 #11 is default

print("Finished Setup")

def takePhotos(): # takes photos of next day's pills
    pins.backlight_on()
    with PiCamera() as camera:
        camera.resolution=(3280,2464)
        print("Taking contour photo")
        time.sleep(1)
        camera.capture('rpi_photo.jpg')
        print("took contour photo")
        pins.backlight_off()
        pins.frontlight_on()
        print("Taking bright photo")
        time.sleep(1)
        camera.capture('lit_photo.jpg')
        print("took front photo")
        pins.frontlight_off()

def analysis(num_pills=1):
    print("Analyzing pill(s)")
    code = "no match"
    enc = an.get_encoding_from_src('images/lit_pill' + str(0) + '.jpg')
    
    print("Searching for QR Code")
    code, in_db = qr.write_to_file('images/qr_code.jpg', an.pill_index)            
    print("QR code: %s" %code)
    add_to_database(enc)

    return code, an.pill_index
                
def database_match():
    print("Finding pill(s)")
    code = "no match"
    qrnum = "none"
    enc = an.get_encoding_from_src('images/lit_pill' + str(0) + '.jpg')
    code, qrnum = qr.read_file('images/qr_code.jpg')
    pill, dist = an.get_database_match(enc)
    print(pill)
    return code, qrnum, pill, dist
                
def add_to_database(enc):
    res = an.add_to_dict(enc)
    an.database_created = False
    print("Index: ", an.pill_index)
    #an.pill_index += 1
        
def finalize_database():
    if not an.database_created:
        print("Finalizing database")
        an.database_from_dict()
        an.create_knn()
                
def get_path():
    path = 'finalImages/' + str(0) + '.jpg'
    return path
    
def get_pill_index():
    print("getting pill index: ", an.pill_index)
    return an.pill_index

def set_pill_index(index):
    an.pill_index = index
    print("set pill index")
    
def center_pill():
    dfc = 1000
    i = 0
    while(True):
        takePhotos()
        seg.original_image = cv2.imread('rpi_photo.jpg')
        seg.bright_image = cv2.imread('lit_photo.jpg')
        if i == 0:
            x,y = seg.locate_pill_and_qr(True)
        else:
            x,y = seg.locate_pill_and_qr(False)
        if x is None:
            dfc = 500
        dfc = y-seg.original_image.shape[0]/2
        if abs(dfc) < 100:
            break
        print("Round %i distance is %f" %(i,dfc))
        steps = int(abs(dfc) * 1.4)
        mdir = int(abs(dfc)/dfc)
        run_motor(mdir=mdir,steps=steps,speed=.005)
        i += 1
        
def pics_only():
    print("starting pics only")
    center_pill()
    num_pills, dfc = seg.segment_pills(firstiter = False)
    print("NEW DFC: ", dfc)
    shutil.copyfile('images/lit_pill0.jpg', 'finalImages/' + str(0) + '.jpg')
    print("done")
    return num_pills
        
def run_motor(mdir=1, steps=4000, speed=.003):
    print("running motor")
    pins.step_motor(mdir, steps, speed)
     
if __name__ == '__main__':
    print("nothing here")

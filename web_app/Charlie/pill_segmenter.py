#!/usr/bin/env python
import cv2
import numpy as np
from picamera import PiCamera
from time import sleep
import math
		
FINALPILLSIZETHRESHOLD = 80000
LARGETHRESHOLD = 300000
SMALLTHRESHOLD = 10000
PIXELTHRESHOLD = 600

class PillSegmenter:
    def __init__(self):
        self.original_image = None
        self.bright_image = None
        self.save_folder ='images'
        self.thresh_thresh = 110
        self.circle_thresh = 10
        self.debug_mode = True

    def threshold_image(self, high=255):
        img = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY) # better in grayscale
        ret, thresh = cv2.threshold(img, self.thresh_thresh, high, 0)
        if self.debug_mode:
            cv2.imwrite(self.save_folder + '/thresh.jpg', thresh)
        return thresh

    def do_contours(self, thresh):
        contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
        contour_sorted = sorted(contours, key=cv2.contourArea, reverse=True)
        if self.debug_mode:
            new_img = self.original_image.copy()
            cv2.drawContours(new_img, contour_sorted, -1, (0, 255, 0))
            cv2.imwrite(self.save_folder+'/contours.jpg', new_img)
        return contour_sorted

    def find_circles(self, cs):
        contour_list = []
        for contour in cs:
            approx = cv2.approxPolyDP(contour,0.005*cv2.arcLength(contour,True),True)
            area = cv2.contourArea(contour)
            if ((len(approx) > self.circle_thresh) and
                (area > SMALLTHRESHOLD) and
                (area < LARGETHRESHOLD) and
                len(contour) > PIXELTHRESHOLD):
                contour_list.append(contour)

        if self.debug_mode:
            new_img2 = self.original_image.copy()
            cv2.drawContours(new_img2, contour_list, -1, (0, 255, 0))
            cv2.imwrite(self.save_folder+'/circle_contours.jpg', new_img2)

        circles_sorted = sorted(contour_list, key=cv2.contourArea)
        return circles_sorted

    def draw_n_contours(self, circles_sorted, index):
        new_img3 = self.original_image.copy()
        i = 0

        while i < len(circles_sorted) and cv2.contourArea(circles_sorted[index-i]) > FINALPILLSIZETHRESHOLD:
            x, y, w, h = self.get_bounding_rect(circles_sorted[index-i])
            cropped = self.original_image.copy()[y:y+h, x:x+w]
            lit_cropped = self.bright_image.copy()[y:y+h, x:x+w]


            print("Original image center: ", self.original_image.shape[0]/2, self.original_image.shape[1]/2)
            print("Pill center: ", x+w/2,y+h/2)

            distance_from_center = (y+h/2) - (self.original_image.shape[0]/2)
            print("DISTANCE: ", distance_from_center)

            if self.debug_mode:
                cv2.drawContours(new_img3, circles_sorted, index-i, (0, 255, 0))
                cv2.imwrite(self.save_folder+'/biggest_contour' + str(i) +'.jpg', new_img3)
                cv2.imwrite(self.save_folder+'/cropped_pill' + str(i) + '.jpg', cropped)
            self.crop_circle(cropped, i, lit_cropped, circles_sorted[index-i])
            i += 1

        return i, distance_from_center

    def get_bounding_rect(self, contour):
        x,y,w,h = cv2.boundingRect(contour)
        return x, y, w, h

    def crop_circle(self, img, i, lit_img, con):
        gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)

        circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,400,
            param1=51,param2=30,minRadius=0,maxRadius=0)
        mask = np.zeros(img.shape[:3], np.uint8)
        x = circles[0,0,0]
        y = circles[0,0,1]
        r = circles[0,0,2]

        cv2.circle(mask,(x,y),int(r),(255,255,255),-1)
        circo = cv2.circle(img.copy(), (x,y), int(r), (255,0,0), 3)
        cv2.imwrite(self.save_folder+'/circooo'+str(i)+'.jpg', circo)


        #if (x-r < 0 or y-r < 0 or x+r > img.shape[0] or y+r > img.shape[1]):
        print("circle is too big, using contour")
        mask2 = np.zeros(self.bright_image.shape[:3], np.uint8)
        cv2.drawContours(mask2, [con], 0, (255,255,255), -1)
        mask2 = cv2.bitwise_not(mask2)
        final1 = cv2.add(self.bright_image, mask2)
        xx,yy,ww,hh = self.get_bounding_rect(con)
        f2 = final1[yy:yy+hh, xx:xx+ww]
        cv2.imwrite(self.save_folder+'/lit_pill'+str(i)+'.jpg', f2)



        xs = int(max(math.ceil(x-r), 0))
        xe = int(max(math.ceil(x+r), img.shape[0]))
        ys = int(max(math.ceil(y-r), 0))
        ye = int(max(math.ceil(y+r), img.shape[1]))

        mask_inv = cv2.bitwise_not(mask)
        out = cv2.add(img, mask_inv)
        lit_out = cv2.add(lit_img, mask_inv)
        #f1 = out[ys:ye, xs:xe]
        f1 = lit_out[ys:ye, xs:xe]
        cv2.imwrite(self.save_folder+'/finalviacirclecrop'+str(i)+'.jpg', f1)


    def crop_qr(self, thresh, xl=300, xh=1500, yl=1200, yh=800):
        og_quart = self.original_image.copy()[1400:, 500:1500]
        ogg = cv2.cvtColor(og_quart, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((3,3), np.uint8)
        __, th = cv2.threshold(ogg, 80, 255, 0)
        cv2.imwrite(self.save_folder + '/qr_code_thresh.jpg', th)
        th = cv2.erode(th, kernel, iterations=5)

        contours = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]

        contour_sorted = sorted(contours, key=cv2.contourArea)
        index = -1

        while cv2.contourArea(contour_sorted[index]) > 10000:
            c = contour_sorted[index]
            #cv2.drawContours(og_quart, [c], 0, (0,0,255), 2)
            index -= 1

        #cv2.imwrite('images/qrconntours.jpg', og_quart)

        x,y,w,h=self.get_bounding_rect(c)
        qr_img = og_quart[y-30:y+h+30, x-30:x+w+30]
        cv2.imwrite(self.save_folder + '/qr_code_old.jpg', qr_img)
               
    def locate_pill_and_qr(self, firstiter):
        print("FINDING PILL", firstiter)
        morphed = self.perform_morphs()
        cv2.imwrite(self.save_folder + '/morphed.jpg', morphed)
        
        
        qr_con, pill_con = self.locate_qrp_contours(morphed, firstiter)
       
        px,py,pw,ph=pill_con
        if firstiter:
            try:
                qx,qy,qw,qh=qr_con
                qr = self.original_image[qy-40:qy+qh+40, qx-40:qx+qw+40]
                cv2.imwrite(self.save_folder + '/qr_code.jpg', qr)
            except:
                print("couldn't find QR code")
               
        return (px+pw/2, py+ph/2)
        #except:
        #    print("couldn't find them")
        #    return (None, None)
               
    def locate_qrp_contours(self, morphed, firstiter):
        contours = cv2.findContours(morphed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
        #print(len(contours))
        qr_con = 0


        for con in contours:
            approx = cv2.approxPolyDP(con,0.02*cv2.arcLength(con,True),True)
            area = cv2.contourArea(approx)
            rect = cv2.boundingRect(approx)
            x,y=rect[0],rect[1]
            w,h=rect[2],rect[3]
            #print(size)
            #print(len(approx), area)
            if len(approx == 4) and area < 100000 and area > 10000 and abs(w-h) < 100:
                qr_con = rect
            elif len(approx) > 5 and abs(w-h) < 150:
                pill_con = rect

        labelled = cv2.rectangle(self.original_image.copy(), pill_con, (0,255,0), 2)
        if firstiter:
            cv2.rectangle(labelled, qr_con, (0,255,0), 2)
        cv2.imwrite(self.save_folder + '/labelled.jpg', labelled)
        return qr_con, pill_con
               
    def perform_morphs(self):
        ker = np.ones((7,7))
        gray = cv2.cvtColor(self.original_image,cv2.COLOR_BGR2GRAY)
        smooth = cv2.blur(gray, (5, 5))
        __, th = cv2.threshold(smooth,110,255,1)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 40))
        final = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (120, 120))
        final = cv2.morphologyEx(final, cv2.MORPH_OPEN, kernel)
        final=cv2.erode(final,ker,iterations=10)
        final=cv2.dilate(final,ker,iterations=10)
        return final
            
    def segment_pills(self, debug_mode=True, firstiter=True):
        self.debug_mode=debug_mode
        print("Processing images")

        cv2.imwrite(self.save_folder+'/original_image.jpg', self.original_image)
        #		self.bright_image = self.original_image # DELETE THIS
        thresh = self.threshold_image()
        if firstiter:
            self.crop_qr(thresh)
        cs = self.do_contours(thresh)
        circles_sorted = self.find_circles(cs)
        index = len(circles_sorted) - 1
        num_pills, dfc = self.draw_n_contours(circles_sorted, index)		
        print("Found %i pill(s)" %num_pills)
        return num_pills, dfc










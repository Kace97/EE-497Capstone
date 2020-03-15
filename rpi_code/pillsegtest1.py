#!/usr/bin/env python
import cv2
import numpy as np
from picamera import PiCamera
from time import sleep


def take_picture():
    camera = PiCamera()
    camera.start_preview()
    sleep(1)
    camera.capture('rpi_photo.jpg')
    camera.stop_preview()


def threshold_image(img, low, high=255, result='images'):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # better in grayscale
    ret, thresh = cv2.threshold(img, low, high, 0)
    cv2.imwrite(result, thresh)
    #plt.imshow(thresh, cmap='gray')
    return thresh


def do_contours(thresh, original_img, save_folder):
    contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
    contour_sorted = sorted(contours, key=cv2.contourArea)
    new_img = original_img.copy()
    cv2.drawContours(new_img, contour_sorted, -1, (0, 255, 0))
    cv2.imwrite(save_folder+'/contours.png', new_img)
    return contour_sorted


def find_circles(cs, circle_thresh, original_img, save_folder):
    contour_list = []
    for contour in cs:
        approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        area = cv2.contourArea(contour)
        if ((len(approx) > circle_thresh) & (area > 30) & (area < 50000) ):
            contour_list.append(contour)

    new_img2 = original_img.copy()
    cv2.drawContours(new_img2, contour_list, -1, (0, 255, 0))
    cv2.imwrite(save_folder+'/circle_contours.png', new_img2)

    circles_sorted = sorted(contour_list, key=cv2.contourArea)
    return circles_sorted

def draw_n_contours(original_img, circles_sorted, index, save_folder, n):
    new_img3 = original_img.copy()

    for i in range(n):
        cv2.drawContours(new_img3, circles_sorted, index-i, (0, 255, 0))
        cv2.imwrite(save_folder+'/biggest_contour' + str(i) +'.png', new_img3)

        x, y, w, h = get_bounding_rect(circles_sorted[index-i])
        cropped = original_img.copy()[y:y+h, x:x+w]
        cv2.imwrite(save_folder+'/cropped_pill' + str(i) + '.png', cropped)

        crop_circle(cropped, save_folder, i)

def get_bounding_rect(contour):
    x,y,w,h = cv2.boundingRect(contour)
    return x, y, w, h


def crop_circle(img, save_folder, i):

    gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,60,
                            param1=80,param2=25,minRadius=0,maxRadius=0)
    mask = np.zeros(img.shape[:3], np.uint8)
    cv2.circle(mask,(circles[0,0,0],circles[0,0,1]),int(circles[0,0,2]),(255,255,255),-1)

    mask_inv = cv2.bitwise_not(mask)
    out = cv2.add(img, mask_inv)
    cv2.imwrite(save_folder+'/finalviacirclecrop'+str(i)+'.png', out)
    #plt.imshow(out)

def segment_pills(original_img, save_folder, thresh_thresh=170, circle_thresh=12, num_pills=1):
    cv2.imwrite(save_folder+'/original_image.png', original_img)
    thresh = threshold_image(original_img, thresh_thresh, result=save_folder+'/thresh.png') #170 for plight
    cs = do_contours(thresh, original_img, save_folder)
    circles_sorted = find_circles(cs, circle_thresh, original_img, save_folder)
    index = len(circles_sorted) - 1
    draw_n_contours(original_img, circles_sorted, index, save_folder, num_pills)
    #mask_background(original_img, save_folder, index, circles_sorted, num_pills)



take_picture()
plight = cv2.imread('rpi_photo.jpg')
#cv2.imwrite('new.png', plight)
segment_pills(plight, 'images', thresh_thresh=120, circle_thresh=8, num_pills=1)







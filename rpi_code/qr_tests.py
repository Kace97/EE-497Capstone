#!/usr/bin/env python
import cv2
from pyzbar import pyzbar
from pylibdmtx import pylibdmtx

image = cv2.imread('lit_photo.jpg')

barcodes = pyzbar.decode(image)
b2 = pylibdmtx.decode(image)

print("scan 1: ", barcodes)
print("scan 2: ", b2[0].data)

#!/usr/bin/env python
import cv2
from pyzbar import pyzbar
from pylibdmtx import pylibdmtx

image = cv2.imread('qr2.jpg')

barcodes = pyzbar.decode(image)
b2 = pylibdmtx.decode(image)
data = b2[0].data.decode("utf-8")

print("data ", data)
print("all ", b2[0])

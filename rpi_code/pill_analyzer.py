#!/usr/bin/env python
import cv2
import numpy as np
from time import sleep
from pylibdmtx import pylibdmtx


class PillAnalyzer:
    def __init__(self):
	    self.qr_image = None
		
    def decode_qr(self):
	    dec = pylibdmtx.decode(self.qr_image)
	    return dec

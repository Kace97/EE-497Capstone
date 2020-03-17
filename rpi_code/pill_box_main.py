#!/usr/bin/env python

import sys
import cv2
import pill_segmenter as ps
import pill_analyzer as pa


# SETUP
print("Setting up system")
seg = ps.PillSegmenter()
an = pa.PillAnalyzer()
time_to_pause = int(sys.argv[1])
seg.thresh_thresh = int(sys.argv[2]) #100-170
seg.circle_thresh = int(sys.argv[3]) #11

# SEGMENTATION
def segmentation():
	seg.original_image = cv2.imread('test_images/rpi_photo.jpg')
	seg.bright_image = cv2.imread('test_images/lit_photo.jpg')
	num_pills = seg.segment_pills(debug_mode=False)

# ANALYSIS
def analysis():
	print("Analyzing pill(s)")
	an.qr_image = cv2.imread('images/qr_code.jpg')
	print("QR code: %s" %an.decode_qr())
	for i in range(num_pills):
		enc = an.encode_pill('images/lit_pill' + str(i) + '.jpg')
		print("Encoding:", enc)

#while(True):
	
#check for signal
arduino_signal = True

#if arduino_signal:
#pd.take_pictures(time_to_pause)
segmentation()
analysis()
arduino_signal = False


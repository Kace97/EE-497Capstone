#!/usr/bin/env python

import sys
import cv2
import pill_segmenter as ps
import pill_analyzer as pa

time_to_pause = int(sys.argv[1])
#pd.take_pictures(time_to_pause)

seg = ps.PillSegmenter()
seg.thresh_thresh = int(sys.argv[2]) #100-170
seg.circle_thresh = int(sys.argv[3]) #11

seg.original_image = cv2.imread('rpi_photo.jpg')
seg.bright_image = cv2.imread('lit_photo.jpg')
seg.segment_pills()

print("Analyzing pill(s)")
an = pa.PillAnalyzer()
#an.qr_image = cv2.imread('images/qr_code.jpg')
an.qr_image = cv2.imread('qr2.jpg')
code = an.decode_qr()
print("QR code: %s" %code)

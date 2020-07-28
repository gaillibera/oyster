# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:16:24 2020

@author: renny
"""

# import the necessary packages
import numpy as np
#import argparse
import imutils
import cv2
image = cv2.imread('oysterRed.png')
#lower = np.array([0, 0, 0])
#upper = np.array([15, 15, 15])
lower = np.array([0, 0, 255])
upper = np.array([0, 0, 255])
shapeMask = cv2.inRange(image, lower, upper)
# find the contours in the mask
cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print("I found {} red shapes".format(len(cnts)))
cv2.imshow("Mask", shapeMask)
# loop over the contours
for c in cnts:
	# draw the contour and show it
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.imshow("Image", image)
cv2.waitKey(0)
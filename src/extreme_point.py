#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on : 30 Aug 2016

Description: extreme_points.py
             Detecting the extreme points in the contours
             to find the extreme north, south, east, and west
             coordinates from a raw contour
             Usage:
             python3 extreme_points.py --image ../images/india.jpeg

@ author    : sampathsingamsetty
"""
import imutils
import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

# load the image, blur the same
image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Blurred Image", image)
cv2.waitKey(0)

# threshold the image, segment the display region from rest
threshold = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
# remove any small regions of noise by performing a series of
# erosions and dilations
threshold = cv2.erode(threshold, None, iterations=2)
threshold = cv2.dilate(threshold, None, iterations=2)

# find the contours in the thresholded image and then grab
# the largest of the contour
cntrs = cv2.findContours(np.copy(threshold),
                         cv2.RETR_EXTERNAL,
                         cv2.CHAIN_APPROX_SIMPLE)
# sort the contours to find the largest one
cntrs = cntrs[0] if imutils.is_cv2() else cntrs[1]
c = max(cntrs, key=cv2.contourArea)

# find the extreme points along the contour
# smallest x-coordinate = west
extremeLeft = tuple(c[c[:, :, 0].argmin()][0])
# largest x-coordinate = east
extremeRight = tuple(c[c[:, :, 0].argmax()][0])
# smallest y-coordinate = north
extremeTop = tuple(c[c[:, :, 1].argmin()][0])
# largest y-coordinate = south
extremeBot = tuple(c[c[:, :, 1].argmax()][0])

# now draw the outline of the object and then draw each of the
# extreme points, where the left-most point is red, right-most
# point is green, top-most point is blue and the bottom-most
# point is teal in colors
cv2.drawContours(image, [c], -1, (0, 255, 255), 3)
cv2.circle(image, extremeLeft, 8, (0, 0, 255), -1)
cv2.circle(image, extremeRight, 8, (0, 255, 0), -1)
cv2.circle(image, extremeTop, 8, (255, 0, 0), -1)
cv2.circle(image, extremeBot, 8, (255, 255, 0), -1)

# display the image
cv2.imshow("Locations on Image", image)
cv2.waitKey(0)

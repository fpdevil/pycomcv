#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 04 Sep 2016

Description: image_thresholding.py
             Thresholding the images is used to focus on the objects
of interest in an image. A downside of then simple thresholding is
that the threshold value T has to be provided manually, which needs
a lot of trial and error. In order to overcome this, we can use the
Adaptive Threshold, which considers small neighbors of pixels and
then finds an optimal threshold T.

             Usage:
             python3 image_thresholding.py --image ../images/numbers.png

@ author   : sampathsingamsetty
"""

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

# Read the image
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", image)

# simple thresholding
# binary thresholding with threshold = 0 and maxVal = 255
(T, threshold) = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold 0, MaxVal 255", threshold)

# changing then threshold value to 127 would remove all the
# numbers less than or equal to 127
# threshold = 127 and maxVal = 255
(T, threshold) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold 127, MaxVal 255", threshold)

# changing maxValue to 128, sets the value of the thresholded regions to 128
(T, threshold) = cv2.threshold(image, 0, 128, cv2.THRESH_BINARY)
cv2.imshow("Threshold 0, MaxVal 128", threshold)

# Inverse Binary Thresholding
# This is the opposite of binary thresholding, with destination pixel 0
# if the correspomding source pixel is greater than the threshold and to
# maxVal if the source pixel is less than the threshold
(T, threshold) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Inverse Threshold 127, MaxVal 255", threshold)

# Truncate Thresholding
# In this the destination pixel is set to the threshold if the source
# pixel is greater than the threshold. Otherwise destination is set to
# source pixel with maxVal ignored.
(T, threshold) = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow("Truncate Threshold 127, MaxVal 255", threshold)

# Threshold to Zero
# In this the destination pixel is set to the correspomding source
# pixel if the source pixel is greater than the threshold. Otherwise
# destination is set to 0, with maxVal ignored.
(T, threshold) = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow("Zero Threshold 127, MaxVal 255", threshold)

# Inverted Threshold to Zero
# In this then destination pixel is set to 0 if the source pixel
# is greater than the threshold. Otherwise destination is set to
# the source pixel with maxVal ignored.
(T, threshold) = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("Inverted Threshold to Zero 127, MaxVal 255", threshold)

cv2.waitKey(0)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 30 Aug 2016

Description: arithmetic.py
             Performing arithmetic operations on the pixel values of images
             Usage:
             python3 arithmetic.py --image ../images/goofy.png

@ author   : sampathsingamsetty
"""
from __future__ import print_function
import numpy as np
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))
print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

print("Image shape: {}".format(image.shape))
Mat = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, Mat)
cv2.imshow("CV2 Added", added)

Mat = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, Mat)
cv2.imshow("CV2 Subtracted", subtracted)
cv2.waitKey(0)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 30 Aug 2016

Description: rotate.py
             Rotating the image by a certain angle
             Usage:
             python3 rotate.py --image ../images/goofy.png

@ author   : sampathsingamsetty
"""
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

Mat = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, Mat, (w, h))
cv2.imshow("Rotated by 45 deg", rotated)

Mat = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, Mat, (w, h))

# using the imutils
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 deg", rotated)
cv2.waitKey(0)

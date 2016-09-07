#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on : 30 Aug 2016

Description: Access and manipulate the pixels of an image
             Usage:
             python3 get_and_set.py --image ../images/goofy.png

@ author   : sampathsingamsetty
"""

from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

# opencv stores R G B in reverse order as b g r
(b, g, r) = image[0, 0]
print("Pixels at (0, 0) - RED: {}, GREEN: {}, BLUE: {}".format(r, g, b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixels at (0, 0) - RED: {}, GREEN: {}, BLUE: {}".format(r, g, b))

# slicing using numppy
corner = image[0:100, 0:100]
cv2.imshow("Image Corner", corner)

image[0:100, 0:100] = (0, 255, 0)

cv2.imshow("Image Updated", image)
cv2.waitKey(0)

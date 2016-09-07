#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 01 Sep 2016

Description: split_and_merge.py
             Split the individual RGB channels of an image and merge
             Usage:
             python3 split_and_merge.py --image ../images/beach.png

@ author   : sampathsingamsetty
"""

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# split the image
(B, G, R) = cv2.split(image)
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

# merging the channels
merged = cv2.merge([B, G, R])
cv2.imshow("Merged Image", merged)
cv2.waitKey(0)

# another approach
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Numpy Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Numpy Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Numpy Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)

cv2.destroyAllWindows()

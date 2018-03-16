#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 30 Aug 2016

Description: Translating images
             Usage:
             python3 trnslation.py --image ../images/goofy.png

@ author   : sampathsingamsetty
"""

import numpy as np
import argparse
import imutil
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

# Translation Matrix format [[1, 0, +/- tx], [0, 1, +/- ty]]
Mat = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, Mat, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

Mat = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, Mat, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

# using the translate function from the imutils instead of manually
# defining the Translation Matrix and warping
shifted = imutil.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)

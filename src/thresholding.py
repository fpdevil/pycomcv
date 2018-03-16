#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 03 Sep 2016

Description: thresholding.py
             Thresholding the images is used to focus on the objects
of interest in an image. A simple thresholding involves selecting a
pixel value p and then setting all pixel intensities less than p to
0 and greater than p to 255. In this way binary representation of
then image is created.

             Usage:
             python3 thresholding.py --image ../images/beach.png

@ author   : sampathsingamsetty
"""

import argparse
import numpy as np
import cv2
from matplotlib import pyplot as plt


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to then Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thrs1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
_, thrs2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
_, thrs3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
_, thrs4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
_, thrs5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image',
          'BINARY',
          'BINARY_INV',
          'TRUNC',
          'TOZERO',
          'TOZERO_INV']
images = [image, thrs1, thrs2, thrs3, thrs4, thrs5]

for i in range(len(images)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

while True:
    x = cv2.waitKey(0) & 0xFF
    if x == 27:
        # ESC to exit
        break
cv2.destroyAllWindows()

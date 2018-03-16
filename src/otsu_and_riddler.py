#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 03 Sep 2016

Description: otsu_and_riddler.py


             Usage:
             python3 otsu_and_riddler.py --image ../images/coins.jpg

@ author   : sampathsingamsetty
"""

from __future__ import print_function
import numpy as np
import argparse
import mahotas
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Gaussian Blur Image", blurred)

T = mahotas.thresholding.otsu(blurred)
print("Otsu's Threshold: {}".format(T))

threshold = image.copy()
threshold[threshold > T] = 255
threshold[threshold < 255] = 0
threshold = cv2.bitwise_not(blurred)
cv2.imshow("Otsu", threshold)

T = mahotas.thresholding.rc(blurred)
print("Riddler Calvard: {}".format(T))

threshold = image.copy()
threshold[threshold > T] = 255
threshold[threshold < 255] = 0
threshold = cv2.bitwise_not(threshold)
cv2.imshow("Riddler Calvard", threshold)
cv2.waitKey(0)

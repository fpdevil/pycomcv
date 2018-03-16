#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 03 Sep 2016

Description: count_coins.py
Using contors and canny edge detection to count the number of
coins in an image.

             Usage:
             python3 count_coins.py --image ../images/uscoins.jpeg

@ author   : sampathsingamsetty
"""

from __future__ import print_function
import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Gaussian Blur", blurred)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Canny Edged", edged)

# cv2.findContours returns a tuple consisting of the below 3 values
# 1. Modified destructed image after applying contour detection algorithm
# 2. Countours themselves
# 3. Contour Hierarchy
# Its important to note that the function is destructive to the image passed
# If its intended to use the image later on in the code its better to use a
# copy of the image using numpy(s) copy method
#
# make a copy of themselves image
edged_copy = np.copy(edged)
(_, ctrs, _) = cv2.findContours(edged_copy,
                                cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
print("Number of coins in the image: {}".format(len(ctrs)))

coins_copy = np.copy(image)
cv2.drawContours(coins_copy, ctrs, -1, (255, 0, 0), 3)
# for c in ctrs:
#     cv2.drawContours(coins_copy, [c], 0, (0, 255, 0), 3)

cv2.imshow("Detecting Coins in the Image", coins_copy)
cv2.waitKey(0)

# crop each individual coins from image
for (i, c) in enumerate(ctrs):
    (x, y, w, h) = cv2.boundingRect(c)
    print("Coins #{}".format(i + 1))
    coin = image[y: y + h, x: x + w]
    cv2.imshow("Coin", coin)
    mask = np.zeros(np.shape(image)[: 2], dtype="uint8")
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)),
               int(radius), (0, 255, 0), -1)
    mask = mask[y: y + h, x: x + w]
    cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask=mask))
    cv2.waitKey(0)

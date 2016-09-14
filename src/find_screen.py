#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on : 30 Aug 2016

Description: find_screen.py
             Detect the screen of a gameboy device
             Usage:
             python3 find_screen.py --image ../images/gameboy0.jpeg

@ author   : sampathsingamsetty
"""

import imutil
import numpy as np
import argparse
import cv2

# parse the user supplied arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

# load the image, compute the ratio of the old height
# to the new height, clone and resize the same.
image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# keep aspect ration, which is the proportional relationship
# of the width to the height of the image. Here we are resizing
# image to have 300 pixel height
ratio = image.shape[0] / 300.0
original = np.copy(image)
image = imutil.resize(image, height=300)

# convert image to grey scale and blur it
# then find the edges in the image. bilateralFilter function
# has the advantage of removing the noise in the image while
# still preserving the actual edges.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)

# Find contours in the edged image and keep only the largest
# ones. Finally initialize our screen contour
(_, cntrs, _) = cv2.findContours(np.copy(edged),
                                 cv2.RETR_TREE,
                                 cv2.CHAIN_APPROX_SIMPLE)
cntrs = sorted(cntrs, key=cv2.contourArea, reverse=True)[:10]
screenCntr = None

# find which contour is the gameboy screen
# loop through the contours
for c in cntrs:
    # approximate the polygonal curves of a contour
    perimeter = cv2.arcLength(c, True)
    epsilon = 0.02 * perimeter  # 2% of the arclength
    approx = cv2.approxPolyDP(c, epsilon, True)

    # if the approximate contour has 4 points then
    # it can be assumed that the screen is found
    if len(approx) == 4:
        screenCntr = approx
        break

cv2.drawContours(image, [screenCntr], -1, (0, 255, 0), 4)
cv2.imshow("Game Boy Screen", image)
cv2.waitKey(0)

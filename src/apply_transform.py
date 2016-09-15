#!/usr/bin/env python
# coding: utf-8

"""
Created on : 30 Aug 2016

Description: apply_transform.py
             Apply Perspective transformation on images

             Usage:

             Example1
             python3 apply_transform.py --image ../images/card.jpg
                     --coords "[(434, 90), (793, 106),(614, 608), (150, 480)]"

             Example2
             python3 apply_transform.py --image ../images/paper.jpg
                     --coords "[(152,394),(477,222),(562,330),(205,508)]"

@ author   : sampathsingamsetty
"""

from transform import fourpoint_transform
import numpy as np
import argparse
import cv2

# argument parsing for the input args
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="Path to them Image")
ap.add_argument("-c", "--coords", help="comma delimited list of source points")
args = vars(ap.parse_args())

# load the image and capture the list of (x, y) points
image = cv2.imread(args["image"])
# supplied coordinates
points = np.array(eval(args["coords"]), dtype='float32')

# now apply the 4 point transform to get the "birds eye view"
# of the supplied image
warped = fourpoint_transform(image, points)

# display the original and warped image
cv2.imshow("Original Image", image)
cv2.imshow("Warped Image", warped)
cv2.waitKey(0)

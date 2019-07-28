#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright © 2018 Sampath Singamsetty
#
# File        : number_threshold.py
# Author      : Sampath Singamsetty <Singamsetty.Sampath@gmail.com>
# Time-stamp  : Sun Mar 18 12:04:28 IST 2018
# Description : python3 src/number_threshold.py \
#                       --image images/numbers_threshold.png
#
##############################################################################
import argparse

import cv2

# command line argument handling
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to the image for applying threshold")
ap.add_argument("-t", "--threshold", type=int,
                default=0, help="Threshold value")
args = vars(ap.parse_args())


# load the image and convert to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold types
# 1. Binary Threshold - Most common and simplest type
# if src > threshold
#    dst = maxVal
# else dst = 0
#
# 2. Inverse Threshold - Opposite of the Binary Threshold
# if src > threshold
#    dst = 0
# else dst = maxVal
#
# 3. Truncate Threshold
# if src > threshold
#    dst = threshold
# else dst = src
#
# 4. Threshold To Zero
# if src > threshold
#    dst = src
# else dst = 0
#
# 5. Inverted Threshold
# if src > threshold
#    dst = 0
# else dst = src

# create a list of all the threshold types supported by OpenCV
threshold_types = [
    ("THRESHOLD_BINARY", cv2.THRESH_BINARY),
    ("THRESHOLD_BINARY_INV", cv2.THRESH_BINARY_INV),
    ("THRESHOLD_TRUCATE", cv2.THRESH_TRUNC),
    ("THRESHOLD_TOZERO", cv2.THRESH_TOZERO),
    ("THRESHOLD_TOZERO_INV", cv2.THRESH_TOZERO_INV)
]

# loop over the list of threshold types
for (threshName, threshType) in threshold_types:
    # apply threshold and display the same
    (T, thresh) = cv2.threshold(gray, args["threshold"], 255, threshType)
    cv2.imshow(threshName, thresh)
    cv2.waitKey(0)

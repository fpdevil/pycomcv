#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 30 Aug 2016

Description: crop.py
             Cropping an image
             Usage:
             python3 crop.py --image ../images/goofy.png

@ author   : sampathsingamsetty
"""
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

cropped = image[30: 120, 240: 335]
cv2.imshow("Cropped Face", cropped)
cv2.waitKey(0)

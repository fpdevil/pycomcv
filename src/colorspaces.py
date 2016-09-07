#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 01 Sep 2016

Description: split_and_merge.py
             Converting and Playing with individual color spaces of an image
             Usage:
             python3 colorspaces.py --image ../images/beach.png

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

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L * a * b", lab)
cv2.waitKey(0)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 03 Sep 2016

Description: simple_thresholding.py
             Thresholding the images is used to focus on the objects
of interest in an image. A simple thresholding involves selecting a
pixel value p and then setting all pixel intensities less than p to
0 and greater than p to 255. In this way binary representation of
then image is created.

             Usage:
             python3 simple_thresholding.py --image ../images/coins.jpeg

@ author   : sampathsingamsetty
"""
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# applying gaussian blurring
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred Image", image)

(T, threshold) = cv2.threshold(blurred, 185, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", threshold)

(T, thresholdINV) = cv2.threshold(blurred, 185, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", thresholdINV)
cv2.imshow("Coins", cv2.bitwise_and(image, image, mask=thresholdINV))
cv2.waitKey(0)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 03 Sep 2016

Description: adaptive_thresholding.py
             Thresholding the images is used to focus on the objects
of interest in an image. A  downside  of the  simple thresholding is
that the threshold value T has to be provided manually, which needs
a lot of trial and error. In order to overcome this, we can use the
Adaptive Threshold, which considers small neighbors of pixels and
then finds an optimal threshold value T.

             Usage:
             python3 adaptive_thresholding.py --image ../images/coins.jpeg

@ author   : sampathsingamsetty
"""
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)

threshold = cv2.adaptiveThreshold(blurred,
                                  255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY_INV,
                                  11,
                                  4)
cv2.imshow("Mean Threshold", threshold)

threshold = cv2.adaptiveThreshold(blurred,
                                  255,
                                  cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY_INV,
                                  15,
                                  3)
cv2.imshow("Gaussian Threshold", threshold)

cv2.waitKey(0)

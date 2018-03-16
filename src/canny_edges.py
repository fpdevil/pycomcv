#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 03 Sep 2016

Description: canny_edges.py
The earlier gradient detection using the sobel_and_laplacian.py
left noisy edges which can be remedied using canny detection.

             Usage:
             python3 canny_edges.py --image ../images/coins.jpg

@ author   : sampathsingamsetty
"""
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Noise reduction
# Since edge detection is susceptible to noise in the image,
# first step is to remove the noise in the image with a 5x5 Gaussian filter
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Gaussian Blurred Image", image)

canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny Image", canny)
cv2.waitKey(0)

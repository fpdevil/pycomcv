#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 03 Sep 2016

Description: sobel_and_laplacian.py
This involves then gradient and edge detection. Formally edge detection
involves mathematical methods for finding the points in an image where
the brightness of the pixel intensities change distinctly

             Usage:
             python3 sobel_and_laplacian.py --image ../images/train.jpeg

@ author   : sampathsingamsetty
"""
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original GrayScale Image", image)

lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

cv2.imshow("Laplacian Image", lap)
cv2.waitKey(0)

# computing the sobel gradient
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 03 Sep 2016

Description: blurring.py
             Blurring the images

             Usage:
             python3 blurring.py --image ../images/sample1.jpg

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

# blurring using averaging
# A sliding matrix of size (n X n)  is defined, where n is an odd number
# for prividing a  true center to the matrix. This  matrix is moved from
# left to right and top to bottom. The pixel at the center is set to the
# average of  all the surrounding  pixels. The sliding matrix  is called
# the "Convolution Kernel" or just a "Kernel". As the size of the Kernel
# increases, the image will become more blurred.

blurred = np.hstack([cv2.blur(image, (3, 3)),
                     cv2.blur(image, (5, 5)),
                     cv2.blur(image, (7, 7))])
cv2.imshow("Average Blurred", blurred)
cv2.waitKey(0)

# guassian blurring
# In Guassian blurring instead of the simple mean a weighted mean, where
# neighborhood pixels  that are closer  to the central  pixel contribute
# more weight to the average
blurred = np.hstack([cv2.GaussianBlur(image, (3, 3), 0),
                     cv2.GaussianBlur(image, (5, 5), 0),
                     cv2.GaussianBlur(image, (7, 7), 0)])
cv2.imshow("Gaussian Blurred", blurred)
cv2.waitKey(0)

# median blurring
# Median blurring  is more  effective in removing  salt-and-pepper noise
# from the image. While applying the  median blur, the kernel size k has
# to be  defined first.  Then similar  to the  average blurring  all the
# pixels in neighborhood of the (k  X k) size is considered. But, unlike
# the averaging method  instead of replacing the central  pixel with the
# average of  the neighborhood, the  central pixel is replaced  with the
# median of the neighborhood.

blurred = np.hstack([cv2.medianBlur(image, 3),
                     cv2.medianBlur(image, 5),
                     cv2.medianBlur(image, 7)])
cv2.imshow("Median Blurred", blurred)
cv2.waitKey(0)

# bilateral blurring
# Images  with the  previous  blurring method  even  though reduced  the
# noise, lost the edges. In order  to reduce noise still maintaining the
# edges, Bilateral blurring can be used.

blurred = np.hstack([cv2.bilateralFilter(image, 5, 21, 21),
                     cv2.bilateralFilter(image, 7, 31, 31),
                     cv2.bilateralFilter(image, 9, 41, 41)])
cv2.imshow("Bilateral Blurred", blurred)
cv2.waitKey(0)

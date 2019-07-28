#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 30 Aug 2016

Description: rotate.py
             Resizing the image by a certain factor
             Usage:
             python3 resize.py --image ../images/goofy.png

@ author   : sampathsingamsetty
"""

import argparse
import imutil
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

# When resizing an  image, we need to  keep in mind the  aspect ratio of
# the image. The aspect ratio is  the proportional relationship of the
# width and the height of the image.  If we aren’t mindful of the aspect
# ratio, our resizing will return results that don’t look correct.
aspectR = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * aspectR))

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)

# resizing the image by specifying the height
aspectR = 50.0 / image.shape[0]
dim = (int(image.shape[1] * aspectR), 50)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)

# using resize function from imutils
resized = imutil.resize(image, width=100)
cv2.imshow("Resized via function", resized)

# now construct the list of interpolation methods
methods = []
methods.append(('cv2.INTER_NEAREST', cv2.INTER_NEAREST))
methods.append(('cv2.INTER_LINEAR', cv2.INTER_LINEAR))
methods.append(('cv2.INTER_AREA', cv2.INTER_AREA))
methods.append(('cv2.INTER_CUBIC', cv2.INTER_CUBIC))
methods.append(('cv2.INTER_LANCZOS4', cv2.INTER_LANCZOS4))

# test resizing by doubling the image size
(h, w) = image.shape[: 2]
for (name, method) in methods:
    print('using {} method for resizing'.format(name))
    resized = imutil.resize(image, width=w * 2, interp=method)
    cv2.imshow('Method: {}'.format(name), resized)
    cv2.waitKey(0)

cv2.waitKey(0)

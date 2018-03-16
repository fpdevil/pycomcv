#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : Sep 02, 2016

Descrption : equalize.py

Histogram equalization  improves the contrast  of an image by  “stretching” the
distribution of pixels. Consider a his- togram  with a large peak at the center
of it. Applying his- togram equalization  will stretch the peak out towards the
corner of the image, thus improving the global contrast of the image. Histogram
equalization is applied to grayscale images.

Usage     : python3 equalize.py --image ../images/train.jpeg

"""
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(image)

cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
cv2.waitKey(0)
cv2.destroyAllWindows()

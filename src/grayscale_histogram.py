#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 01 Sep 2016

Description: grayscale_histogram.py
A histogram represents the  distribution of pixel intensities (whether
color or gray- scale) in an image. It can be visualized as a graph (or
plot) that gives a high-level intuition of the intensity (pixel value)
distribution.  Here an  RGB color  space  is assumed,  so these  pixel
values will be in the range of 0 to 255

             Usage:
             python3 grayscale_histogram.py --image ../images/beach.png

@ author   : sampathsingamsetty
"""
from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to these Image")
args = vars(ap.parse_args())

# using these matplotlib to plot the histograms
image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", image)
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

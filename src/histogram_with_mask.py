#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 03 Sep 2016

Description: histogram_with_mask.py
             Masks can be used to focus on these regions of interest
within the images. We can construct a mask and compute the color
histograms for only the ROI's

             Usage:
             python3 histogram_with_mask.py --image ../images/sample1.jpg

@ author   : sampathsingamsetty
"""

from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2


def plot_histogram(image, title, mask=None):
    chnls = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    for (chnl, clr) in zip(chnls, colors):
        hist = cv2.calcHist([chnl], [0], mask, [256], [0, 256])
        plt.plot(hist, color=clr)
        plt.xlim([0, 256])

plt.show()


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
plot_histogram(image, "Histogram for the Original Image")

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Applying the Mask", masked)

cv2.waitKey(0)

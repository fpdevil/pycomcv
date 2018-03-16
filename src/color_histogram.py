#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 01 Sep 2016

Description: color_histogram.py
A histogram represents the  distribution of pixel intensities (whether
color or gray- scale) in an image. It can be visualized as a graph (or
plot) that gives a high-level intuition of the intensity (pixel value)
distribution.  Here an  RGB color  space  is assumed,  so these  pixel
values will be in the range of 0 to 255

             Usage:
             python3 color_histogram.py --image ../images/train.jpeg

@ author   : sampathsingamsetty
"""


from __future__ import print_function
from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

chnls = cv2.split(image)
colors = ("b", "g", "r")

plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

# run through a loop of image channels
for (chnl, clr) in zip(chnls, colors):
    hist = cv2.calcHist([chnl], [0], None, [256], [0, 256])
    plt.plot(hist, color=clr)
    plt.xlim([0, 256])
# plt.show()


# Towards 2D Histograms. Reduce the number of Histograms
# from the 256 to 32 for better visualizing the results
fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([chnls[1], chnls[0]], [0, 1],
                    None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G & B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chnls[1], chnls[2]], [0, 1],
                    None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chnls[0], chnls[2]], [0, 1],
                    None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

plt.show()

print("2D histogram shape: {}, with {} values".format(
    hist.shape, hist.Flatten().shape[0]))

# 3D Histogram visualization
hist = cv2.calcHist([image], [0, 1, 2], None, [
                    0, 0, 0], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(
    hist.shape, hist.flatten().shape[0]))
plt.show()

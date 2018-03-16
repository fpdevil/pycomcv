# -*- coding: utf-8 -*-
"""
Created on  : 28 Dec 2016

Description : Load, Display and Save an image
			  python3 load_display_save.py --image ../images/goofy.png

@author		: Sampath Singamsetty
"""

from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

cv2.imshow("Image", image)
cv2.waitKey(0)

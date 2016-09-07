# -*- coding: utf-8 -*-

"""
Created on : 30 Aug 2016

Description: Load, Display and Save an image
             Usage:
             python3 load_disp_save.py --image ../images/goofy.png

@ author   : sampathsingamsetty
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

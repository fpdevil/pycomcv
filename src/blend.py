#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 03 Sep 2016

Description: blend.py

Blending  of two  images  using  the weighted  sum  of  the two  array
representations  of  the images.  The  images  are  added as  per  the
equation,  𝚍𝚜𝚝(I)=(𝚜𝚛𝚌𝟷(I)∗𝚊𝚕𝚙𝚑𝚊+𝚜𝚛𝚌𝟸(I)∗𝚋𝚎𝚝𝚊+𝚐𝚊𝚖𝚖𝚊). Where  I is  the
multi-dimensional index of array elements.

             Usage:
             python3 blend.py --image1 ../images/doggies.jpeg --image2 ../images/puppies.jpeg

@ author   : sampathsingamsetty
"""

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i1", "--image1", required=True,
                help="Path to the first image")
ap.add_argument("-i2", "--image2", required=True,
                help="Path to the second image")
args = vars(ap.parse_args())

image1 = cv2.imread(args["image1"])
image2 = cv2.imread(args["image2"])

dst = cv2.addWeighted(image1, 0.7, image2, 0.3, 0)
cv2.imshow("Blended image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

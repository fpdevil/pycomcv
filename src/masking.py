#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 30 Aug 2016

Description: masking.py

      Performing  masking operations  on the  images. Masking  allows us  to
      concentrate only  on the portions of  the image that aren  of interest
      for us. For example, let’s say that we were building a computer vision
      system to  recognize faces.  The  only part of  the image which  is of
      interest  for us  is finding  and describing  the parts  of the  image
      containing faces – we simply don’t  care about the rest of the content
      of the image. Provided  that we could find the faces  in the image, we
      might construct a mask to show only the faces in the image.

             Usage:
             python3 masking.py --image ../images/goofy.png

@ author   : Sampath Singamsetty
"""
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

masking = np.zeros(image.shape[:2], dtype="uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(masking, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)
cv2.imshow("Masked Image", masking)

masked = cv2.bitwise_and(image, image, mask=masking)
cv2.imshow("Mask applied to image", masked)
cv2.waitKey(0)

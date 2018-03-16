#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on : 30 Aug 2016

Description: find_screen.py
             Detect the screen of a gameboy device
             Usage:
             python3 find_screen.py --image ../images/gameboy0.jpeg

@ author   : sampathsingamsetty
"""

import imutil
import numpy as np
import argparse
from skimage import exposure
import cv2

# parse the user supplied arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

# load the image, compute the ratio of the old height
# to the new height, clone and resize the same.
image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# keep aspect ration, which is the proportional relationship
# of the width to the height of the image. Here we are resizing
# image to have 300 pixel height
ratio = image.shape[0] / 300.0
original = np.copy(image)
image = imutil.resize(image, height=300)

# convert image to grey scale and blur it
# then find the edges in the image. bilateralFilter function
# has the advantage of removing the noise in the image while
# still preserving the actual edges.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)

# Find contours in the edged image and keep only the largest
# ones. Finally initialize our screen contour
(_, cntrs, _) = cv2.findContours(np.copy(edged),
                                 cv2.RETR_TREE,
                                 cv2.CHAIN_APPROX_SIMPLE)
cntrs = sorted(cntrs, key=cv2.contourArea, reverse=True)[:10]
screenCntr = None

# find which contour is the gameboy screen
# loop through the contours
for c in cntrs:
    # approximate the polygonal curves of a contour
    perimeter = cv2.arcLength(c, True)
    epsilon = 0.02 * perimeter  # 2% of the arclength
    approx = cv2.approxPolyDP(c, epsilon, True)

    # if the approximate contour has 4 points then
    # it can be assumed that the screen is found
    if len(approx) == 4:
        screenCntr = approx
        break

cv2.drawContours(image, [screenCntr], -1, (0, 255, 0), 4)
cv2.imshow("Game Boy Screen", image)
cv2.waitKey(0)

# once we have the screen contour, we need to determine
# the top left, top right, bottom right, bottom left points
# so that we can warp the image later. We will start with
# reshaping our contour to be the ultimate value and the
# initializing our output rectangle in the clockwise way.
points = screenCntr.reshape(4, 2)
rectangle = np.zeros((4, 2), dtype="float32")

# the top left point has the smallest sum and
# the bottom right point has the largest sum
s = points.sum(axis=1)
rectangle[0] = points[np.argmin(s)]
rectangle[2] = points[np.argmax(s)]

# compute the difference between the points, the top right points
# will have the minimum difference and the bottom left will have
# the maximum difference
diff = np.diff(points, axis=1)
rectangle[1] = points[np.argmin(diff)]
rectangle[3] = points[np.argmax(diff)]

# In oder to extract the original large Game Boy screen, we will
# multiply our rectangle by the ratio, thus transforming the
# points to the original image size.
rectangle *= ratio

# now calculate the size of the game boy screen so that we allocate
# memory to store it
(tl, tr, br, bl) = rectangle
widthX = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
widthY = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))

# height of the image
heightX = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
heightY = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))

# take the maximum of width and height values to reach
# the ulitmate values
maxWidth = max(int(widthX), int(widthY))
maxHeight = max(int(heightX), int(heightY))

# construct the destination points which will be used to
# map the screen to a top-down "birds eye" view
dst = np.array([[0, 0],
                [maxWidth - 1, 0],
                [maxWidth - 1, maxHeight - 1],
                [0, maxHeight - 1]],
               dtype="float32")

# calculate the perspective transform matrix and warp
# the perspective to grab the screen
Mat = cv2.getPerspectiveTransform(rectangle, dst)
warp = cv2.warpPerspective(original, Mat, (maxWidth, maxHeight))
# cv2.imshow("Warp", warp)
# cv2.waitKey(0)

# crop out the pokemon from the top right portion of screen
# convert the warped image to grayscale and then adjust the
# intensity of the pixels to have minimum and maximum values
# of 0 and 255, respectively
warp = cv2.cvtColor(warp, cv2.COLOR_BGR2GRAY)
warp_rescaled = exposure.rescale_intensity(warp, out_range=(0, 255))
# cv2.imshow("rescaled image", warp_rescaled)

# the pokemon we would like to identify is in the top right
# corner of the warped image, so lets crop it out
# 40% of width and 45% of height
(h, w) = np.shape(warp_rescaled)
(dX, dY) = (int(w * 0.4), int(h * 0.45))
crop = warp_rescaled[10: dY, w - dX: w - 10]

# save the cropped image to the file
cv2.imwrite("cropped-pokemon.png", crop)

# Now show our images
cv2.imshow("Warped Image", warp)
cv2.imshow("Rescaled Image", warp_rescaled)
cv2.imshow("Cropped Image", crop)
cv2.waitKey(0)

#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Created on : 30 Aug 2016

Description: cat_detector.py
             Detect the cat faces in an image
             Usage:
             python3 cat_detector.py --image ../images/cat.png

@ author   : sampathsingamsetty
"""

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
ap.add_argument(
    "-c",
    "--cascade",
    default="/opt/software/opencv/data/haarcascades/haarcascade_frontalcatface.xml",
    help="Path to the Cat detection haar cascade")
args = vars(ap.parse_args())

# load the input image and convert to grayscale
image = cv2.imread(args["image"])
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load cat detector cascade and detect the cat faces
detector = cv2.CascadeClassifier(args["cascade"])
rectangles = detector.detectMultiScale(grayscale,
                                       scaleFactor=1.309,
                                       minNeighbors=10,
                                       minSize=(75, 75))

print("Found {0} Cat faces!".format(len(rectangles)))

# loop over the detected cat faces and draw a rectangle
# surrounding each cat's face
for (i, (x, y, w, h)) in enumerate(rectangles):
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.putText(image,
                "Cat #{}".format(i + 1),
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (255, 0, 0),
                2)

# display the detected cat face
cv2.imshow("Detected Cat Faces", image)
cv2.waitKey(0)

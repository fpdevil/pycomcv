#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#
# File        : facial_landmark_detect.py
# Author      : Sampath Singamsetty <Singamsetty.Sampath@gmail.com>
# Time-stamp  : Fri Mar 16 19:18:36 IST 2018
# Description : Find frontal human faces in an image and identify the 68
#               landmarks on them.
# python3 src/facial_landmark_detect.py \
#        --shape_predictor lib/shape_predictor_68_face_landmarks.dat \
#        --image images/landmark_face.jpg
###############################################################################
# import all the necessary libraries
import argparse

import imutils
from imutils import face_utils

import cv2
import dlib

# handle the command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape_predictor", required=True,
                help="path to the facial landmark predictor")
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

# now initialize the dlib provided face detector and create the facial
# landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# load and resize the image (inc width to 500px) and convert to grayscale
image = cv2.imread(args["image"])
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Ask the detector to find the bounding boxes of each face. The 1 in the
# second argument indicates that we should upsample the image 1 time. This
# will make everything bigger and allow us to detect more faces.
dets = detector(gray, 1)

# loop over the face detectors
for (i, d) in enumerate(dets):
    # get the landmarks/parts for the face in box d
    shape = predictor(gray, d)
    # convert the landmarks detected into a numpy array
    shape = face_utils.shape_to_np(shape)
    print(shape)

    # convert the dlib's box to OpenCV style bounding box
    (x, y, w, h) = face_utils.rect_to_bb(d)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # label the found face
    cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    # loop through the (x, y) coordinates of the facial landmarks
    # and draw them on the image
    for (x, y) in shape:
        cv2.circle(image, (x, y), 1, (0, 255, 0), -1)

# Display the output image with all the facial landmarks
cv2.imshow("Output", image)
cv2.waitKey(0)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018
#
# Author       : Sampath Singamsetty
# Created Time : Fri Sep 28 21:36:43 2018
# File Name    : facial_landmarks.py
# Description  :
# Get the frontal human face in an  image and get the 68 landmarks from
# face  and  print  the  same  along with  circling the  nose  area. The
# pre-trained facial landmark  detector inside the dlib  library is used
# to estimate the  location of 68 (x, y)-coordinates that  map to facial
# structures on the face.
# @reference http://dlib.net/
########################################################################
import argparse

import cv2

import dlib

# take and handle the command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
ap.add_argument(
    "-p",
    "--shape_predictor",
    required=True,
    help="path to the 68 point landmark predictor")
args = vars(ap.parse_args())


def box(bb):
    """box: Take a bounding box from the dlib's predictor and convert the same
    into the four locational coordinates (x, y, w, h)
    :returns: locational coordinates

    """
    x = bb.left()
    y = bb.top()
    w = bb.right() - x
    h = bb.bottom() - y

    return (x, y, w, h)


# initialize  the  HOG based  face  detector  from  dlib  using the
# frontal  face detection api by providing the 68 point  data set as
# input and create the facial landmark predictor
print("[DEBUG] now loading the facial landmark detector/predictor")
# get the default face detector
detector = dlib.get_frontal_face_detector()
# identify the locations of important facial  landmarks such as the
# corners of the mouth and eyes, tip of the nose, and so forth from
# a human face image
predictor = dlib.shape_predictor(args["shape_predictor"])

# now, using the opencv api read the image and convert the same into
# the gray scale image
print("[INFO] converting the RGB image into grayscale")
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# using the detector find the bounding boxes of the face
# as per the dlib documentation...
# The 1 in the second argument indicates that we should upsample
# the image 1 time. This will make everything bigger and allow us
# to detect more faces.
boxes = detector(gray, 1)

for (a, b) in enumerate(boxes):
    print(
        "[DEBUG] detected face count: {}, left: {},top: {}, right: {}, bottom: {}".
        format(a+1, b.left(), b.top(), b.right(), b.bottom()))
    # get the landmarks for the face in the image
    shape = predictor(gray, b)
    print(
        "[DEBUG] getting the landmark coordinates, part 0: {}, part 1: {}...".
        format(shape.part(0), shape.part(1)))

    # convert the dlib's bounding box to an opencv styled box
    # draw a yellow colored box around each face found
    (x, y, w, h) = box(b)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)
    cv2.putText(image, "Face #{}".format(a + 1), (x - 15, y - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 165, 255), 2)

    # to point the nose, draw a cricle around the nose
    # the nose tip starts at 31 and extends till 36
    nose_x = shape.part(30).x
    nose_y = shape.part(30).y
    radius = int(abs(shape.part(36).x - shape.part(31).x) / 2)
    cv2.circle(image, (nose_x, nose_y), radius, (255, 0, 255), 6)
    # put a blue dot at point 30 on nose
    cv2.circle(image, (nose_x, nose_y), 2, (255, 0, 0), 6)
    # now counting from 0 through 68, print the landmark numbers
    for l in range(0, 68):
        x = shape.part(l).x
        y = shape.part(l).y
        cv2.putText(image, str(l), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.2,
                    (0, 255, 0), 1)

#  newImage = cv2.resize(image, (850, 650))
#  cv2.imshow("Final Image", newImage)
cv2.imshow("Final Image", image)
cv2.waitKey(0)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# File        : facial_landmark_regions.py
# Author      : Sampath Singamsetty <Singamsetty.Sampath@gmail.com>
# Time-stamp  : Sat Mar 17 02:22:30 IST 2018
# Description : Detect the facial regions under the 68 point facial
# landmark data points as described in the paper,
# https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/
#
# Following are the face regions which can be detected
# Mouth
# Right eyebrow
# Left eyebrow
# Right eye
# Left eye
# Nose
# Jaw
##############################################################################
# import the required packages
import numpy as np
import argparse
import cv2
import dlib
from imutils import face_utils
from collections import OrderedDict

# command line argument handling
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape_predictor", required=True,
                help="path to the 68 point facial landmark predictor")
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

# define a dictionary for mapping between the 68 point
# facial landmark indexes with the actual facial regions
facial_landmark_regions = {"mouth": (48, 68),
                           "right_eyebrow": (17, 22),
                           "left_eyebrow": (22, 27),
                           "right_eye": (36, 42),
                           "left_eye": (42, 48),
                           "nose": (27, 35),
                           "jaw": (0, 17)}
facial_regions_index = OrderedDict(
    sorted(facial_landmark_regions.items(), key=lambda t: t[1]))


def resize_image(image, height=None, width=None, interp=cv2.INTER_AREA):
    """Function to resize the image using the opencv interpolation

    :param image: input image
    :param height: height to change
    :param width: width to change
    :param interp: interpolation method
    :returns: resized image
    :rtype: object

    """
    image_dim = None
    (h, w) = image.shape[:2]

    if height is None and width is None:
        return image

    if height is None:
        ratio = width / float(h)
        image_dim = (width, int(h * ratio))

    else:
        ratio = height / float(h)
        image_dim = (int(w * ratio), height)

    resized_image = cv2.resize(image, image_dim, interpolation=interp)
    return resized_image


def render_facial_landmarks(image, shape, colors=None, alpha=0.75):
    """The function renders the actual landmark points obtained
    from the detector on the output image in different colors, so
    that we can visualize the facial regions.

    It uses the OpenCV image blending technique to blend 2 images
    together with cv2.addWeighted() function which applies the below
    function on the image.

    dst = alpha * img1 + beta * img2 + gamma
    where, alpha + beta =  1

    cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]]) → dst

    :param image: input image which needs facial region rendering
    :param shape: shape associated with the facial region landmark range
    :param colors: overlay color values to be set for rendering
    :param alpha: overlay transition coefficient (0 to 1)
    :returns: blended image
    :rtype: object

    """
    # make two copies of the image, one for overlay and another one for the
    # output image
    overlay_image = image.copy()
    output_image = image.copy()

    # check if the list of colors is provided, if not supply default values
    # for the same
    if colors is None:
        colors = [(79, 102, 255), (68, 71, 39),
                  (145, 176, 75), (133, 174, 178),
                  (83, 47, 240), (221, 130, 65),
                  (40, 99, 45)]

    # now loop over the facial landmark regions
    for (idx, name) in enumerate(facial_regions_index.keys()):
        print("{} - checking {}".format(idx, name))
        # take the (x, y) coordinates of each facial landmark
        (i, j) = facial_regions_index[name]
        points = shape[i: j]

        # first check if we are checking the jaw region as for the jaw region
        # we will just put an outline using convex hull mechanism
        if name == "jaw":
            for line in range(1, len(points)):
                pointX = tuple(points[line - 1])
                pointY = tuple(points[line])
                cv2.line(overlay_image, pointX, pointY, colors[idx], 2)

        # else calculate the convex hull on the facial landmark
        # coordinate points and render the same
        else:
            convex_hull = cv2.convexHull(points)
            cv2.drawContours(overlay_image, [convex_hull], -1, colors[idx], -1)

    # now apply transparent overlay
    cv2.addWeighted(overlay_image, alpha, output_image,
                    1 - alpha, 0, output_image)

    # return the updated output image
    return output_image


# now initialize the dlib provided face detector and create the facial
# landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# load and resize the image (inc width to 500px) and convert to grayscale
image = cv2.imread(args["image"])
image = resize_image(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

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

    # loop over all the facial parts individually using the indexes
    for (name, (j, k)) in facial_regions_index.items():
        # make a copy of the original image so that the features can be drawn
        # on it and then render the name of the particular facial region or
        # part on the image
        temp_image = image.copy()
        cv2.putText(temp_image, name, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        # now once the text is inserted, loop over the facial regions to draw
        # the discoverd facial part
        for (x, y) in shape[j: k]:
            cv2.circle(temp_image, (x, y), 1, (0, 255, 0), -11)

        # extract the image ROI of the facial region as an individual image
        # part
        (x, y, w, h) = cv2.boundingRect(np.array([shape[j: k]]))
        roi = image[y: y + h, x: x + w]
        roi = resize_image(roi, width=500, interp=cv2.INTER_CUBIC)

        # display the individual specific facial part
        cv2.imshow("ROI", roi)
        cv2.imshow("Image", temp_image)
        cv2.waitKey(0)

    # render all the facial landmarks with a transparent overlay
    output_image = render_facial_landmarks(image, shape)
    cv2.imshow("Image", output_image)
    cv2.waitKey(0)

#!/usr/bin/env python
# coding: utf-8

"""
Created on : 30 Aug 2016

Description: transform.py
             Perspective transformation on images
             Usage: import pycomcv.transform

@ author   : sampathsingamsetty
"""

import numpy as np
import cv2


def order_points(points):
    """Order the points of the rectangle.

    the function takes a single argument points which is a list of 4
    points depicting (x, y) coordinates of the rectangle.
    initialize a list of coordinates which would be ordered such that
    the first entry of the list is the top-left, second entry of list
    is top-right, third entry is the bottom-right and the fourth is
    the bottom-left
    """
    rectangle = np.zeros((4, 2), dtype='float32')

    # top-left point will have the smallest sum
    # bottom-right will have the largest sum
    s = points.sum(axis=1)
    rectangle[0] = points[np.argmin(s)]
    rectangle[2] = points[np.argmax(s)]

    # compute the difference between the points, with the top-right
    # point having smallest difference, and the bottom-left having
    # the largest difference
    diff = np.diff(points, axis=1)
    rectangle[1] = points[np.argmin(diff)]
    rectangle[3] = points[np.argmax(diff)]

    # return ordered coordinates
    return rectangle


def fourpoint_transform(image, points):
    """Consistent ordering of points.

    get a consistent ordering of the points and separate them
    it takes image to which perspective transform is needed and
    points which is a list of four points containing the ROI of
    the image to be transformed
    """
    rectangle = order_points(points)
    (tl, tr, br, bl) = rectangle

    # calculcation of the width of new image
    # this would be the maximum distance between bottom-right
    # and bottom-left x-coordinates or the top-right and the
    # top-left x-coordinates
    widthX = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthY = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthX), int(widthY))

    # calculcation of the height of new image
    # this would be them maximum distance between the top-right
    # and bottom-right y-coordinates or the top-left and the
    # bottom-left y-coordinates
    heightX = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - bl[1]) ** 2))
    heightY = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightX), int(heightY))

    # now with the dimensions of the new image calculcated, construct
    # a set of new destination points for getting a "birds eye view"
    # (top-down view) of the image, specifying points in the order of
    # top-left, top-right, bottom-right and bottom-left
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype='float32')

    # calculcate the perspective transform of the matrix and apply
    Mat = cv2.getPerspectiveTransform(rectangle, dst)
    warped = cv2.warpPerspective(image, Mat, (maxWidth, maxHeight))

    # return the warped image
    return warped

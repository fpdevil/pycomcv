#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 30 Aug 2016

Description: imutil.py
             Helper for the translation functions

@ author   : sampathsingamsetty
"""
import numpy as np
import cv2

# define a translate function


def translate(image, x, y):
    """Helper function for translating an image.

    horizontally and vertically based on x, y values
    """
    Mat = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, Mat, (image.shape[1], image.shape[0]))
    return shifted


def rotate(image, angle, center=None, scale=1.0):
    """Rotate an image by a certain angle.

    the defaults for rotation are via center and scale of 1.0
    """
    (h, w) = image.shape[:2]
    if center is None:
        center = (w / 2, h / 2)

    Mat = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, Mat, (w, h))
    return rotated


def resize(image, width=None, height=None, interp=cv2.INTER_AREA):
    """Resize an image based on the aspect ratio.

    the resize can be done by either height or width of the image
    """
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        aspectR = height / float(h)
        dim = (int(w * aspectR), height)
    else:
        aspectR = width / float(w)
        dim = (width, int(h * aspectR))

    resized = cv2.resize(image, dim, interpolation=interp)

    return resized

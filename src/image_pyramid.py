#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
Created on : 30 Aug 2016

Description: image_pyramid.py
             Create image pyramid for a supplied image.

An  Image pyramid  is a  multi-scale representation  of an  image.  It
allows  to  find  objects  in  an image  at  different  scales  of  an
image. Combined with the sliding window one can find objects in images
at various locations. At the bottom of the image pyramid, the original
image will  be there at original  size. At each subsequent  layer, the
image  is  resized  and  optionally  smoothed  via  Gaussian  blurring
method. Image  is progressively  subsampled until  a minimum  size has
been reached and no further subsampling is needed. These set of images
with different resolution are called Image Pyramids (because when they
are kept in a stack with biggest image at bottom and smallest image at
top look like a pyramid)

             Usage:
             python3 image_pyramid.py --image ../images/disney0.jpg

@ author   : sampathsingamsetty
"""

from skimage.transform import pyramid_gaussian
import imutils
import argparse
import cv2


def pyramid(image, scaleFactor=1.5, minSize=(30, 30)):
    """Helper function for creating an image pyramid.

    create an image pyramid based on the supplied values
    or defaults of scaleFactor and minimum size.
    """
    # first yield the original supplied image
    yield image

    # loop over the pyramid
    while True:
        # compute new dimensions for the supplied image
        # and resized the same
        w = int(image.shape[1] / scaleFactor)
        image = imutils.resize(image, width=w)

        # if the resized image does not fit the supplied default
        # values then stop further subsampling and pyramid build
        if (image.shape[0] < minSize[1] or image.shape[1] < minSize[0]):
            break

        # yield the next image from the pyramd
        yield image

# read the supplied arguments and parse them
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
ap.add_argument("-s", "--scale", type=float,
                default=1.5, help="size of the scale factor")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])

# Method 1 is purely opencv based with python
# just scaling, nothing smooth
# loop through the image pyramid
for (i, resized) in enumerate(pyramid(image, scaleFactor=args["scale"])):
    # display them resized image
    cv2.imshow("Layer {}".format(i + 1), resized)
    cv2.waitKey(0)

# close allows the windows
cv2.destroyAllWindows()

# Method is based in python with scikit-image
# http://scikit-image.org/docs/dev/api/skimage.transform.html#pyramid-gaussian
for (i, resized) in enumerate(pyramid_gaussian(image, downscale=2)):
    # if the resized image is too small, break the loop
    if resized.shape[0] < 30 or resized.shape[1] < 30:
        break

    # display the resized image
    cv2.imshow("Layer {}".format(i + 1), resized)
    cv2.waitKey(0)

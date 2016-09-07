# -*- coding: utf-8 -*-
"""
Created on : 19 July 2016

Description: kMeans clustering for color segmentation.
             Get the color palettes from an image using the
             k-means clustering algorithm provided by SciKit.
             Usage:
             python colors.py --image images/spidey.jpg --clusters 3

@ author   : sampathsingamsetty
"""

import argparse
import cv2
import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans

# input arggument parsing section
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-c", "--clusters", required=True,
                type=int, help="number of clusters")
args = vars(ap.parse_args())

# represent the image as multi dimensional numpy array. These arrays are in
# a BGR format and need to be converted to RGB format for further processing
# and rendering using the python's matplotlib library.
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# show the image
plt.figure()
plt.title(args["image"])
plt.axis("off")
plt.imshow(image)

# treating the datapoints as clusters we need to generate k-clusters
# from n data-points, for which the image needs to be reshaped to a
# list of pixels rather than the m X n pixels of image.
# numpy function reshape() gives a new shape to an array without
# changing its data
image = image.reshape((image.shape[0] * image.shape[1], 3))

# using kMeans clustering to find the most dominant colors of image
# clustering the pixel intensities
cluster = KMeans(n_clusters=args["clusters"])
cluster.fit(image)

# helper functions for displaying the clustered colors
# count the number of pixels beloging to each cluster


def centroid_histogram(cluster):
    """Function definition for centroid_histogram.

    This function takes the number of clusters as input
    and creates a histogram based on the number of pixels
    assigned to each individual cluster.
    """

    num_of_labels = np.arange(
        0, len(np.lib.arraysetops.unique(cluster.labels_)) + 1)
    (hist, bin_edges) = np.histogram(cluster.labels_, bins=num_of_labels)

    # normalize the histogram so that the sum can be one
    hist = hist.astype("float")
    hist /= hist.sum()
    # return the histogram
    return hist

# helper function for plotting the color paette


def plot_colors(hist, centroids):
    """Function definition for plot_colors.

    initialize the bar chart representing the relative frequency
    of each of the colors in the image
    creating a 400 X 75 rectangle to hold colors in image
    """
    bar = np.zeros((75, 400, 3), dtype="uint8")
    startx = 0
    # start looping over color and percentage distribution
    # of each cluster
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endx = startx + (percent * 400)
        # The function rectangle draws a rectangle outline or a filled
        # rectangle whose two opposite corners are the first 2 args.
        cv2.rectangle(bar, (int(startx), 0), (int(endx), 75),
                      color.astype("uint8").tolist(), -1)
        startx = endx

    # return the bar chart
    return bar

# build a histogram of clusters and then create a figure
# representing the number of pixels labelled to each color
hist = centroid_histogram(cluster)
bar = plot_colors(hist, cluster.cluster_centers_)

# show color bar
plt.figure()
plt.axis("auto")
plt.title(str(args["clusters"] + 1) + " colors")
plt.imshow(bar)
plt.show()

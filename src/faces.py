# -*- coding: utf-8 -*-
"""
Created on

Description: Detect faces in a photo
python3 faces.py --image images/sample.jpg
                 --cascade
                 /opt/software/opencv/data/haarcascades/haarcascade_frontalface_default.xml

fun: unable to decipher my oracular calligraphy :) , quite an oxymoron
@ author: sampathsingamsetty
"""

import argparse
import cv2

# Get user supplied values
# image_path = sys.argv[1]
# cascade_path = sys.argv[2]

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
ap.add_argument("-c", "--cascade", required=True, help="path to the cascade")
args = vars(ap.parse_args())

image_path = args["image"]
cascade_path = args["cascade"]

# Create the haar cascade
face_cascade = cv2.CascadeClassifier(cascade_path)

# Read the image
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray,
                                      scaleFactor=1.10,
                                      minNeighbors=5,
                                      minSize=(30, 30),
                                      flags=cv2.CASCADE_SCALE_IMAGE)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(10000)

cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)

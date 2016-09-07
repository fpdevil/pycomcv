#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on : 30 Aug 2016

Description: Drawing lines and squares
             Usage:
             python3 drawing.py

@ author   : sampathsingamsetty
"""

import numpy as np
import cv2

# define a canvas format drawing
canvas = np.zeros((300, 300, 3), dtype="uint8")

green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas Green", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas Red", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas Green Rectangle", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas Red Rectangle", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas Blue Rectangle", canvas)
cv2.waitKey(0)

# circles
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] / 2, canvas.shape[0] / 2)
white = (255, 255, 255)

for x in range(0, 175, 25):
    cv2.circle(canvas, (int(centerX), int(centerY)), x, white)

cv2.imshow("Canvas Concentric Circles", canvas)
cv2.waitKey(0)

# Abstract circle drawing
for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3, )).tolist()
    pt = np.random.randint(0, high=300, size=(2, ))
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas Abstract Circles", canvas)
cv2.waitKey(0)

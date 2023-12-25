#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2

# Read an image
image = cv2.imread('face.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a haar cascade classifier for detecting faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Define a scale factor for zooming
zoom_factor = 1.2

# Draw a rectangle around each face and zoom in
for (x, y, w, h) in faces:
    # Calculate new width and height based on zoom factor
    new_w = int(w * zoom_factor)
    new_h = int(h * zoom_factor)

    # Calculate new (x, y) to keep the center of the face the same
    new_x = int(x - (new_w - w) / 2)
    new_y = int(y - (new_h - h) / 2)

    # Draw a rectangle around the zoomed face
    cv2.rectangle(image, (new_x, new_y), (new_x + new_w, new_y + new_h), (0, 255, 0), 2)

# Display the image
cv2.imshow('Zoomed Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

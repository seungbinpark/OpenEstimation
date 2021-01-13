import numpy as np
import cv2

def onChange(value):
    global image, title, line1, line2

    line1, line2 = value, value


def onMouse(event, x, y, flags, param = onChange):
    global title, pt

    if event == cv2.EVENT_RBUTTONDOWN:
        pt = (x, y)
        cv2.rectangle(image, pt, (x + 30, y + 30), (255, 0, 0), line1)
        cv2.imshow(title, image)


    elif event == cv2.EVENT_LBUTTONDOWN:
        pt = (x, y)
        cv2.circle(image, pt, line2, (0, 0, 255), 2)
        cv2.imshow(title, image)

image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

pt = (-1, -1)
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.createTrackbar('Thickness', title, 1, 10, onChange)
cv2.createTrackbar('radius', title, 1, 50, onChange)
cv2.waitKey(0)
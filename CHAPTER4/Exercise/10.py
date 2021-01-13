import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global title, pt

    if event == cv2.EVENT_RBUTTONDOWN:
        pt = (x, y)
        cv2.rectangle(image, pt, (x + 30, y + 30), (255, 0, 0), 2)
        cv2.imshow(title, image)


    elif event == cv2.EVENT_LBUTTONDOWN:
        pt = (x, y)
        cv2.circle(image, pt, 20, (0, 0, 255), 2)
        cv2.imshow(title, image)

image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

pt = (-1, -1)
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
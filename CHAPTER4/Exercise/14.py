import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global title, pt

    if event == cv2.EVENT_MBUTTONDOWN:
        pt = (x, y)
        cv2.ellipse(image, pt, (120, 60), 0, 0, 360, (255, 0, 0), 1)
        cv2.imshow(title, image)


image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

pt = (-1, -1)
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
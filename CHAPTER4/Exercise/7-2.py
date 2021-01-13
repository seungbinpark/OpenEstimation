import numpy as np, cv2

def onMouse(event , x, y, flags, param):
    global title, pt
    pt = (150, 150)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, pt, 5, (100, 0, 0), 1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(image, pt, (150 + 30, pt + 30), (100, 0, 0))
        cv2.imshow(title, image)

image = np.ones((300, 300), np.uint8) * 255

title = "Draw Event"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
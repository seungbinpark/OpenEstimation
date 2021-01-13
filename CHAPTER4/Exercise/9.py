import numpy as np, cv2

image = np.zeros((600, 400, 3), np.uint8)
image[:] = (255, 255, 255)
pt = (100, 100)

cv2.rectangle(image, pt, (300, 400), (0, 0, 255), -1)

cv2.imshow("Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
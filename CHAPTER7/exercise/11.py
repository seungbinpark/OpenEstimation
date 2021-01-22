import numpy as np, cv2
from Common.filters import differential

image = cv2.imread("images/image.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [-1, 0, 0,
         0, 1, 0,
         0, 0, 0]
data2 = [0, 0, -1,
         0, 1, 0,
         0, 0, 0]
data3 = [-1, 0, 1,
         -1, 0, 1,
         -1, 0, 1]
data4 = [-1,-1,-1,
         0, 0, 0,
         1, 1, 1]

dst1, _, _ = differential(image, data1, data2)
dst2, _, _ = differential(image, data3, data4)
dst3 = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, 3)
dst4 = cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1, 3)
dst3 = cv2.convertScaleAbs(dst3)
dst4 = cv2.convertScaleAbs(dst4)

cv2.imshow("image", image)
cv2.imshow("roberts edge", dst1)
cv2.imshow("prewitt edge", dst2)
cv2.imshow("sobel- vertical_OpenCV", dst3)
cv2.imshow("sobel- horizontal_OpenCV", dst4)
cv2.waitKey(0)
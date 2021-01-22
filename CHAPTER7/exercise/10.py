import numpy as np, cv2
from Common.filters import filter

def filter2(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    ycenter, xcenter = rows//2, cols//2

    for i in range(ycenter, rows - ycenter):
        for j in range(xcenter, cols - xcenter):
            sum = 0.0
            for u in range(mask.shape[0]):
                for v in range(mask.shape[1]):
                    y, x = i + u - ycenter, j + v - xcenter
                    sum += image[y, x] * mask[u, v]
            dst[i, j] =sum
    return dst

image = cv2.imread("images/filter_blur.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data = [ 1/9, 1/9, 1/9,
         1/9, 1/9, 1/9,
         1/9, 1/9, 1/9]
mask = np.array(data, np.float32).reshape(3, 3)
blur1 = filter(image, mask)
blur2 = filter2(image, mask)
blur1 = blur1.astype('uint8')
blur2 = cv2.convertScaleAbs(blur2)

# 샤프닝 마스크 원소 지정
data1 = [ 0, -1, 0,
          -1, 5, -1,
          0, -1, 0]
data2 = [[-1, -1, -1],
         [-1, 9, -1],
         [-1, -1, -1]]
mask1 = np.array(data1, np.float32).reshape(3, 3)
mask2 = np.array(data2, np.float32)
sharpen1 = filter(image, mask1)
sharpen2 = filter(image, mask2)
sharpen1 = cv2.convertScaleAbs(sharpen1)
sharpen2 = cv2.convertScaleAbs(sharpen2)


cv2.imshow("image", image)
cv2.imshow("blur1", blur1)
cv2.imshow("blur2", blur2)
cv2.waitKey(0)

cv2.imshow("image", image)
cv2.imshow("sharpen1", sharpen1)
cv2.imshow("sharpen2", sharpen2)
cv2.waitKey(0)
import numpy as np, cv2

def contain(p, shape):
    return 0<=p[0] < shape[0] and 0<= p[1] < shape[1]

def translate(img, pt):
    dst = np.zeros(img.shape, img.dtype)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x, y = np.subtract((j, i), pt)
            if contain((y, x), img.shape):
                dst[i, j] = img[y, x]
    return dst

image = cv2.imread("images/translate.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

dst1 = translate(image, (50, 60))

pt1 = np.array([(0, 0), (0, image.shape[1]), (image.shape[0], 0)], np.float32)
pt2 = np.array([(50, 60), (50, 60 + image.shape[1]), (50 + image.shape[0], 60)], np.float32)
aff_mat = cv2.getAffineTransform(pt1, pt2)
dst2 = cv2.warpAffine(image, aff_mat, image.shape[:2])

cv2.imshow("image", image)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)

import numpy as np, cv2

image = cv2.imread("images/image.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

h, w = image.shape

flip1 = cv2.warpAffine()
flip2 = cv2.warpAffine()
flip3 = cv2.warpAffine()

'''flip1 = np.float32([[-1,0,563],[0,1,0]])
flip2 = np.float32([[1,0,1],[0,-1,447]])
flip3 = np.float32([[-1,0,563],[0,-1,447]])'''

'''flip1 = np.array([[-1, 0, 0],
                  [0, 1, 0]]).astype('float32')
flip2 = np.array([[1, 0, 0],
                  [0, -1, 0]]).astype('float32')
flip3 = np.array([[-1, 0, 0],
                  [0, -1, 0]]).astype('float32')'''

dst1 = cv2.warpAffine(image, flip1, (w,h))
dst2 = cv2.warpAffine(image, flip2, (w,h))
dst3 = cv2.warpAffine(image, flip3, (w,h))
cv2.imshow("image", image);     cv2.imshow("flip1", dst1)
cv2.imshow("flip2", dst2);      cv2.imshow("flip3", dst3)
cv2.waitKey()
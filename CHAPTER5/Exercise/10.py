import numpy as np, cv2

image = cv2.imread("images/sum_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류 발생")

mask = np.zeros((200, 100), np.uint8)
mask[200:400, 100:200] = 255                          #관심 영역에 값(255) 할당

'''
mean_value = cv2.mean(image, mask)

print("[mean_value] =", mean_value)
print()
'''

mean2, _ = cv2.meanStdDev(image, mask=mask)   #마스크가 255인 영역만 계산
print("[mean2] =", mean2.flatten())

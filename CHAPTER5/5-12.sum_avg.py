import numpy as np, cv2

image = cv2.imread("images/sum_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류 발생")

mask = np.zeros(image.shape[:2], np.uint8)
mask[60:160, 20:120] = 255                          #관심 영역에 값(255) 할당

sum_value = cv2.sumElems(image)                     #채널별 합 - 튜플로 반환
mean_value1 = cv2.mean(image)                       #채널별 평균 - 튜플로 반환
mean_value2 = cv2.mean(image, mask)

print("sum_value 자료형:", type(sum_value), type(sum_value[0]))
print("[sum_value] =", sum_value)
print("[mean_value1] =", mean_value1)
print("[mean_value2] =", mean_value2)
print()

##평균과 표준편차 결과 저장
mean, stddev = cv2.meanStdDev(image)                #2 원소 튜플로 변환
mean2, stddev2 = cv2.meanStdDev(image, mask=mask)   #마스크가 255인 영역만 계산
print("mean 자료형:", type(mean), type(mean[0][0]))  #반환 행렬 자료형, 원소 자료형
print("[mean] =", mean.flatten())                   #벡터 변환 후 출력
print("[stddev] =", stddev.flatten())
print()

print("[mean2] =", mean2.flatten())
print("[stddev2] =", stddev2.flatten())

cv2.imshow('image', image)
cv2.imshow('mask', mask)
cv2.waitKey(0)
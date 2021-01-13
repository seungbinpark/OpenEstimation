import numpy as np, cv2

image = np.zeros((400, 600, 3), np.uint8)                               # 400행, 600열 크기의 3채널 np.nint8형으로 행렬 생성
image[:] = (255, 255, 255)                                              # 행렬의 모든 화소 흰색으로 지정
pt1, pt2 = (50, 100), (200, 300)                                        # 좌표 선언 - 정수형 튜플

cv2.line(image, pt1, pt2, (0,255,0), 5)                                 # image 윈도우에 시작 좌표 pt1부터 종료 좌표 pt2까지 초록색 선을 두께 5로 그린다
cv2.rectangle(image, pt2, (300, 400), (0, 0, 255), -1, cv2.LINE_4, 1)   # 좌표 pt2, (300, 400)을 그대로 빨간색 사각형 그린다.

cv2.imshow("Line & Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
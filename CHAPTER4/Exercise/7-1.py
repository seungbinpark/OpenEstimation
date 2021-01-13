import numpy as np, cv2

image = np.zeros((300, 400, 3), np.uint8)
image[:] = (255, 255, 255)

pt1, pt2 = (50, 130), (200, 300)

cv2.line(image, pt1, (100, 200), (255, 0, 0))       # image 윈도우에 주어진 좌표에 따라 B(255)색의 선
cv2.line(image, pt2, (100, 100), (100))             # image 윈도우에 주어진 좌표에 따라 B(100)색의 선
cv2.rectangle(image, pt1, pt2, (255, 0, 255))       # image 윈도우에 주어진 좌표에 따라 B,R색의 사각형
cv2.rectangle(image, pt1, pt2, (0, 0, 255))         # image 윈도우에 주어진 좌표에 따라 R색의 사각형
# 사각형끼리 좌표가 곂쳐 빨간색으로 보임

title = "Line & Rectangle"
cv2.namedWindow(title)                              # title 이름 윈도우 생성, flag를 지정하지 않아 기본값인 'cv2.WINDOW_AUTOSIZE'로 지정
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
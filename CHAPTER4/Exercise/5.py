import numpy as np, cv2

image = np.zeros((300, 400), np.uint8)      # 자료형 8비트 부호없는 정수로 300행, 400열 크기의 행렬 생성
image[:] = 100                              # 회색 바탕 영상 생성

title = 'Window'                            # 윈도우 이름
cv2.namedWindow(title, cv2.WINDOW_NORMAL)   # 크기 변경 자유로운 윈도우 생성
cv2.moveWindow(title, 100, 200)             # x좌표 100, y좌표 200으로 이동
cv2.imshow(title, image)                    # title 변수 이름의 윈도우에 하나의 행렬(image)을 영상으로 표시
cv2.waitKey(0)                              # 키 입력 대기
cv2.destroyAllWindows()                     # 키가 입력된 후에 윈도우 닫기

import numpy as np, cv2

BGR_img = cv2.imread("images/color_model.jpg", cv2.IMREAD_COLOR)
if BGR_img is None: raise Exception("영상파일 읽기 오류")

white = np.array([255, 255, 255], np.uint8)
CMY_img = white - BGR_img
CMY = cv2.split(CMY_img)                                    # 채널 분리

black = cv2.min(CMY[0], cv2.min(CMY[1], CMY[2]))            # 원소 간의 최솟값 저장
Yellow, Magenta, Cyan = CMY - black                         # 2개 행렬 화소값 차분

titles = ['black', 'Yellow', 'Magenta', 'Cyan']
[cv2.imshow(t,eval()) for t in titles]                      # 리스트 생성 방식 활용
cv2.waitKey(0)
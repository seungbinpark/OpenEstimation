import cv2
from Common.utils import put_string

# 밝기 조절 콜백 함수
def brightness_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_BRIGHTNESS, value)       # 줌 설정

# 대비 조절 콜백 함수
def contrast_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_CONTRAST, value)

capture = cv2.VideoCapture(0)                   # 0번 카메라 연결
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)      # 카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)     # 카메라 프레임 높이
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)       # 프레임 밝기 초기화

title = "Change Camera Properties"
cv2.namedWindow(title)
cv2.createTrackbar('brightness', title, 0, 10, brightness_bar)
cv2.createTrackbar('contrast', title, 0, 40, contrast_bar)

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    brightness = int(capture.get(cv2.CAP_PROP_BRIGHTNESS))
    contrast = int(capture.get(cv2.CAP_PROP_CONTRAST))
    put_string(frame, 'brightness : ', (10, 240), brightness)
    put_string(frame, 'contrast : ', (10, 270), contrast)
    cv2.imshow(title, frame)

capture.release()
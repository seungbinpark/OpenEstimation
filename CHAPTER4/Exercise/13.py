import cv2

image = cv2.imread("images/read_color1.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 100)
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 9]

cv2.imwrite("images/test.jpg", image, params_jpg)  # 지정한 화질로 저장
cv2.imwrite("images/test.png", image, params_png)
print("저장 완료")
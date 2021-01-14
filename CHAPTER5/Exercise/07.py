import numpy as np, cv2

logo = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)
if logo is None: raise Exception("영상파일 읽기 오류")

blue, green, red = cv2.split(logo)

m_mask1 = np.zeros(logo.shape, np.uint8)

blue_img = cv2.add(m_mask1, blue)
green_img = cv2.add(m_mask1, green)
red_img = cv2.add(m_mask1, red)

cv2.imshow("logo", logo)
cv2.imshow("blue_img", blue_img)
cv2.imshow("green_img", green_img)
cv2.imshow("red_img", red_img)
cv2.waitKey()

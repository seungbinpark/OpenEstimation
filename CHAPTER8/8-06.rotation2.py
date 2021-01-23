import numpy as np, cv2
from Common.interpolation import rotate_pt

def calc_angle(pts):
    d1 = np.subtract(pts[1], pts[0])
    d2 = np.subtract(pts[2], pts[0])
    angle1 = cv2.fastAtan2(d1[1].float32, d1[0].float32)
    angle2 = cv2.fastAtan2(d2[1].float32, d2[0].float32)
    return (angle2 - angle1)

def draw_point(x, y):
    pts.append([x, y])
    print("좌표:", len(pts), [x,y])
    cv2.circle(tmp, (x,y), 2, 255, 2)
    cv2.imshow("image", tmp)

def onMouse(event, x, y, flags, param):
    global tmp, pts
    if(event == cv2.EVENT_LBUTTONUP and len(pts) == 0): draw_point(x, y)
    if(event == cv2.EVENT_LBUTTONDOWN and len(pts) == 1): draw_point(x, y)
    if(event == cv2.EVENT_LBUTTONUP and len(pts) == 2): draw_point(x, y)

    if len(pts) == 3:
        angle = calc_angle(pts)
        print("회전각: %3.2F" % angle)
        dst = rotate_pt(image, angle, pts[0])
        cv2.imshow("image", dst)
        tmp = np.copy(image)
        pts = []

image = cv2.imread("images/rotate.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")
tmp = np.copy(image)
pts = []

cv2.imshow("image", image)
cv2.setMouseCallback("image", onMouse, 0)
cv2.waitKey(0)
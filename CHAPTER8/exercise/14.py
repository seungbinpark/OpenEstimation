import numpy as np, cv2

def contain(p, shape):
    return 0<=p[0] < shape[0] and 0<= p[1] < shape[1]

def translate(img, pt):
    dst = np.zeros(img.shape, img.dtype)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x, y = np.subtract((j, i), pt)
            if contain((y, x), img.shape):
                dst[i, j] = img[y, x]
    return dst

def draw_point(x, y):
    pts.append([x, y])
    print("좌표:", len(pts), [x,y])
    cv2.circle(tmp, (x,y), 2, 255, 2)
    cv2.imshow("image", tmp)

def onMouse(event, x, y, flags, param):
    global tmp, pts
    if(event == cv2.EVENT_LBUTTONDOWN and len(pts) == 0): draw_point(x, y)
    if(event == cv2.EVENT_LBUTTONUP and len(pts) == 1): draw_point(x, y)

    if len(pts) == 2:
        print("기울기: %3.2F" % ((pts[1][1]-pts[0][1])/(pts[1][0]-pts[0][0])))
        pts=[]
        #cv2.line(image, pts[0], pts[1], 0, 3, cv2.LINE_A)

image = cv2.imread("images/image.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")
tmp = np.copy(image)
pts = []

dx, dy = pts[1][0]-pts[0][0], pts[1][1]-pts[0][1]

dst1 = translate(image, (dx, dy))

cv2.imshow("image", image)
cv2.imshow("dst1", dst1)
cv2.waitKey(0)
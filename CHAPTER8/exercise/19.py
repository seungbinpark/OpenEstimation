import numpy as np, cv2

def draw_bars(img, pt, w, bars):
    pt = np.array(pt, np.int)
    for bar in bars:
        (x,y), h = pt, w*6
        cv2.rectangle(img, (x,y,w,h), (0, 0, 0), -1)
        if bar == 0:
            y = 200
            h = 100
            cv2.rectangle(img,(x,y,w,h), (255, 255, 255), -1)
        pt += (int(w*1.5), 0)

img = np.full((400, 600, 3), (255, 255, 255), np.uint8)
c = 200
r, sr, c2, c4 = c//2, c//4, c*2, c*4
center = (300, 200)
center1 = (250, 200)
center2 = (350, 200)

B = (255, 0, 0)
R = (0, 0, 255)

cv2.ellipse(img, center, (100, 100), 0, 0, 180, B, -1)
cv2.ellipse(img, center, (100, 100), 180, 0, 180, R, -1)
cv2.ellipse(img, center1, (50, 50), 0, 0, 180, R, -1)
cv2.ellipse(img, center2, (50, 50), 180, 0, 180, B, -1)

left = (c2 -c * (18+8)/24, c2 - sr)
right = (c2 +c * (18+0)/24, c2 - sr)

draw_bars(img, left, c//12, (1,1,1))
draw_bars(img, right, c//12, (0,0,0))
angle = cv2.fastAtan2(2, 3)
img = cv2.warpAffine(img, cv2.getRotationMatrix2D((c2,c2), -angle*2, 1), (c4, c4))


title = "image"
cv2.imshow(title, img)
cv2.waitKey(0)
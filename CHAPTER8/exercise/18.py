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

image = np.full((400, 600, 3), (255, 255, 255), np.uint8)
center = (300, 200)
center1 = (250, 200)
center2 = (350, 200)

B = (255, 0, 0)
R = (0, 0, 255)

cv2.ellipse(image, center, (100, 100), 0, 0, 180, B, -1)
cv2.ellipse(image, center, (100, 100), 180, 0, 180, R, -1)
cv2.ellipse(image, center1, (50, 50), 0, 0, 180, R, -1)
cv2.ellipse(image, center2, (50, 50), 180, 0, 180, B, -1)

title = "image"
cv2.imshow(title, image)
cv2.waitKey(0)
import numpy as np, cv2

m = np.full((3, 6), 10, np.float64)

m1 = cv2.reduce(m, 0, 1)
m2 = cv2.reduce(m, 1, 1)

print("\n%s\n" %m1)
print("\n%s\n" %m2)
cv2.waitKey(0)
import numpy as np, cv2

m1 = [1, 2, 3, 1, 2, 3]
m2 = [3, 3, 4, 2, 2, 3]
m1 = np.array(m1, np.uint8)     # 1차원 리스트로 행렬 생성
m2 = np.array(m2, np.uint8)
m3 = cv2.add(m1, m2)            # 행렬 덧셈
m4 = cv2.subtract(m1, m2)       # 행렬 뺄셈

print("[m1] = %s" %m1)
print("[m2] = %s" %m2)
print("[m3] = %s" %m3)
print("[m4] = %s" %m4)
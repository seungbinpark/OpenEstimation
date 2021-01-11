import numpy as np, cv2

##ndarray 생성 예시
v1 = np.array([1, 2, 3], np.float32)      #1차원 리스트로 행렬 생성
v2 = np.array([[1], [2], [3]], np.float32)  #2차원 리스트(3행, 1열) - 열벡터
v3 = np.array([[1, 2, 3]], np.float32)    #2차원 리스트(1행, 3열) - 행벡터

##OpenCV 산술 연산 함수 - 입력 인수로 ndarray 객체만 가능함
v1_exp = cv2.exp(v1)
v2_exp = cv2.exp(v2)
v3_exp = cv2.exp(v3)
v1_log = cv2.log(v1)
v2_sqrt = cv2.sqrt(v2)
v3_pow = cv2.pow(v3, 3)

##행렬 정보 결과 출력
print("[v1] 형태: %s 원소: %s" % (v1.shape, v1))
print("[v2] 형태: %s 원소: \n%s" % (v2.shape, v2))
print("[v3] 형태: %s 원소: %s" % (v3.shape, v3))
print()

##행렬 정보 출력 - OpenCV 결과는 행렬로 반환됨
print("[v1_exp] 자료형: %s 형태: %s" % (type(v1_exp), v1_exp.shape))
print("[v2_exp] 자료형: %s 형태: %s" % (type(v2_exp), v2_exp.shape))
print("[v3_exp] 자료형: %s 형태: %s" % (type(v3_exp), v3_exp.shape))
print()

##열벡터를 1행에 출력하는 예시
print("[log] =", v1_log.T)
print("[sqrt] =", np.ravel(v2_sqrt))
print("[pow] =", v3_pow.flatten())
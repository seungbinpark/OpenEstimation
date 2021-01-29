import numpy as np, cv2
from Common.fft2d import fft2, ifft2, calc_spectrum, fftshift

def FFT(image, mode=2):
    if mode == 1: dft = fft2(image)
    elif mode==2: dft = np.fft.fft2(image)
    elif mode==3: dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft = fftshift(dft)
    spectrum = calc_spectrum(dft)
    return dft, spectrum

def IFFT(dft, shape, mode=2):
    dft = fftshift(dft).real
    if mode == 1: img = ifft2(dft).real
    if mode == 2: img = np.fft.ifft2(dft).real
    if mode == 3: img = cv2.idft(dft, flags=cv2.DFT_SCALE)[:,:,0]
    img = img[:shape[0], :shape[1]]
    return cv2.convertScaleAbs(img)

image = cv2.imread("images/image.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")
cy, cx = np.divmod(image.shape, 2)[0]
mode = 3

dft, spectrum = FFT(image, mode)

midpass = np.zeros(dft.shape, np.float32)

cv2.circle(midpass, (cx, cy), 60, (1, 1), -1)
cv2.circle(midpass, (cx, cy), 30, (0, 0), -1)

midpassed_dft = dft * midpass

midpassed_img = IFFT(midpassed_dft, image.shape, mode)


cv2.imshow("image", image)
cv2.imshow("midpassed_img", midpassed_img)
cv2.imshow("spectrum_img", spectrum)
cv2.imshow("midpass_spect", calc_spectrum(midpassed_dft))
cv2.waitKey(0)
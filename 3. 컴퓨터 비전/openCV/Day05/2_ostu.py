import cv2
import matplotlib.pyplot as plt

src = cv2.imread('./rice.png', cv2.IMREAD_GRAYSCALE)

th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY| cv2.THRESH_OTSU)
print('otsu:', th)
# 최적의 임계값은 131 이라고 출력된다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

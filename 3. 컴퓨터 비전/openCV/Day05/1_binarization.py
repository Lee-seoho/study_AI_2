import cv2
import matplotlib.pyplot as plt

src = cv2.imread('./cells.png', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([src], [0], None, [256], [0, 255])
hist

# 100보다 낮은 애들은 검은색으로 100보다 크면 흰색으로
a, dst1 = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY)
# 210보다 낮은 애들은 검은색으로 100보다 크면 흰색으로
b, dst2 = cv2.threshold(src, 210, 255, cv2.THRESH_BINARY)
# a와 b는 내가 직접 설정한 thresh(임계값)들이다.

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

plt.plot(hist)
plt.show()

cv2.waitKey()
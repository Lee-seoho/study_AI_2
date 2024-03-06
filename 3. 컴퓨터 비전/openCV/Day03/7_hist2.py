# dog.bmp 이미지를 사용하여 3채녈(RGB)로 계산해 히스토그램 그리기
# 단, 하나의 plot에서 RGB 그래프를 그리기
import cv2
import matplotlib.pyplot as plt

src = cv2.imread("./dog.bmp")

''' 
b = src[:, :, 0]
g = src[:, :, 1]
r = src[:, :, 2]

hist1 = cv2.calcHist([b], [0], None, [256], [0, 255])
hist2 = cv2.calcHist([g], [0], None, [256], [0, 255])
hist3 = cv2.calcHist([r], [0], None, [256], [0, 255])

plt.plot(hist1, color='b')
plt.plot(hist2, color='g')
plt.plot(hist3, color='r')

plt.show()
cv2.imshow("src", src)
cv2.waitKey()
'''

colors = ["b", "g", "r"]

bgr = cv2.split(src)

for (b, c) in zip(bgr, colors):
    hist = cv2.calcHist([b], [0], None, [256], [0, 255])
    plt.plot(hist, color=c)

cv2.imshow("src", src)
plt.show()
cv2.waitKey()
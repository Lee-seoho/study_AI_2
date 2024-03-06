import cv2

img = cv2.imread('./noise.bmp')
dst = cv2.medianBlur(img, 3)

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()
# 3 * 3 정방행렬에 담긴 이미지들을 1자로 쭉 피고 그것을 sort 하여 중앙값을 구한다음 그 중앙값으로 이미지를 평탄화 한다
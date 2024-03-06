import cv2

src = cv2.imread('./field.bmp')

# ycbcr = []
#
# dst = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
# ycbcr = cv2.split(dst)
# ycbcr = list(ycbcr)
# print(ycbcr)
#
# ycbcr[0] = cv2.equalizeHist((ycbcr[0]))
# dst = cv2.merge(ycbcr)
# dst = cv2.cvtColor(dst, cv2.COLOR_YCrCb2BGR)
#
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()

# 문제
# split(), merge()를 사용하지 않고 슬라이싱 또는 인덱싱을 이용하여 2_equalize2.py와 동일한 프로그램을 작성

dst = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
dst[:, :, 0] = cv2.equalizeHist(dst[:, :, 0])
dst = cv2.cvtColor(dst, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
import numpy as np
import cv2

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (7, 7))
#
# print(kernel)

img = cv2.imread('./circuit.bmp', cv2.IMREAD_GRAYSCALE)
gse = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
dst1 = cv2.erode(img, gse)
dst2 = cv2.dilate(img, gse)

cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
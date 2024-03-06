import cv2

img = cv2.imread('./dog.bmp')
cp = (img.shape[1]/2, img.shape[0]/2)
rot = cv2.getRotationMatrix2D(cp, 30, 0.5)
# angle : 각도/ scale : 이미지 크기
dst = cv2.warpAffine(img, rot, (0,0))

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()
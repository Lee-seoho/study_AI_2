import cv2

img = cv2.imread('./dog.bmp')
# img_test = img
img_copy = img.copy()

# x좌표가 91~210, y좌표가 125~245까지 영역에 (255, 102, 255) 색상으로 색칠
# img1 = np.full(((91)-(210), (125)-(245), 3), (255, 102, 255), dtype=np.uint8)

# img_test[91:210, 125:245] = (255, 102, 255)
img_copy[91:210, 125:245] = (255, 102, 255)

cv2.imshow('img', img)
# cv2.imshow('img_test', img_test)
cv2.imshow('img_copy', img_copy)

cv2.waitKey()
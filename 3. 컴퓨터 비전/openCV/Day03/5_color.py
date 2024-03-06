import cv2

src = cv2.imread("./candies.png")
print("shape", src.shape)
print("dtype", src.dtype)

# b = src[:, :, 0]
# g = src[:, :, 1]
# r = src[:, :, 2]
b, g, r = cv2.split(src)

cv2.imshow("src", src)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
cv2.waitKey()


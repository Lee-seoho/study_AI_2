import cv2

src1 = cv2.imread("./dog.bmp", cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread("./dog.bmp")

dst1 = cv2.add(src1, 100)
dst2 = cv2.add(src2, (100, 100, 100, 0))
dst3 = cv2.subtract(src1, (100))
dst4 = cv2.multiply(src1, (10))
dst5 = cv2.divide(src1, (10))


cv2.imshow("src1", src1)
cv2.imshow("src2", src2)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)
cv2.imshow("dst4", dst4)
cv2.imshow("dst5", dst5)


cv2.waitKey()

import cv2

img = cv2.imread("./dog.bmp")
cv2.imshow("image", img)

while True:
    keyvalue = cv2.waitKey()
    if keyvalue == ord("i") or keyvalue == ord("I"):
        img = ~img # ~: 이미지 반전시키기
        cv2.imshow("image", img)
    elif keyvalue == 27:
        break
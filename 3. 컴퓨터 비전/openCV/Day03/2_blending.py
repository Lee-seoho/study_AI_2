import cv2
import matplotlib.pyplot as plt

src1 = cv2.imread("./man.jpg")
src2 = cv2.imread("./turkey.jpg")

dst1 = src1 + src2
dst2 = cv2.add(src1, src2)

# src1 + src2와 cv2.add(src1, src2)의 차이점 설명하기
# src1 + src2 값이 255를 넘어가면 해당값의 256을 빼서 표현
# cv2.add(src1, src2)의 값이 255를 넘어가면 255를 고정

# cv2.imshow("dst1", dst1)
# cv2.imshow("dst2", dst2)
#
# cv2.waitKey()

img = {"src1": src1, "src2": src2, "dst1": dst1, "dst2": dst2}

for i, (k, v) in enumerate(img.items()):
    plt.subplot(2, 2, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)
plt.show()
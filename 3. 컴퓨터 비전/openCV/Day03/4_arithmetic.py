# add, addWeighted, subtract, absdiff
# dog.jpg와 squared.bmp 위 연산을 시도
# matplotlib의 subplot을 이용하여 이미지를 비교

import cv2
import matplotlib.pyplot as plt

src1 = cv2.imread("./dog.jpg")
src2 = cv2.imread("./square.bmp")

alpha = 0.5

dst1 = cv2.add(src1, src2)
dst2 = cv2.addWeighted(src1, alpha, src2, (1-alpha), 0)
dst3 = cv2.subtract(src1, src2)
dst4 = cv2.absdiff(src1, src2)

img = {"dst1": dst1, "dst2": dst2, "dst3": dst3, "dst4": dst4}

for i, (k, v) in enumerate(img.items()):
    plt.subplot(2, 2, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)
plt.show()

# plt.subplot(2, 2, 1), plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB)), plt.title('add')
# plt.subplot(2, 2, 2), plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB)), plt.title('addWeighted')
# plt.subplot(2, 2, 3), plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB)), plt.title('subtract')
# plt.subplot(2, 2, 4), plt.imshow(cv2.cvtColor(dst4, cv2.COLOR_BGR2RGB)), plt.title('absdiff')
#
# plt.show()
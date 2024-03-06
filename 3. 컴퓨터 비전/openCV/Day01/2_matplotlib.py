import cv2
import matplotlib.pyplot as plt


# # cv를 통해 출력
# img = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('img', img)
# cv2.waitKey()



# # matplotlib을 통해 그레이스케일 출력
# img = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
# plt.axis('off')
# plt.imshow(img, cmap='gray')
# plt.show()





# # matplotlib을 통해 트루컬러 출력
# img = cv2.imread('./dog.bmp') # BGR이기 때문에
# plt.axis('off')
# plt.imshow(img)
# plt.show()




# # matplotlib을 통해 트루컬러 출력
# img = cv2.imread('./dog.bmp') # BGR이기 때문에
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.axis('off')
# plt.imshow(img)
# plt.show()



img1 = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('./dog.bmp')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.axis('off')
plt.imshow(img1, cmap='gray')

plt.subplot(122)
plt.axis('off')
plt.imshow(img2)

plt.show()
import cv2

# 실행: 컨트롤 + 쉬프트 + F10
# print('현재 openCV 버전: ', cv2.__version__)

# 그레이스케일 영상
img = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)

# # # 트루컬러 영상
# img = cv2.imread('./dog.bmp')
# # print(img)
# #
cv2.imshow('img', img) # 창이름, 영상
cv2.waitKey() # 키를 입력할 때까지 대기

import cv2

img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
# print('img_gray type: ', type(img_gray))
# print('img_gray shape: ', img_gray.shape)
# print('img_gray dtype: ', img_gray.dtype)

img_color = cv2.imread('./dog.bmp')
# print('img_color type: ', type(img_color))
# print('img_color shape: ', img_color.shape)
# print('img_color dtype: ', img_color.dtype)

# img_color의 정보를 아래와 같이 출력
# img_color 사이즈: 548 * 364
# print('img_color 사이즈: ', img_color.shape[1], '*', img_color.shape[0])
'''
강사님
h, w = img_color.shape[:2]
print(f'img_color 사이즈: {w}*{h}')
'''
# img_gray가 그레이스케일 영상인지 컬러 영상인지 구별하는 프로그램을 작성
# if문을 사용
# "img_gray는 그레이스케일 영상입니다"
# if len(img_gray.shape) == 2:
#     print("img_gray는 그레이스케일 영상입니다")
# else:
#     print("img_gray는 그레이스케일 영상이 아닙니다")
'''
강사님
if len(img_gray.shape) == 2:
    print('img_gray는 그레이스케일 영상입니다')
elif len(img_gray.shape) == 3:
    print('img_gray는 컬러 영상입니다')
'''


#img_color에 특정 색 정보로 영상을 출력
# BGR: (255, 102, 255)
# h, w = img_color.shape[:2]
#
# for x in range(h):
#     for y in range(w):
#         img_color[x, y] = (255, 102, 255)
#
# cv2.imshow('img_color', img_color)
# cv2.waitKey()
'''
강사님
for x in range(h):
    for y in range(w):
    img_color[x, y] = (255, 102, 255)
    
cv2.imshow('img_color', img_color)
cv2.waitKey()
'''

# for문을 간단하게 쓰면
img_color[:,:] = (255, 102, 255)

cv2.imshow('img_color', img_color)
cv2.waitKey()

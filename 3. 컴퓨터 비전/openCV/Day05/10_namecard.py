import cv2
import numpy as np
import sys

src = cv2.imread('./namecard.jpg')

# namecard의 가로 세로를 가져온다.
h, w = src.shape[:2]
# 화면의 세로를 500픽셀로 가정한다.
dh = 500
# A4용지 크기: 210*297cm
# A4 용지 비율을 맞추기 위해 아래와 같은 코드를 쓴다.
dw = round(dh * 297 / 210)

# 원본의 좌표 잡기
srcQuad = np.array([[30, 30], [30, h-30], [w-30, h-30], [w-30, 30]], np.float32)
# 결과물의 좌표 잡기
dstQuad = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32)
# 각 방향에 있는 원이 드래그 되고 있는가에 따라 변화 됨 현재는 초기화 상태
dragSrc = [False, False, False, False]

# 함수 만들기
def drawROI(img, corners):
    cpy = img.copy()
    # 컬러 값 지정
    c1 = (192, 192, 255)
    c2 = (128, 128, 255)

    # 좌표를 가지고 와서 그 좌표의 갯수 만큼 돈다.
    for pt in corners:
        # 반지름을 25로 잡고 색상은 c1이고 가운데 색상을 채우는 원을 그린다
        cv2.circle(cpy, tuple(pt.astype(int)), 25, c1, -1)

    # 선 그리기 corners에서 받은 좌표 0번째 꼭지점에서 1번째 꼭지점으로 ... 4번째 까지, 컬러는 c2, 두깨 2짜리
    cv2.line(cpy, tuple(corners[0].astype(int)), tuple(corners[1].astype(int)), c2, 2)
    cv2.line(cpy, tuple(corners[1].astype(int)), tuple(corners[2].astype(int)), c2, 2)
    cv2.line(cpy, tuple(corners[2].astype(int)), tuple(corners[3].astype(int)), c2, 2)
    cv2.line(cpy, tuple(corners[3].astype(int)), tuple(corners[0].astype(int)), c2, 2)

    return cpy


def onMouse(event, x, y, flags, param):
    global srcQuad, dragSrc, ptOld, src

    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(4):
            # 마우스 포인트가 원 안에 들어왔다면
            if cv2.norm(srcQuad[i] - (x, y)) < 25:
                # dragSrc가 True로 변경 되고
                dragSrc[i] = True
                # 위치 값을 ptOld변수에 넣어주고 끝
                ptOld = (x, y)
                break

    if event == cv2.EVENT_LBUTTONUP:
        for i in range(4):
            # L버튼을 뗐을 때 dragSrc를 False로 바꿔준다
            dragSrc[i] = False

    # 마우스를 움직였을 때
    if event == cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            # dragSrc가 True가 있으면
            if dragSrc[i]:
                dx = x - ptOld[0]
                dy = y - ptOld[1]
                srcQuad[i] += (dx, dy)
                cpy = drawROI(src, srcQuad)
                cv2.imshow('img', cpy)
                ptOld = (x, y)
                break

disp = drawROI(src, srcQuad)
cv2.imshow('img', disp)
cv2.setMouseCallback('img', onMouse)

while True:
    key = cv2.waitKey()
    if key == 13:
        break
    elif key == 27:
        sys.exit()

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (dw, dh), flags=cv2.INTER_CUBIC)
cv2.imshow('dst', dst)
cv2.waitKey()
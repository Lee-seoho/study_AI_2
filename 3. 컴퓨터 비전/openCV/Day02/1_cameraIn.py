import cv2
import sys

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다")
    sys.exit()

print("카메라 연결 성공!")
print("가로 사이즈: ", int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("세로 사이즈: ", int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("frame", frame)
    if cv2.waitKey(10) == 27: # esc가 27번임 1000은 1초에 한번씩 10은 0.01초에 한번씩 화면이 바뀐다
        break

cap.release()
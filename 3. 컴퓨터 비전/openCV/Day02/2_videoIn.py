import cv2
import sys

cap = cv2.VideoCapture("./city.mp4")

if not cap.isOpened():
    print("동영상을 불러올 수 없습니다")
    sys.exit()

print("동영상 연결 성공!")

print("가로 사이즈:", int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("세로 사이즈:", int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("프레임 수: ", int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
print("FPS: ", cap.get(cv2.CAP_PROP_FPS))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("frame", frame)
    if cv2.waitKey(10) == 27: # esc가 27번임 1000은 1초에 한번씩 10은 0.01초에 한번씩 화면이 바뀐다
        break

cap.release()
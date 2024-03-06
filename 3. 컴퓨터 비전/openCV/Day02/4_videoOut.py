import cv2
import sys

cap1 = cv2.VideoCapture("./city.mp4")
cap2 = cv2.VideoCapture("./cloud.mp4")

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
print(frame_cnt1)
print(frame_cnt2)

fps1 = cap1.get(cv2.CAP_PROP_FPS)
fps2 = cap2.get(cv2.CAP_PROP_FPS)
print(fps1)
print(fps2)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("width: ", w)
print("height: ", h)

fourcc = cv2.VideoWriter.fourcc(*"DIVX")
out = cv2.VideoWriter("mix.avi", fourcc, fps1, (w, h))

for i in range(frame_cnt1):
    ret, frame = cap1.read()
    cv2.imshow("output", frame)
    out.write(frame)
    if cv2.waitKey(10) == 27:
        break

for i in range(frame_cnt2):
    ret, frame = cap2.read()
    cv2.imshow("output", frame)
    out.write(frame)
    if cv2.waitKey(10) == 27:
        break

cap1.release()
cap2.release()
out.release()
# mean-shift目标检测
import cv2 as cv
import numpy as np


def nothing():
    pass


video = cv.VideoCapture("./assets/amazing.flv")

_, first_frame = video.read()
print(first_frame.shape)  # (288, 512, 3)
cv.imshow("first_frame", first_frame)
x = 130
y = 100
width = 300
height = 144
# 计算roi区域
roi = first_frame[y:y + height, x:x + width]
# 将roi区域转为HSV
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
#
roi_hist = cv.calcHist([hsv_roi], [0], None, [180], [0, 180])
# 归一化
roi_hist = cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
print(roi_hist)

term_criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
green = (0, 255, 0)

while True:
    _, frame = video.read()
    if frame is None:
        break
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    _, track_window = cv.meanShift(mask, (x, y, width, height), term_criteria)
    x, y, w, h = track_window

    cv.rectangle(frame, (x, y), (x + w, y + h), green, 2)

    cv.imshow("roi", roi)
    cv.imshow("mask", mask)
    cv.imshow("Frame", frame)

    key = cv.waitKey(60) & 0xFF
    if key == 27:
        break

video.release()
# 销毁窗体
cv.destroyAllWindows()

# 创建视频的Trackbar (类似于进度条)
import cv2 as cv
import numpy as np


def nothing():
    pass


video = cv.VideoCapture("./assets/amazing.flv")

cv.namedWindow("frame")
# 创建Trackbar. 参数：trackbar的名称，窗口名，最小值，数量，回调方法
cv.createTrackbar("test", "frame", 0, 100, nothing)
# 创建切换颜色和灰度的trackbar
cv.createTrackbar("color/gray", "frame", 0, 1, nothing)

while True:
    # 读取视频，frame表示第一帧的图片，ret表示视频的信息
    _, frame = video.read()

    # 读取到最后
    if frame is None:
        break
    # 获得trackbar的位置。参数：trackbar的名称，窗口名
    test = cv.getTrackbarPos("test", "frame")
    # 操作trackbar
    font = cv.FONT_HERSHEY_COMPLEX
    cv.putText(frame, str(test), (50, 150), font, 4, (0, 0, 255), thickness=3)

    # 切换颜色/灰度的Trackbar
    s = cv.getTrackbarPos("color/gray", "frame")
    if s == 0:
        pass
    else:
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("frame", frame)

    # 如果cv.waitKey()中的参数小于1的时候，画面停止，就是属于无限等待输入，输入的频率越快，播放的速度就越快
    key = cv.waitKey(30) & 0xFF
    # 按ESC退出
    if key == 27:
        break

# 释放资源
video.release()
# 销毁窗体
cv.destroyAllWindows()

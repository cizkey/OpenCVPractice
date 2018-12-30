# 使用HSV色彩空间进行对象检测
import cv2 as cv
import numpy as np

video = cv.VideoCapture("./assets/amazing.flv")

while True:
    # 读取视频，frame表示第一帧的图片，ret表示视频的信息
    _, frame = video.read()

    # 读取到最后
    if frame is None:
        break

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

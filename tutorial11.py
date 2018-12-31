# Perspective transformation 投影变化
# 参见： https://blog.csdn.net/a352611/article/details/51418178 第4点 投影变化
import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

red = (0, 0, 255)

while True:
    # 读取视频，frame表示第一帧的图片，ret表示视频的信息
    _, frame = video.read()

    # 读取到最后
    if frame is None:
        break

    # 原来的四个顶点
    cv.circle(frame, (155, 120), 5, red, -1)
    cv.circle(frame, (480, 120), 5, red, -1)
    cv.circle(frame, (20, 475), 5, red, -1)
    cv.circle(frame, (620, 475), 5, red, -1)

    # 原来的四个顶点讲投影到新图像的位置
    pts1 = np.float32([[155, 120], [480, 120], [20, 475], 620, 475])
    # 设置一个新的图像大小，400 * 600
    pts2 = np.float32([[0, 0], [400, 0], [0, 600], [400, 600]])
    # 获得Matrix
    matrix = cv.getPerspectiveTransform(pts1, pts2)
    # 应用matrix到图像上
    result = cv.warpPerspective(frame, matrix, (400, 600))

    cv.imshow("frame", frame)
    # 显示投影变化后的图像
    cv.imshow("Perspective transformation", result)

    # 如果cv.waitKey()中的参数小于1的时候，画面停止，就是属于无限等待输入，输入的频率越快，播放的速度就越快
    key = cv.waitKey(30) & 0xFF
    # 按ESC退出
    if key == 27:
        break

# 释放资源
video.release()
# 销毁窗体
cv.destroyAllWindows()

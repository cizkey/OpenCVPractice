# 读取本地视频文件，翻转和保存视频
import cv2 as cv
import numpy as np

video = cv.VideoCapture("./assets/amazing.flv")

# Fourcc 就是一个4字节码，用来确定视频的编码格式
fourcc = cv.VideoWriter_fourcc(*"XVID")
# 设置视频保存都 文件名， 编码格式， 帧率， 视频分辨率(通过读取frame.shape获得)
out = cv.VideoWriter("./assets/flipped_amazing.avi", fourcc, 25, (512, 288))

while True:
    # 读取视频，frame表示第一帧的图片，ret表示视频的信息
    ret, frame = video.read()

    # 读取到最后
    if frame is None:
        break
    # 通过获得frame图片的信息 (288,512,3) 高为288，宽为512，色彩深度为3
    print(frame.shape)
    # 翻转视频。 0 表示180倒置翻转，1 表示镜像翻转
    flip_frame = cv.flip(frame, 1)

    # 显示每一帧图片
    cv.imshow("flip frame", flip_frame)
    cv.imshow("frame", frame)

    # 保存视频
    out.write(flip_frame)

    # 如果cv.waitKey()中的参数小于1的时候，画面停止，就是属于无限等待输入，输入的频率越快，播放的速度就越快
    key = cv.waitKey(30) & 0xFF
    # 按ESC退出
    if key == 27:
        break

# 释放资源
video.release()
out.release()
# 销毁窗体
cv.destroyAllWindows()

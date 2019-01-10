#  基于dlib的face detection, eye detection
#  dlib的检测比使用opencv的人脸检测更加精准和强大

### 重要说明
#  安装dlib
#       首先确保python版本为3.6，从https://pypi.org/simple/dlib/下载dlib-19.8.1-cp36-cp36m-win_amd64.whl，
#       然后使用pip install dlib-19.8.1-cp36-cp36m-win_amd64.whl命令安装
#  准备人脸关键点模型
#       从http://dlib.net/files/下载shape_predictor_68_face_landmarks.dat.bz2，解压后拷贝到工程中即可

###
# 参考文章：
# https://www.cnblogs.com/vipstone/p/8964656.html
###

import cv2 as cv
import dlib

# 读入图片, im --> image
image = cv.imread("./assets/girl.jpg")
# 转为灰度图片
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# 获得检测器
detector = dlib.get_frontal_face_detector()
# 根据关键点训练模型，获得预测器
predictor = dlib.shape_predictor("./dat/shape_predictor_68_face_landmarks.dat")
# 检测人脸特征
faces = detector(gray_image)

# 绿色
green = (0, 255, 0)
thickness = 2


def mid_point(p1, p2):
    return int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2)


for face in faces:
    landmarks = predictor(gray_image, face)

    # 绘制所有68个关键点
    for pt in landmarks.parts():
        pt_pos = (pt.x, pt.y)
        cv.circle(image, pt_pos, 2, green, thickness)

    # 绘制人脸区域
    x, y = face.left(), face.top()
    x1, y1 = face.right(), face.bottom()
    cv.rectangle(image, (x, y), (x1, y1), green, thickness)

    # 绘制左边眼关键区域
    left_point = (landmarks.part(36).x, landmarks.part(36).y)
    right_point = (landmarks.part(39).x, landmarks.part(39).y)
    center_top = mid_point(landmarks.part(37), landmarks.part(38))
    center_bottom = mid_point(landmarks.part(41), landmarks.part(40))
    # 绘制眼睛的水平横线和纵线
    hor_line = cv.line(image, left_point, right_point, green, thickness)
    ver_line = cv.line(image, center_top, center_bottom, green, thickness)

cv.imshow("Image", image)

# 等待键盘输入
cv.waitKey(0) & 0xFF
# 销毁窗体
cv.destroyAllWindows()

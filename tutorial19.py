#  基于Haar cascade的人脸检测

###
# 说明：
# opencv自带的haar特征分类器是一个xml文件存放在openCV下的/data/haarcascades目录下
# 可以到https://github.com/opencv/opencv/tree/master/data/haarcascades查看
# 其中包含已经训练好的分类器，包括：面部，眼睛，微笑等。
#
###

###
# 参考文章：
# https://www.cnblogs.com/21207-iHome/articles/6253796.html
###

import cv2 as cv

# 读入图片, im --> image
image = cv.imread("./assets/physical.jpg")
# 高斯模糊
blur_image = cv.GaussianBlur(image, (5, 5), 0)
# 转为灰度图片
gray_image = cv.cvtColor(blur_image, cv.COLOR_BGR2GRAY)
# 加载分类器
face_haar = cv.CascadeClassifier("./dat/haarcascade_frontalface_default.xml")
# face_haar = cv.CascadeClassifier("./dat/haarcascade_frontalface_alt_tree.xml")
# 检测图片中所有的脸
faces = face_haar.detectMultiScale(gray_image, 1.1, 5)

# 绿色
green = (0, 255, 0)
thickness = 2

# 绘制所有的人脸
for (x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x + w, y + h), green, thickness)

# 显示图片
cv.imshow("Image", image)

# 等待键盘输入
cv.waitKey(0) & 0xFF
# 销毁窗体
cv.destroyAllWindows()

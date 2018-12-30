#  在图片上绘制Drawing on images

import cv2 as cv
import numpy as np

# 读入图片, im --> image
image = cv.imread("./assets/animal.jpg")

shape = image.shape
print(shape)  # (667, 1000, 3)

# 在cv中色彩为BGR模式
blue = (255, 0, 0)
red = (0, 0, 255)
green = (0, 255, 0)
violet = (180, 0, 180)
yellow = (0, 180, 180)
white = (255, 255, 255)

# 画线。参数：图像，第一点，第二点，颜色，thickness粗细,
cv.line(image, (50, 30), (950, 600), blue, thickness=5)

# 画圆。参数：图像，中心点，半径，颜色，填充模式(0不填充，-1填充)
cv.circle(image, (200, 300), 23, red, 0)

# 画矩形 (参数类似画圆)
cv.rectangle(image, (50, 40), (950, 90), green, -1)

# 画椭圆
cv.ellipse(image, (400, 300), (100, 50), 0, 0, 360, violet, -1)

# 使用np生成顶点
points = np.array([[[140, 230], [400, 230], [320, 250], [280, 250]]], np.int32)
# 画多边形
cv.polylines(image, [points], True, yellow, thickness=3)

# 绘制文字
font = cv.FONT_HERSHEY_COMPLEX
cv.putText(image, "Maxwell", (20, 180), font, 4, red)

# 显示图片
cv.imshow("Image", image)

# 等待键盘输入
cv.waitKey(0)
# 销毁窗体
cv.destroyAllWindows()

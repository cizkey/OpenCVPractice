# smooth image: 去除图像上的噪点 noise
# 一般采用模糊的方式
# 均值模糊

import cv2 as cv
import numpy as np

img = cv.imread("./assets/girl_noise.jpg")

# 均值模糊
averaging = cv.blur(img, (7, 7))
# 高斯模糊
gaussian = cv.GaussianBlur(img, (7, 7), 0)
# 中值模糊
median = cv.medianBlur(img, 7)
# Bilateral Filters 双边滤波： 双边滤波是一种非线性滤波器，它可以达到保持边缘、降噪平滑的效果。和其他滤波原理一样，双边滤波也是采用加权平均的方法，用周边像素亮度值的加权平均代表某个像素的强度，所用的加权平均基于高斯分布
bilateral = cv.bilateralFilter(img, 7, 75, 75)

cv.imshow("girl_noise", img)
cv.imshow("averaging", averaging)
cv.imshow("gaussian", gaussian)
cv.imshow("median", median)
cv.imshow("bilateral", bilateral)

cv.waitKey(0)
# 销毁窗体
cv.destroyAllWindows()

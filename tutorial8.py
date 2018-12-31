# 图像二值化 binary threshold, 使用二进制阈值来分割图像
# threshold函数作用： 去掉噪，例如过滤很小或很大像素值的图像点。

# binary_threshold通过一个自动确定的全局阈值并返回区域中的分段区域来分割单通道图像。例如：在同质照明的背景下对字符的分割很有用。
# bin_threshold:二值化阈值，自动地全局阈值方法，使用Threshold找到两个波峰之间的最小值,分割出来的是非黑即白。

# 二值化的方法：（参考：http://blog.csdn.net/jia20003/article/details/8074627）
# 方法一：扫描图像的每个像素值，值小于127的将像素值设为0(黑色)，值大于等于127的像素值设为255(白色)。该方法的好处是计算量少速度快。
# 方法二：计算像素的平均值K，扫描图像的每个像素值如像素值大于K像素值设为255(白色)，值小于等于K像素值设为0(黑色)。
# 方法三：使用直方图方法来寻找二值化阈值，直方图是图像的重要特质，直方图方法选择二值化阈值主要是发现图像的两个最高的峰，然后在阈值取值在两个峰之间的峰谷最低处。

import cv2 as cv
import numpy as np

# 读入图片, im --> image
# 原图载入为灰度图片。另外转为灰度图片的方式是使用cv.cvt()
image = cv.imread("./assets/animal.jpg", cv.IMREAD_GRAYSCALE)

# 阈值
_, threshold_binary = cv.threshold(image, 128, 255, cv.THRESH_BINARY)
# 反阈值
_, threshold_binary_inv = cv.threshold(image, 128, 255, cv.THRESH_BINARY_INV)
# 截断
_, threshold_trunc = cv.threshold(image, 128, 255, cv.THRESH_TRUNC)
# 阈值二值化
_, threshold_to_zero = cv.threshold(image, 128, 255, cv.THRESH_TOZERO)
# 反二值化
_, threshold_to_zero_inv = cv.threshold(image, 128, 255, cv.THRESH_TOZERO_INV)

cv.imshow("image", image)
cv.imshow("threshold_binary", threshold_binary)
cv.imshow("threshold_binary_inv", threshold_binary_inv)
cv.imshow("threshold_trunc", threshold_trunc)
cv.imshow("threshold_to_zero", threshold_to_zero)
cv.imshow("threshold_to_zero_inv", threshold_to_zero_inv)

# 等待键盘输入
cv.waitKey(0)
# 销毁窗体
cv.destroyAllWindows()

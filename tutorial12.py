# 自适应阈值化 Adaptive threshold
# adaptive threshold only will greyscale image !!!

# 图像阈值化的一般目的是从灰度图像中分离目标区域和背景区域，
# 然而仅仅通过设定固定阈值很难达到理想的分割效果。
# 在实际应用中，我们可以通过某个像素的邻域以某种方法确定这个像素应该具有的阈值，
# 进而保证图像中各个像素的阈值会随着周期围邻域块的变化而变化。
# 在灰度图像中，灰度值变化明显的区域往往是物体的轮廓，
# 所以将图像分成一小块一小块的去计算阈值往往会得出图像的轮廓，而固定阈值的方法就不行。


import cv2 as cv
import numpy as np

img = cv.imread("./assets/book_page.jpg")

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 固定阈值化
_, threshold = cv.threshold(img, 110, 255, cv.THRESH_BINARY)

# 自适应阈值
#####
# InputArray src：源图像
#
# OutputArray dst：输出图像，与源图像大小一致
#
# int adaptiveMethod：在一个邻域内计算阈值所采用的算法，有两个取值，分别为 ADAPTIVE_THRESH_MEAN_C 和 ADAPTIVE_THRESH_GAUSSIAN_C 。
#
# ADAPTIVE_THRESH_MEAN_C的计算方法是计算出领域的平均值再减去第七个参数double C的值
#
# ADAPTIVE_THRESH_GAUSSIAN_C的计算方法是计算出领域的高斯均值再减去第七个参数double C的值
#
# int thresholdType：这是阈值类型，只有两个取值，分别为 THRESH_BINARY 和THRESH_BINARY_INV  具体的请看官方的说明，这里不多做解释
#
# int blockSize：adaptiveThreshold的计算单位是像素的邻域块，邻域块取多大，就由这个值作决定
#
# double C：在对参数int adaptiveMethod的说明中，这个参数实际上是一个偏移值调整量
#
# 从上面的说明中可以看出，使用函数adaptiveThreshold的关键是确定blockSize和C的值，明白了这两个值的意义之后，在实际项目中，应该可以根据试验法选出较为合适的值吧！
#####
# mean_c 算法
mean_c = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 13)
# 高斯算法
gaussian_c = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 31, 17)

cv.imshow("book_page", img)

# 使用阈值二值化的效果很一般
cv.imshow("threshold_binary", threshold)
cv.imshow("adaptive_threshold_mean_c", mean_c)
cv.imshow("adaptive_threshold_gaussian_c", gaussian_c)

cv.waitKey(0)
# 销毁窗体
cv.destroyAllWindows()

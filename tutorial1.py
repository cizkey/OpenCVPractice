#  读取图片和保存图片

import cv2 as cv
import numpy as np

# 读入图片, im --> image
image = cv.imread("./assets/animal.jpg")
# 转为灰度图片
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

cv.imwrite("./assets/out_image.png", gray_image)

# 显示图片
cv.imshow("Gray Image", gray_image)
cv.imshow("Image", image)

# 等待键盘输入
cv.waitKey(0)
# 销毁窗体
cv.destroyAllWindows()

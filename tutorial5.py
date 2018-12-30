#  叠加图片

import cv2 as cv
import numpy as np

# 读入图片, im --> image
image1 = cv.imread("./assets/road.jpg")
image2 = cv.imread("./assets/car.jpg")

# 叠加图片
# 前提：两张图片具有相同都尺寸

# 添加权重
weighted = cv.addWeighted(image1, 1, image2, 0.5, 0)
image = cv.add(image1, image2)

# 显示图片
cv.imshow("image1", image1)
cv.imshow("image2", image2)
cv.imshow("Image", image)

# 等待键盘输入
cv.waitKey(0)
# 销毁窗体
cv.destroyAllWindows()

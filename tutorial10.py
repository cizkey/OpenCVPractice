# 图像基本的几何变化 basic geometric transformations
# 仿射变换warpAffine
# Affine Transform描述了一种二维仿射变换的功能，它是一种二维坐标之间的线性变换，
# 保持二维图形的“平直性”(即变换后直线还是直线，圆弧还是圆弧)和“平行性”(其实是保持二维图形间的相对位置关系不变，平行线还是平行线，
# 而直线上的点位置顺序不变，另特别注意向量间夹角可能会发生变化)。
# 仿射变换可以通过一系列的原子变换的复合来实现包括：平移(Translation)、缩放(Scale)、翻转(Flip)、旋转(Rotation)和错切(Shear).

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("./assets/girl2.jpg")

rows, cols, channels = img.shape
print("Height: ", rows)
print("Width： ", cols)

# 图像缩放
scale_img = cv.resize(img, None, fx=1 / 2, fy=1 / 2)

# 图像平移
matrix_t = np.float32([[1, 0, 50], [0, 1, 50]])
translate_img = cv.warpAffine(img, matrix_t, (cols, rows))

# 图像旋转
matrix_r = cv.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
rotate_img = cv.warpAffine(img, matrix_r, (cols, rows))

# 显示图像
cv.imshow("image", img)
cv.imshow("scale_img", scale_img)
cv.imshow("translate_img", translate_img)
cv.imshow("rotate_img", rotate_img)

cv.waitKey(0)
cv.destroyAllWindows()

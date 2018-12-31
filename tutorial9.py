#  histgraph 直方图： 直方图是频次的累计

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# img = np.zeros((100, 100), np.uint8)
# cv.rectangle(img, (0, 50), (100, 100), (255, 255, 255), -1)
#
# cv.imshow("img", img)


# 参数： img.ravel() 将图像转成一维数组
# bins : 256, 每个bin的宽度为1
# range： 区间为[0,256]
# 参见：https://www.cnblogs.com/Undo-self-blog/p/8439149.html
# plt.hist(img.ravel(), 256, [0, 256])
# plt.show()
# 等待键盘输入
# cv.waitKey(0)
# 销毁窗体
# cv.destroyAllWindows()


img = cv.imread("./assets/girl2.jpg")
# cv.imshow("image", img)

b, g, r = cv.split(img)
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)

plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

# 边缘检测

import cv2 as cv
import numpy as np

img = cv.imread("./assets/animal.jpg", cv.IMREAD_GRAYSCALE)
img = cv.GaussianBlur(img, (5, 5), 0)

soblex = cv.Sobel(img, cv.CV_64F, 1, 0)
sobley = cv.Sobel(img, cv.CV_64F, 0, 1)

laplacian = cv.Laplacian(img, cv.CV_64F, ksize=3)

canny = cv.Canny(img, 10, 80)

cv.imshow("animal", img)
cv.imshow("soblex", soblex)
cv.imshow("sobley", sobley)
cv.imshow("laplacian", laplacian)
cv.imshow("canny", canny)

cv.waitKey(0)
# 销毁窗体
cv.destroyAllWindows()

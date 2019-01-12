#  KNN实现手写数字识别

###
# 这个手写数字识别总体来说比较刻意，不能用于生产，只是基本的演示
###

import cv2 as cv
import numpy as np

# 训练数据
digits = cv.imread("./assets/digits.png", cv.IMREAD_GRAYSCALE)
# 测试数据
test_digits = cv.imread("./assets/test_digits.png", cv.IMREAD_GRAYSCALE)

# 垂直分割
rows = np.vsplit(digits, 50)
cells = []

# 遍历每一行数字
for row in rows:
    # 横向分割
    row_cells = np.hsplit(row, 50)
    # 遍历每一行的元素
    for cell in row_cells:
        # flatten()返回一个折叠成一维的数组
        cell = cell.flatten()
        cells.append(cell)
cells = np.array(cells, dtype=np.float32)

# 初始化特征，np.arange(10)返回从0~9的数组
k = np.arange(10)
# 标记每个数字的特征
cells_labels = np.repeat(k, 250)

# 开始测试
test_digits = np.vsplit(test_digits, 50)
test_cells = []
for d in test_digits:
    d = d.flatten()
    test_cells.append(d)
test_cells = np.array(test_cells, dtype=np.float32)

# KNN (K近邻算法)
knn = cv.ml.KNearest_create()
# 使用KNN训练数据 (有监督学习有特征标签)
knn.train(cells, cv.ml.ROW_SAMPLE, cells_labels)

# 测试数据获得识别结果
ret, result, neighbours, dist = knn.findNearest(test_cells, k=3)
# 输出结果
print(result)

# 查找和绘制轮廓
# 这种是基于颜色的运动物体轮廓检查，不是很准确，只有当目标物体颜色和背景相差很大时才能比较清晰的描述目标的轮廓
# 通过trackbar，不断的调节hsv的lower和upper颜色，实现颜色区域的确定
import cv2 as cv
import numpy as np


def nothing():
    pass


video = cv.VideoCapture("./assets/amazing.flv")

# cv.namedWindow("Trackbars")
# cv.createTrackbar("L-H", "Trackbars", 0, 179, nothing)
# cv.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
# cv.createTrackbar("L-V", "Trackbars", 0, 255, nothing)
# cv.createTrackbar("H-H", "Trackbars", 179, 179, nothing)
# cv.createTrackbar("H-S", "Trackbars", 126, 255, nothing)
# cv.createTrackbar("H-V", "Trackbars", 255, 255, nothing)

green = (0, 255, 0)

while True:
    _, frame = video.read()
    if frame is None:
        break
    # 将图像转为HSV色彩空间图像
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    blur_frame = cv.GaussianBlur(hsv_frame, (5, 5), 0)

    # l_h = cv.getTrackbarPos("L-H", "Trackbars")
    # l_s = cv.getTrackbarPos("L-S", "Trackbars")
    # l_v = cv.getTrackbarPos("L-V", "Trackbars")
    # h_h = cv.getTrackbarPos("H-H", "Trackbars")
    # h_s = cv.getTrackbarPos("H-S", "Trackbars")
    # h_v = cv.getTrackbarPos("H-V", "Trackbars")

    # 黄色颜色值
    # lower_yellow = np.array([l_h, l_s, l_v])
    # upper_yellow = np.array([h_h, h_s, h_v])
    lower_yellow = np.array([0, 0, 0])
    upper_yellow = np.array([170, 86, 255])
    # 创建mask
    mask = cv.inRange(hsv_frame, lower_yellow, upper_yellow)
    # 查找轮廓
    _, contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    # 排除噪点
    for contour in contours:
        area = cv.contourArea(contour)
        print(area)
        if area > 50:
            cv.drawContours(frame, contour, -1, green, 2)
    # cv.drawContours(frame, contours, -1, green, 1)

    cv.imshow("Frame", frame)
    cv.imshow("hsv_frame", hsv_frame)
    cv.imshow("Mask", mask)

    key = cv.waitKey(60) & 0xFF
    if key == 27:
        break

video.release()
# 销毁窗体
cv.destroyAllWindows()

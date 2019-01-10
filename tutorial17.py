# mean-shift目标检测，运动目标检测， 失败版本！！！！ 以后会逐渐完善，最终达到目的
import cv2 as cv
import numpy as np


def get_roi_hist(full_frame, x, y, w, h):
    # 确定头部的roi
    roi = full_frame[y:y + h, x:x + w]
    # 头部roi转hsv
    hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
    # 创建头部的mask
    mask = cv.inRange(hsv_roi, np.array([0, 32, 48]), np.array([180, 255, 255]))  # 这个inRange区域待调整
    # 计算头部的直方图
    roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
    # 归一化头部直方图
    roi_hist = cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
    return roi_hist


def draw_tracking(roi_hist, x, y, w, h):
    mask = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    _, track_window = cv.meanShift(mask, (x, y, w, h), term_criteria)
    x, y, w, h = track_window
    cv.rectangle(frame, (x, y), (x + w, y + h), green, 1)
    # ret, track_window = cv.CamShift(mask, (x, y, w, h), term_criteria)
    # pts = cv.boxPoints(ret)
    # pts = np.int0(pts)
    # img = cv.polylines(frame, [pts], True, green, 1)
    # cv.imshow("img", img)
    pass


def nothing():
    pass


video = cv.VideoCapture("./assets/dancing.mp4")

# cv.namedWindow("Trackbars")
# cv.createTrackbar("L-H", "Trackbars", 0, 179, nothing)
# cv.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
# cv.createTrackbar("L-V", "Trackbars", 0, 255, nothing)
# cv.createTrackbar("H-H", "Trackbars", 179, 179, nothing)
# cv.createTrackbar("H-S", "Trackbars", 59, 255, nothing)
# cv.createTrackbar("H-V", "Trackbars", 255, 255, nothing)

term_criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

green = (0, 255, 0)

# 获取第一帧
_, first_frame = video.read()

# 显示第一帧图像
cv.imshow("first_frame", first_frame)
# 获取头部的区域
x_head, y_head, w_head, h_head = (302, 80, 36, 39)
roi_hist_head = get_roi_hist(first_frame, x_head, y_head, w_head, h_head)

# 获取上半身的区域
x_upper_body, y_upper_body, w_upper_body, h_upper_body = (295, 122, 54, 58)
roi_hist_upper_body = get_roi_hist(first_frame, x_upper_body, y_upper_body, w_upper_body, h_upper_body)

# 获取下半身的区域
x_lower_body, y_lower_body, w_lower_body, h_lower_body = (270, 182, 87, 52)
roi_hist_lower_body = get_roi_hist(first_frame, x_lower_body, y_lower_body, w_lower_body, h_lower_body)

# 获取左腿的区域
x_left_leg, y_left_leg, w_left_leg, h_left_leg = (306, 236, 19, 73)
roi_hist_left_leg = get_roi_hist(first_frame, x_left_leg, y_left_leg, w_left_leg, h_left_leg)

# 获取左腿鞋子的区域
x_left_shoes, y_left_shoes, w_left_shoes, h_left_shoes = (299, 308, 20, 28)
roi_hist_left_shoes = get_roi_hist(first_frame, x_left_shoes, y_left_shoes, w_left_shoes, h_left_shoes)

# 获取右腿的区域
x_right_leg, y_right_leg, w_right_leg, h_right_leg = (320, 240, 11, 64)
roi_hist_right_leg = get_roi_hist(first_frame, x_right_leg, y_right_leg, w_right_leg, h_right_leg)

# 获取右腿鞋子的区域
x_right_shoes, y_right_shoes, w_right_shoes, h_right_shoes = (320, 299, 20, 30)
roi_hist_right_shoes = get_roi_hist(first_frame, x_right_shoes, y_right_shoes, w_right_shoes, h_right_shoes)

# 获取左手的区域
x_left_hand, y_left_hand, w_left_hand, h_left_hand = (230, 144, 29, 18)
roi_hist_left_hand = get_roi_hist(first_frame, x_left_hand, y_left_hand, w_left_hand, h_left_hand)

# 获取左手袖子的区域
x_left_sleeve, y_left_sleeve, w_left_sleeve, h_left_sleeve = (258, 148, 43, 40)
roi_hist_left_sleeve = get_roi_hist(first_frame, x_left_sleeve, y_left_sleeve, w_left_sleeve, h_left_sleeve)

# 获取右手的区域
x_right_hand, y_right_hand, w_right_hand, h_right_hand = (380, 68, 16, 29)
roi_hist_right_hand = get_roi_hist(first_frame, x_right_hand, y_right_hand, w_right_hand, h_right_hand)

# 获取右手袖子的区域
x_right_sleeve, y_right_sleeve, w_right_sleeve, h_right_sleeve = (353, 100, 37, 53)
roi_hist_right_sleeve = get_roi_hist(first_frame, x_right_sleeve, y_right_sleeve, w_right_sleeve, h_right_sleeve)

_, frame1 = video.read()
_, frame2 = video.read()

while True:
    # 获取视频每一帧
    _, frame = video.read()

    if frame is None:
        break

    d = cv.absdiff(frame1, frame2)

    cv.imshow("d", d)

    gray = cv.cvtColor(d, cv.COLOR_BGR2GRAY)

    blur = cv.GaussianBlur(gray, (7, 7), 0)

    _, th = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)

    dilated = cv.dilate(th, np.ones((3, 3), np.uint8), iterations=3)

    eroded = cv.erode(dilated, np.ones((3, 3), np.uint8), iterations=1)

    img, c, h = cv.findContours(eroded, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    font = cv.FONT_HERSHEY_SIMPLEX

    # for cc in c:
    #     area = cv.contourArea(cc)
    #     print(area)
    #     if area > 100:
    #         cv.drawContours(frame, cc, -1, green, 2)
    cv.drawContours(frame1, c, -1, green, 2)

    cv.imshow("inter", frame1)

    # 将每一帧转为HSV
    # blur_frame = cv.GaussianBlur(frame, (5, 5), 0)
    # hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    #
    # l_h = cv.getTrackbarPos("L-H", "Trackbars")
    # l_s = cv.getTrackbarPos("L-S", "Trackbars")
    # l_v = cv.getTrackbarPos("L-V", "Trackbars")
    # h_h = cv.getTrackbarPos("H-H", "Trackbars")
    # h_s = cv.getTrackbarPos("H-S", "Trackbars")
    # h_v = cv.getTrackbarPos("H-V", "Trackbars")

    # 黄色颜色值
    # lower_yellow = np.array([l_h, l_s, l_v])
    # upper_yellow = np.array([h_h, h_s, h_v])

    # 创建mask
    # mask = cv.inRange(hsv, lower_yellow, upper_yellow)
    # 查找轮廓
    # _, contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    # 排除噪点
    # for contour in contours:
    #     area = cv.contourArea(contour)
    #     print(area)
    #     if 40 < area < 10000:
    #         cv.drawContours(frame, contour, -1, green, 2)
    # cv.drawContours(frame, contours, -1, green, 1)

    # cv.imshow("hsv", hsv)
    # cv.imshow("Mask", mask)

    # # 确定头部的跟踪区域
    # draw_tracking(roi_hist_head, x_head, y_head, w_head, h_head)
    # # 确定上半身的跟踪区域
    # draw_tracking(roi_hist_upper_body, x_upper_body, y_upper_body, w_upper_body, h_upper_body)
    # # 确定下半身的跟踪区域
    # draw_tracking(roi_hist_lower_body, x_lower_body, y_lower_body, w_lower_body, h_lower_body)
    # # 确定左腿的跟踪区域
    # draw_tracking(roi_hist_left_leg, x_left_leg, y_left_leg, w_left_leg, h_left_leg)
    # # 确定左腿鞋子的跟踪区域
    # draw_tracking(roi_hist_left_shoes, x_left_shoes, y_left_shoes, w_left_shoes, h_left_shoes)
    # # 确定右腿的跟踪区域
    # draw_tracking(roi_hist_right_leg, x_right_leg, y_right_leg, w_right_leg, h_right_leg)
    # # 确定右腿鞋子的跟踪区域
    # draw_tracking(roi_hist_right_shoes, x_right_shoes, y_right_shoes, w_right_shoes, h_right_shoes)
    # # 确定左手的跟踪区域
    # draw_tracking(roi_hist_left_hand, x_left_hand, y_left_hand, w_left_hand, h_left_hand)
    # # 确定左手袖子的跟踪区域
    # draw_tracking(roi_hist_left_sleeve, x_left_sleeve, y_left_sleeve, w_left_sleeve, h_left_sleeve)
    # # 确定右手的跟踪区域
    # draw_tracking(roi_hist_right_hand, x_right_hand, y_right_hand, w_right_hand, h_right_hand)
    # # 确定右手袖子的跟踪区域
    # draw_tracking(roi_hist_right_sleeve, x_right_sleeve, y_right_sleeve, w_right_sleeve, h_right_sleeve)
    # 显示图像
    # cv.imshow("Dancing Girl", frame)

    # 等待键盘输入
    key = cv.waitKey(60) & 0xFF
    if key == 27:
        break

    frame1 = frame2
    _, frame2 = video.read()
    if frame2 is None:
        break

# 释放资源
video.release()
# 销毁窗体
cv.destroyAllWindows()

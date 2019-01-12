# 基于OpenCV的eye detection
####
# 注意事项：openCV版本目前已经到了4.0版本，部分api有修改
# 参考文章：https://pysource.com/2019/01/04/eye-motion-tracking-opencv-with-python/
####
import cv2 as cv

# 读取视频文件
video = cv.VideoCapture("./assets/eye_recording.flv")

green = (0, 255, 0)
thickness = 2

while True:
    ret, frame = video.read()
    if ret is False:
        break
    # 获取roi区域
    roi = frame[269: 795, 537: 1416]
    # 获取roi区域的形状信息
    rows, cols, _ = roi.shape
    # roi图像转为灰度图像
    gray_roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    # 高斯模糊降噪
    gray_roi = cv.GaussianBlur(gray_roi, (7, 7), 0)
    # 反向阈值二值化
    _, threshold = cv.threshold(gray_roi, 3, 255, cv.THRESH_BINARY_INV)
    # 查找阈值化后图像中的轮廓
    contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # 将找到的轮廓大小排序，用来获得最大面积的封闭轮廓区域，用来过滤无效的轮廓
    contours = sorted(contours, key=lambda c: cv.contourArea(c), reverse=True)

    # 绘制眼球的轮廓
    for cnt in contours:
        # 获得轮廓的外接矩形区域
        (x, y, w, h) = cv.boundingRect(cnt)
        # 绘制矩形区域
        cv.rectangle(roi, (x, y), (x + w, y + h), green, thickness)
        # 绘制十字线
        cv.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), green, thickness)
        cv.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), green, thickness)
        break

    cv.imshow("Threshold", threshold)
    cv.imshow("gray roi", gray_roi)
    cv.imshow("roi", roi)

    if cv.waitKey(60) & 0xFF == 27:
        break

video.release()
cv.destroyAllWindows()

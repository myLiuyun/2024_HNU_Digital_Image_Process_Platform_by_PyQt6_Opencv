# name:Gong Xiaoyv
# Time  2024-05-16   1:19

import cv2
from PyQt6.QtWidgets import QWidget,QGridLayout,QPushButton,QGroupBox,QRadioButton
import numpy as np
from src.Components.ComponentObjects.MorphologyComponent.MorphologyComponent import MorphologyComponent

class EdgeComponent(MorphologyComponent):
    name = 'EdgeComponent'
    detail = '边缘检测，膨胀-收缩'
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlWidget = self.basicControlWidget


    def processImage(self, image: np.array) -> np.ndarray:
        height, width, channels = image.shape
        if channels == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        elif channels == 4:
            gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
        else:
            raise Exception("un valid channel number")

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        dilate_img = cv2.dilate(gray, kernel)
        erode_img = cv2.erode(gray, kernel)
        absdiff_img = cv2.absdiff(dilate_img, erode_img)
        # 对绝对差值图像进行阈值处理，将大于40的像素值设为255，小于40的像素值设为0。
        retval, threshold_img = cv2.threshold(absdiff_img, 40, 255, cv2.THRESH_BINARY)
        # 对阈值处理后的图像进行取反操作。
        result = cv2.bitwise_not(threshold_img)
        result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGRA)
        return result

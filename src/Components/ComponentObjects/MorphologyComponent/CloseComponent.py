# name:Gong Xiaoyv
# Time  2024-05-16   0:28

import cv2
from PyQt6.QtWidgets import QWidget,QGridLayout,QPushButton,QGroupBox,QRadioButton
import numpy as np
from src.Components.ComponentObjects.MorphologyComponent.MorphologyComponent import MorphologyComponent

from typing import List

class CloseComponent(MorphologyComponent):
    name = "CloseComponent"
    detail = "形态学处理：闭操作"
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlWidget = self.basicControlWidget

    def processImage(self, image: np.array) -> np.ndarray:
        height, width, channels = image.shape
        if channels == 3:
            gray = cv2.cvtColor(image, cv.COLOR_BGR2GRAY)
        elif channels == 4:
            gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
        else:
            raise Exception("un valid channel number")
        ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        # 模板/结构元素
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        dst1 = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)  # 参数，第二个为开操作
        dst1 = cv2.cvtColor(dst1, cv2.COLOR_GRAY2BGRA)
        return dst1

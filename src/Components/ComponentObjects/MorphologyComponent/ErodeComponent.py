# name:Gong Xiaoyv
# Time  2024-05-16   1:01

import cv2
from PyQt6.QtWidgets import QWidget,QGridLayout,QPushButton,QGroupBox,QRadioButton
import numpy as np
from src.Components.ComponentObjects.MorphologyComponent.MorphologyComponent import MorphologyComponent

from typing import List

class ErodeComponent(MorphologyComponent):
    name = 'ErodeComponent'
    detail = '腐蚀操作, kernel_size=5'
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
        ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        ans = super().erode(binary, kernel_size=5, iterations=1)
        ans = cv2.cvtColor(ans, cv2.COLOR_GRAY2BGRA)
        return ans
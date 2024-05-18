# name:Gong Xiaoyv
# Time  2024-05-07   19:58

import cv2
import numpy as np

from src.Image import Image
from src.Components.Component import Component
from PyQt6.QtCore import pyqtSignal

class SketchComponent(Component):
    name = "Sketch Effect Component"
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlWidget = self.basicControlWidget

    def processImage(self, image) -> Image:
        src = image
        h, w = src.shape[:2]
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        # 存储处理后图像
        # 反色
        temp = 255 - gray
        # 高斯滤波
        gauss = cv2.GaussianBlur(temp, (21, 21), 0)
        # 再反色
        inverGauss = 255 - gauss
        # 结果转为三通道
        ans = cv2.divide(gray, inverGauss, scale=127.0)
        ans = cv2.cvtColor(ans, cv2.COLOR_GRAY2BGR)
        return ans
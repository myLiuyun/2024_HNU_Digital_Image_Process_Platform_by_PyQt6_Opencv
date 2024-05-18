# name:Gong Xiaoyv
# Time  2024-05-07   20:03

import cv2
import numpy as np

from src.Image import Image
from src.Components.Component import Component
from PyQt6.QtCore import pyqtSignal

class OldComponent(Component):
    name = "Old Effect Component"
    detail = "老照片效果"
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlWidget = self.basicControlWidget

    def processImage(self, image) -> Image:
        src = image
        h, w = src.shape[:2]
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        # 存储处理后图像
        oldImg = np.zeros((h, w, 3), np.uint8)
        for i in range(h):
            for j in range(w):
                b = 0.272 * src[i, j][2] + 0.534 * src[i, j][1] + 0.131 * src[i, j][0]
                g = 0.349 * src[i, j][2] + 0.686 * src[i, j][1] + 0.168 * src[i, j][0]
                r = 0.393 * src[i, j][2] + 0.769 * src[i, j][1] + 0.189 * src[i, j][0]
                if b > 255:
                    b = 255
                if g > 255:
                    g = 255
                if r > 255:
                    r = 255
                oldImg[i, j] = np.uint8((b, g, r))
        return oldImg
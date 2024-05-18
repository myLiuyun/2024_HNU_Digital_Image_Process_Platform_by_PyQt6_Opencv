# name:Gong Xiaoyv
# Time  2024-05-07   17:16

import cv2
import numpy as np

from src.Image import Image
from src.Components.Component import Component


class GlassComponent(Component):
    name = "Glass Effect Component"
    detail = "毛玻璃特效"
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlWidget = self.basicControlWidget

    def processImage(self, image) -> Image:
        src = image
        if image.shape[2] == 4:
            src = cv2.cvtColor(src, cv2.COLOR_BGRA2BGR)
        h, w = src.shape[:2]
        # 存储处理后图像
        glassImg = np.zeros((h, w, 3), np.uint8)
        for i in range(h - 6):
           for j in range(w - 6):
               index = int(np.random.random() * 6)
               glassImg[i, j] = src[i + index, j + index]
        glassImg = cv2.cvtColor(glassImg, cv2.COLOR_BGR2BGRA)
        return glassImg
# name:Gong Xiaoyv
# Time  2024-05-07   19:06

import cv2
import numpy as np

from src.Image import Image
from src.Components.Component import Component


class ReliefComponent(Component):
    name = "Relief Effect Component"
    detail = "浮雕效果。先进行边缘查找，再做增强。边缘为白，其余为灰"
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlWidget = self.basicControlWidget

    def processImage(self, image) -> Image:
        src = image
        h, w = src.shape[:2]
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        # 存储处理后图像
        reliefImg = np.zeros((h, w, 1), np.uint8)
        for i in range(h):
            for j in range(w - 1):
                # 以y方向的相邻像素差作边界查找
                edge = int(gray[i, j]) - int(gray[i, j + 1])
                # 所有像素增加120的灰度
                val = edge + 120
                if val > 255:
                    val = 255
                if val < 0:
                    val = 0
                reliefImg[i, j] = val
        # 转为三通道
        reliefImg = cv2.cvtColor(reliefImg, cv2.COLOR_GRAY2BGR)
        return reliefImg
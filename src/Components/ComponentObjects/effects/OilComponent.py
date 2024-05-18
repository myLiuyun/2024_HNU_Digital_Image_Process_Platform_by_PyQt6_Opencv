# name:Gong Xiaoyv
# Time  2024-05-07   19:32

import cv2
import numpy as np

from src.Image import Image
from src.Components.Component import Component


class OilComponent(Component):
    name = "Oil Effect Component"
    detail = "油画效果"
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlWidget = self.basicControlWidget

    def processImage(self, image) -> Image:
        src = image
        h, w = src.shape[:2]
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        # 存储处理后图像
        oilImg = np.zeros((h, w, 3), np.uint8)
        for i in range(2, h - 2):
            for j in range(2, w - 2):
                quant = np.zeros(8, np.uint8)
                # Kernel 5*5
                for k in range(-2, 2):
                    for t in range(-2, 2):
                        # 将灰度分为8个等级，计算这个像素点处于哪一级
                        level = int(gray[i + k, j + t] / 32)
                        # 灰度等级为level的像素点个数为quant[level]
                        quant[level] = quant[level] + 1
                # 最多像素点数量的像素等级, 的像素数量
                valMax = max(quant)
                # 最多像素点数量的像素等级
                valIndex = list(quant).index(valMax)
                for k in range(-2, 2):
                    for t in range(-2, 2):
                        if gray[i + k, j + t] >= (valIndex * 32) and gray[i + k, j + t] <= (
                                (valIndex + 1) * 32):
                            (b, g, r) = src[i + k, j + t]
                oilImg[i, j] = (b, g, r)
        return oilImg
# name:Gong Xiaoyv
# Time  2024-05-07   19:54

import numpy as np

from src.Image import Image
from src.Components.Component import Component


class MaskComponent(Component):
    name = "Mask Effect Component"
    detail = "马赛克效果"

    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlWidget = self.basicControlWidget

    def processImage(self, image) -> Image:
        src = image
        h, w = src.shape[:2]
        # 存储处理后图像
        maskImg = np.zeros((h, w, 3), np.uint8)
        for i in range(h - 5):
            for j in range(w - 5):
                if i % 5 == 0 and j % 5 == 0:
                    # 以该像素为起点，进行马赛克化
                    for k in range(5):
                        for t in range(5):
                            # 将右下的5*5个像素的值，设置为和现在相等
                            (b, g, r) = src[i, j]
                            maskImg[i + k, j + t] = (b, g, r)
        return maskImg
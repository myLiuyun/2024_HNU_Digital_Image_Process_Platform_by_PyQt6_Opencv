# name:Gong Xiaoyv
# Time  2024-05-07   20:13

import math
import numpy as np

from src.Image import Image
from src.Components.Component import Component


class FleetComponent(Component):
    name = "Fleet Effect Component"
    detail = "流年特效"
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlWidget = self.basicControlWidget

    def processImage(self, image) -> Image:
        src = image
        h, w = src.shape[:2]
        # 存储处理后图像
        fleetImg = np.zeros((h, w, 3), np.uint8)
        for i in range(h):
            for j in range(0, w):
                b = math.sqrt(src[i, j][0]) * 14
                g = src[i, j][1]
                r = src[i, j][2]
                if b > 255:
                    b = 255
                fleetImg[i, j] = np.uint8((b, g, r))
        return fleetImg
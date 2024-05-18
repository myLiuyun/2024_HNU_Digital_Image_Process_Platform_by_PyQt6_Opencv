# name:Gong Xiaoyv
# Time  2024-05-13   18:36

import cv2
import numpy as np

from src.Components.Component import Component
from src.Components.ComponentWidgets.BoxFilterComponentWidget import BoxFilterComponentWidget


class BoxFilterComponent(Component):
    name = 'BoxFilterComponent'
    detail = "可以读取自定义的filter"
    def __init__(self,parent=None):
        super().__init__(parent)
        self.controlWidget = BoxFilterComponentWidget()
        """连接信号和槽"""
        self.controlWidget.filterUpdateSignal.connect(self.componentAttributeUpdate)

    def processImage(self, image:np.array)->np.ndarray:
        filter = self.controlWidget.getFilterSumOne()
        src = image
        if image.shape[2] == 4:
            src = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        processed = cv2.filter2D(src, -1, filter)
        if processed.shape[2]==3:
            processed = cv2.cvtColor(processed, cv2.COLOR_BGR2BGRA)
        return processed


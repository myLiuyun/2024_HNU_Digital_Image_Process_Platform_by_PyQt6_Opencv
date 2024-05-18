# name:Gong Xiaoyv
# Time  2024-05-13   18:38

import cv2
import numpy as np

from src.Components.Component import Component
from src.Components.ComponentWidgets import SortedFilterComponentWidget

from typing import List

class SortedFilterComponent(Component):
    name= 'Sorted Filter Component'
    detail = "排序滤波器"
    def __init__(self,parent=None):
        super().__init__(parent)
        self.controlWidget = SortedFilterComponentWidget.SortedFilterComponentWidget()
        # MaxFilter/ MinFilter/ MidFilter
        self.filterType = "MaxFilter"
        self.KernelSize = 3

        """信号和槽"""
        self.controlWidget.ui.enableButton.toggled.connect(self.setEnabel)
        self.controlWidget.ui.max.toggled.connect(self.setFilterTypeMax)
        self.controlWidget.ui.mid.toggled.connect(self.setFilterTypeMid)
        self.controlWidget.ui.min.toggled.connect(self.setFilterTypeMin)
        self.controlWidget.ui.spinBox.valueChanged.connect(self.updateKernelSize)

    def processImage(self, image:np.array)->np.ndarray:
        if len(image.shape)<3:
            raise Exception("need channel = 3 image, channel is null")

        height, width, channel = image.shape
        src = image
        if channel==4:
            src = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
            channel=3
        src = np.float32(src)
        processed = np.float32(np.zeros_like(src))
        padding = self.KernelSize // 2
        # 进行滤波
        for c in range(channel):
            for y in range(height):
                for x in range(width):
                    neighbors = []
                    # 遍历周围的像素，加到neighbor里面
                    for j in range(-padding, padding + 1):
                        for i in range(-padding, padding + 1):
                            if 0 <= x + i < width and 0 <= y + j < height:
                                neighbors.append(src[y + j, x + i, c])
                    # 根据判别准则，从neighbor中返回应该填充的像素
                    processed[y,x,c] = self.getPixFromNeighbor(neighbors)
        processed = processed.astype(np.uint8)
        processed = cv2.cvtColor(processed, cv2.COLOR_BGR2BGRA)
        return processed

    def getPixFromNeighbor(self, neighbor:List[int]) -> int:
        if self.filterType == "MaxFilter":
            return max(neighbor)
        elif self.filterType == "MinFilter":
            return min(neighbor)
        elif self.filterType == "MidFilter":
            sorted_lst = sorted(neighbor)
            n = len(sorted_lst)
            # 如果列表长度为奇数，中位数为中间值
            if n % 2 == 1:
                return sorted_lst[n // 2]
            # 如果列表长度为偶数，中位数为中间两个数的平均值
            else:
                mid_right = n // 2
                mid_left = mid_right - 1
                return (sorted_lst[mid_left] + sorted_lst[mid_right]) / 2

    def updateKernelSize(self, kernelSize):
        self.KernelSize = kernelSize
        self.componentAttributeUpdate.emit()

    def updateFilterType(self, filterType):
        self.filterType = filterType
        self.componentAttributeUpdate.emit()

    def setFilterTypeMax(self):
        self.updateFilterType("MaxFilter")
    def setFilterTypeMin(self):
        self.updateFilterType("MinFilter")
    def setFilterTypeMid(self):
        self.updateFilterType("MidFilter")
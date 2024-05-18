# name:Gong Xiaoyv
# Time  2024-05-15   20:34

from src.Components.ComponentObjects.FilterComponent.SortedFilterComponent import SortedFilterComponent
import cv2
from PyQt6.QtWidgets import QWidget,QGridLayout,QPushButton,QGroupBox,QRadioButton
import numpy as np
from src.Components.ComponentWidgets.TrimmedSortedFilterWidget import TrimmedSortedFilterWidget

from typing import List

class TrimmedSortedFilter(SortedFilterComponent):
    name = 'TrimmedSortedFilter'
    detail = '修正后的算数均值滤波'
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlWidget = TrimmedSortedFilterWidget()
        self.d = 4

        """信号和槽"""
        self.controlWidget.ui.enableButton.toggled.connect(self.setEnabel)
        self.controlWidget.ui.max.toggled.connect(self.setFilterTypeMax)
        self.controlWidget.ui.mid.toggled.connect(self.setFilterTypeMid)
        self.controlWidget.ui.min.toggled.connect(self.setFilterTypeMin)
        self.controlWidget.ui.k.valueChanged.connect(self.updateKernelSize)
        self.controlWidget.ui.b.valueChanged.connect(self.setB)

    def processImage(self, image: np.array) -> np.ndarray:
        return super().processImage(image)

    def getPixFromNeighbor(self, neighbor:List[int]) -> int:
        """修改根据相邻像素计算当前像素的规则"""
        neighbor = sorted(neighbor)
        if len(neighbor) > self.d:
            num = (self.d-1) // 2
            neighbor = neighbor[num : -num]

        return sum(neighbor)/len(neighbor)

    def setB(self,value:int):
        self.d = value
        self.componentAttributeUpdate.emit()
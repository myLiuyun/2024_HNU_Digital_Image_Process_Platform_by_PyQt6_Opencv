# name:Gong Xiaoyv
# Time  2024-05-14   1:33
import cv2

from src.Image import Image
from src.Components.ComponentObjects.FrequencyDomainFiltersComponent.FrequencyFilterComponent import FrequencyFilterComponent
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QRadioButton, QGroupBox
import numpy as np
import math

class BandFilterComponent(FrequencyFilterComponent):
    name = 'Frequency Band Filter Component'
    detail = '频率域条带滤波器，实现高通低通'

    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlWidget.ui.par1Label.setText("breadth")
        self.controlWidget.ui.par2Label.setText("radius")

        self.breadth = 64  # parameter 1
        self.radius = 32  # parameter 2
        """信号和槽"""
        self.controlWidget.ui.par1Val.valChanged.connect(self.setBreadth)
        self.controlWidget.ui.par2Val.valChanged.connect(self.setRadius)


    def processImage(self, image:np.array)->np.ndarray:
        if image.shape[2] == 3:
            [b,g,r] = cv2.split(image)
        elif image.shape[2] == 4:
            [b,g,r,a] = cv2.split(image)
        else:
            raise Exception("channel not valid")
        if self.filterType == 'High':
            pb = self.BandHighPassFilter(super().preFFT(b))
            pg = self.BandHighPassFilter(super().preFFT(g))
            pr = self.BandHighPassFilter(super().preFFT(r))
        elif self.filterType == 'Low':
            pb = self.BandLowPassFilter(super().preFFT(b))
            pg = self.BandLowPassFilter(super().preFFT(g))
            pr = self.BandLowPassFilter(super().preFFT(r))
        else:
            raise Exception("filter type not valid")

        pb = super().iFFT(pb).astype(np.uint8)
        pg = super().iFFT(pg).astype(np.uint8)
        pr = super().iFFT(pr).astype(np.uint8)

        if image.shape[2] == 3:
            result = cv2.merge((pb,pg,pr))
            result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
        else :
            result = cv2.merge((pb,pg,pr,a))

        return result


    def BandLowPassFilter(self, dtf_img):
        shape = dtf_img.shape
        height = shape[0]
        mid_height = int(height / 2)
        wight = shape[1]
        mid_wight = int(wight / 2)
        mask = np.zeros((height, wight, 2), np.float32)
        for i in range(0, height):
            for j in range(0, wight):
                # 计算(i, j)到中心点的距离
                d = math.sqrt(pow(i - mid_height, 2) + pow(j - mid_wight, 2))
                if self.radius - self.breadth / 2 < d < self.radius + self.breadth / 2:
                    mask[i, j, 0] = mask[i, j, 1] = 1
        #showImg(mask[:,:,0])
        return dtf_img * mask


    def BandHighPassFilter(self, dtf_img):
        shape = dtf_img.shape
        height = shape[0]
        mid_height = int(height / 2)
        wight = shape[1]
        mid_wight = int(wight / 2)
        mask = np.ones((height, wight, 2), np.float32)
        for i in range(0, height):
            for j in range(0, wight):
                # 计算(i, j)到中心点的距离
                d = math.sqrt(pow(i - mid_height, 2) + pow(j - mid_wight, 2))
                if self.radius - self.breadth / 2 < d < self.radius + self.breadth / 2:
                    mask[i, j, 0] = mask[i, j, 1] = 0
        # showImg(mask[:,:,0])
        return dtf_img * mask



    def setBreadth(self, val:int):
        self.breadth = val
        self.componentAttributeUpdate.emit()

    def setRadius(self, val:int):
        self.radius = val
        self.componentAttributeUpdate.emit()
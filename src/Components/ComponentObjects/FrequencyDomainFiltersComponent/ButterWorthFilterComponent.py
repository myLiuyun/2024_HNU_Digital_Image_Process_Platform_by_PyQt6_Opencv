# name:Gong Xiaoyv
# Time  2024-05-14   2:31
import math

import cv2
import numpy as np

from PyQt6.QtCore import pyqtSignal
from src.Components.ComponentObjects.FrequencyDomainFiltersComponent.FrequencyFilterComponent import FrequencyFilterComponent

class ButterWorthFilterComponent(FrequencyFilterComponent):
    name = 'Frequency Butter Worth Filter'
    detail = '频率域条带滤波器，实现高通低通'

    def __init__(self,parent=None):
        super().__init__(parent)
        self.controlWidget.ui.par2Val.setMax(5)
        self.controlWidget.ui.par1Val.setVal(64)
        self.controlWidget.ui.par2Val.setVal(2)

        self.d0 = 64  # par1
        self.order = 2 # par2
        self.wight = 1 # c

        """信号和槽"""
        self.controlWidget.ui.par1Val.valChanged.connect(self.setD0)
        self.controlWidget.ui.par2Val.valChanged.connect(self.setOrder)

    def processImage(self, image:np.array)->np.ndarray:
        if image.shape[2] == 3:
            [b,g,r] = cv2.split(image)
        elif image.shape[2] == 4:
            [b,g,r,a] = cv2.split(image)
        else:
            raise Exception("channel not valid")
        if self.filterType == 'High':
            pb = self.ButterWorthHighPassFliter(super().preFFT(b))
            pg = self.ButterWorthHighPassFliter(super().preFFT(g))
            pr = self.ButterWorthHighPassFliter(super().preFFT(r))
        elif self.filterType == 'Low':
            pb = self.ButterWorthLowPassFliter(super().preFFT(b))
            pg = self.ButterWorthLowPassFliter(super().preFFT(g))
            pr = self.ButterWorthLowPassFliter(super().preFFT(r))
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


    def ButterWorthLowPassFliter(self, dtf_img:np.ndarray)->np.ndarray:
        shape = dtf_img.shape
        height = shape[0]
        mid_height = int(height / 2)
        wight = shape[1]
        mid_wight = int(wight / 2)
        mask = np.zeros((height, wight, 2), np.float32)

        for i in range(height):
            for j in range(wight):
                d = math.sqrt(pow(i - mid_height, 2) + pow(j - mid_wight, 2))
                try:
                    mask[i, j, :] = 1 / (1 + self.wight * pow(d / self.d0, 2 * self.order))
                except ZeroDivisionError:
                    mask[i, j, :] = 0
        # showImg(mask[:,:,0])
        return dtf_img * np.float32(mask)

    def ButterWorthHighPassFliter(self, dtf_img:np.ndarray)->np.ndarray:
        shape = dtf_img.shape
        height = shape[0]
        mid_height = int(height / 2)
        wight = shape[1]
        mid_wight = int(wight / 2)
        mask = np.zeros((height, wight, 2), np.float32)

        for i in range(height):
            for j in range(wight):
                d = math.sqrt(pow(i - mid_height, 2) + pow(j - mid_wight, 2))
                try:
                    mask[i, j, :] = 1-(1 / (1 + self.wight * pow(d / self.d0, 2 * self.order)))
                except ZeroDivisionError:
                    mask[i, j, :] = 1
        # showImg(mask[:,:,0])
        return dtf_img * np.float32(mask)

    def setD0(self, val:int):
        self.d0 = val
        self.componentAttributeUpdate.emit()

    def setOrder(self, val:int):
        self.order = val
        self.componentAttributeUpdate.emit()
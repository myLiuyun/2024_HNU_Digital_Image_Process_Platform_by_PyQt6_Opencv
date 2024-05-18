# name:Gong Xiaoyv
# Time  2024-05-13   14:52

"""
直方图均衡化
"""
import cv2
import numpy as np

from src.Components.Component import Component
from PyQt6.QtWidgets import QWidget

class HistogramEqualizationComponent(Component):
    name = "Histogram Equalization Component"
    detail = "直方图均衡化，针对每一个通道，进行均衡化，不包括Alpha通道"

    def __init__(self,parent=None):
        super().__init__(parent)
        self.controlWidget = self.basicControlWidget

    def processImage(self, image:np.array)->np.ndarray:
        h, w, channel = image.shape
        processed = np.zeros_like(image)

        if channel == 4:
            (b, g, r, a) = cv2.split(image)
            bH = cv2.equalizeHist(b)
            gH = cv2.equalizeHist(g)
            rH = cv2.equalizeHist(r)
            # 合并每一个通道
            processed = cv2.merge((bH, gH, rH, a))
        elif channel == 3:
            (b, g, r) = cv2.split(image)
            bH = cv2.equalizeHist(b)
            gH = cv2.equalizeHist(g)
            rH = cv2.equalizeHist(r)
            # 合并每一个通道
            processed = cv2.merge((bH, gH, rH))
            processed = cv2.cvtColor(processed, cv2.COLOR_BGR2BGRA)
        return processed

    def histogramEqualization(self,image:np.array)->np.ndarray:
        """
        针对单通道image，进行直方图均衡化
        1. 统计频率
        2. 计算累计频率
        3. 计算映射关系
        4. 进行映射，返回映射后的图像
        """
        if len(image.shape)!=2:
            raise Exception("histogramEqualization: Image shape error")


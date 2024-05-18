# name:Gong Xiaoyv
# Time  2024-05-15   23:46

import cv2
from PyQt6.QtWidgets import QWidget,QGridLayout,QPushButton,QGroupBox,QRadioButton
import numpy as np
from src.Components.Component import Component

from typing import List

class MorphologyComponent(Component):
    def __init__(self, parent=None):
        super().__init__(parent)

    def dilate (self,image, kernel_size=3, iterations=1):
        """膨胀操作"""
        # 构造一个矩形结构元素（kernel）
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        # 对图像进行膨胀操作 iterations：膨胀次数
        dilated_image = cv2.dilate(image, kernel, iterations=iterations)
        return dilated_image

    def erode(self, image, kernel_size=3, iterations=1):
        """腐蚀操作"""
        # 构造一个矩形结构元素（kernel）
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        # 对图像进行腐蚀操作
        eroded_image = cv2.erode(image, kernel, iterations=iterations)
        return eroded_image
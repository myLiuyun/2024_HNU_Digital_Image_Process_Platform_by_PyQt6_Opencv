# name:Gong Xiaoyv
# Time  2024-05-14   4:03


import cv2

from src.Image import Image
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QRadioButton, QGroupBox
import numpy as np
import math
from src.Components.ComponentObjects.ImageCaculateComponent.ImageCaculateComponent import ImageCaculateComponent

class AddImageComponent(ImageCaculateComponent):
    name = 'Add Image Component'
    detail = '实现了两张图片相加'

    def __init__(self, parent=None):
        super().__init__(parent)

    def processImage(self, image:np.array)->np.ndarray:
        return super().processImage(image)

    def caculatePix(self, sourcePix, otherPix):
        # print('caculatePix')
        return sourcePix * 0.5 + otherPix * 0.5
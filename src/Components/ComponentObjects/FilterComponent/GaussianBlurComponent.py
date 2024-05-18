# name:Gong Xiaoyv
# Time  2024-05-06   19:43
import cv2
import numpy as np

from src.Image import Image
from src.Components.Component import Component
from src.Components.ComponentWidgets.GaussianBlurComponentWidget import GaussianBlurComponentWidget


class GaussianBlurComponent(Component):
    name = "GaussianBlur Component"
    detail = "高斯滤波"
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlWidget = GaussianBlurComponentWidget()
        self.ksize = [5,5]
        """连接信号和槽"""
        self.controlWidget.ui.enableButton.toggled.connect(self.setEnabel)
        self.controlWidget.ui.kernal_x.valueChanged.connect(self.setKx)
        self.controlWidget.ui.kernal_y.valueChanged.connect(self.setKy)

    def processImage(self, image:Image)->np.ndarray:
        blurred = cv2.GaussianBlur(image, self.ksize,sigmaX=0, sigmaY=0)
        return blurred

    def updateKernalSize(self, kernal_x:int = -1, kernal_y:int = -1)->None:
        if kernal_x != -1:
            self.ksize[0] = kernal_x
        if kernal_y != -1:
            self.ksize[1] = kernal_y
        self.componentAttributeUpdate.emit()

    def setKx(self, x:int)->None:
        self.updateKernalSize(kernal_x=x)
    def setKy(self, y:int)->None:
        self.updateKernalSize(kernal_y=y)

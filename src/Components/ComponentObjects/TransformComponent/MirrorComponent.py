# name:Gong Xiaoyv
# Time  2024-05-14   8:55


"""
实现图像镜像
"""
from src.Components.Component import Component
import cv2
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QWidget,QGridLayout,QPushButton,QGroupBox,QRadioButton
from src.Image import Image
from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtWidgets
import numpy as np
from src.Components.ComponentWidgets.MirrorComponentWidget import MirrorComponentWidget

class MirrorComponent(Component):
    name = 'MirrorComponent'
    detail = '镜像功能，水平镜像'
    def __init__(self,parent=None):
        super(MirrorComponent,self).__init__(parent)
        self.controlWidget = MirrorComponentWidget()
        self.x = True
        self.y = False
        """信号和槽"""
        self.controlWidget.ui.enable.toggled.connect(self.setEnabel)
        self.controlWidget.ui.x.toggled.connect(self.setX)
        self.controlWidget.ui.y.toggled.connect(self.setY)

    def processImage(self, image:np.array)->np.ndarray:
        dst = np.zeros_like(image)
        if self.x and not self.y:
            cv2.flip(image,0, dst)
        if not self.x and self.y:
            cv2.flip(image,1, dst) # 围绕y
        if self.x and self.y:
            cv2.flip(image, -1, dst)
        return dst

    def setX(self, val:bool):
        self.x = val
        self.componentAttributeUpdate.emit()
    def setY(self, val:bool):
        self.y = val
        self.componentAttributeUpdate.emit()

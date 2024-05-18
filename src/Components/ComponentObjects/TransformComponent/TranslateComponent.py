# name:Gong Xiaoyv
# Time  2024-05-15   11:26
from src.Components.Component import Component
import cv2
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QWidget,QGridLayout,QPushButton,QGroupBox,QRadioButton
from src.Image import Image
from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtWidgets
import numpy as np
from src.Components.ComponentWidgets.TransformComponentWidget import TransformComponentWidget
"""
利用cv2.warpAffine()，实现仿射变换
cv2.warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) → dst
参数：
    src - 输入图像。
    M - 变换矩阵。
    dsize - 输出图像的大小。
    flags - 插值方法的组合（int 类型！）
    borderMode - 边界像素模式（int 类型！）
    borderValue - （重点！）边界填充值; 默认情况下，它为0。
"""

class TransformComponent(Component):
    name = 'TransformComponent'
    detail = "进行简单的空间变换"
    def __init__(self,parent=None):
        super().__init__(parent)
        self.controlWidget = TransformComponentWidget()
        # 平移变换
        self.translationX = 20
        self.translationY = 20
        # 旋转变换,单位为角度，中心为图像中心
        self.rotation = 0
        # 缩放变换
        self.scaleX = 1
        self.scaleY = 1
        """信号和槽"""
        self.controlWidget.ui.enable.toggled.connect(self.setEnabel)
        self.controlWidget.ui.tranX.valueChanged.connect(self.setTranX)
        self.controlWidget.ui.tranY.valueChanged.connect(self.setTransY)
        self.controlWidget.ui.rotate.valueChanged.connect(self.setRotation)
        self.controlWidget.ui.scaleX.valueChanged.connect(self.setScaleX)
        self.controlWidget.ui.scaleY.valueChanged.connect(self.setScaleY)

    def processImage(self, image:np.array)->np.ndarray:
        h,w = image.shape[:2]
        mat = self.getTranformMatrix()
        processed = np.zeros_like(image)
        processed = cv2.warpAffine(image, mat,(w,h))

        # self.showImageOpenCv(processed)

        return processed

    def getTranformMatrix(self):
        translateMat = np.array([[1,0,self.translationX],
                                 [0,1,self.translationY],
                                 [0,0,1]],dtype=np.float32)
        cos = np.cos(self.rotation * np.pi / 180)
        sin = np.sin(self.rotation * np.pi / 180)
        RatateMat = np.array([[cos,-sin,0],
                              [sin,cos,0],
                              [0,0,1]],dtype=np.float32)
        zoomMat = np.array([[self.scaleX,0,0],
                            [0,self.scaleY,0],
                            [0,0,1]],dtype=np.float32)
        ans = translateMat.dot(RatateMat).dot(zoomMat)
        ans = ans/ans[2, 2]
        ans = ans[:-1,:]

        return ans

    def setTranX(self,value):
        self.translationX = value
        self.componentAttributeUpdate.emit()

    def setTransY(self,value):
        self.translationY = value
        self.componentAttributeUpdate.emit()

    def setRotation(self,value):
        self.rotation = value
        self.componentAttributeUpdate.emit()

    def setScaleX(self, value):
        print(f"scale x ={value}")
        self.scaleX = value
        self.componentAttributeUpdate.emit()

    def setScaleY(self,value):
        self.scaleY = value
        self.componentAttributeUpdate.emit()
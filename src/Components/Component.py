# name:Gong Xiaoyv
# Time  2024-05-06   19:36
import cv2
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QWidget,QGridLayout,QPushButton,QGroupBox,QRadioButton
from src.Image import Image
from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtWidgets
import numpy as np

class Component(QObject):
    """属性更新"""
    componentAttributeUpdate = pyqtSignal()
    name = "Component"
    def __init__(self, parent=None):
        super(Component, self).__init__(parent)
        self.controlWidget = QWidget()
        """初始化Ui"""
        self.basicControlWidget = QWidget()
        self.basicControlWidget.resize(320, 129)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.basicControlWidget)
        self.enableButton = QRadioButton(parent=self.basicControlWidget)
        self.enableButton.setChecked(True)
        self.enableButton.setObjectName("enableButton")
        self.enableButton.setText("是否启用")
        self.horizontalLayout.addWidget(self.enableButton)
        # self.basicControlWidget.show()

        # 设置布局
        self.controlWidget.setLayout(self.horizontalLayout)
        self.basicControlWidget.setLayout(self.horizontalLayout)
        """初始化属性"""
        self.enable = True
        """信号和槽"""
        self.enableButton.toggled.connect(self.setEnabel)
        self.enableButton.clicked.connect(self.componentAttributeUpdate)

    def processImage(self, image:np.array)->np.ndarray:
        pass

    def getName(self):
        return self.name

    def setEnabel(self, enable:bool):
        print("component set enable")
        self.enable = enable
        self.componentAttributeUpdate.emit()

    def showImageOpenCv(self, image):
        cv2.imshow(self.name, image)
        cv2.waitKey(0)
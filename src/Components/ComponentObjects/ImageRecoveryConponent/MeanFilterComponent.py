# name:Gong Xiaoyv
# Time  2024-05-15   17:41
"""
使用均值
"""
from src.Components.Component import Component
import cv2
from PyQt6.QtWidgets import QWidget,QGridLayout,QPushButton,QGroupBox,QRadioButton
import numpy as np
from src.Components.ComponentWidgets.MeanFilterComponentWidget import MeanFilterComponentWidget
class MeanFilterComponent(Component):
    name = 'MeanFilterComponent'
    detail = "均值滤波器，可选算数均值、几何均值、谐波、逆谐波"

    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlWidget = MeanFilterComponentWidget()
        # arithmetic / geometric / harmonic / contra_harmonic
        self.filterType = "arithmetic"
        self.KernelSize = 3
        self.q = 1  # 逆谐波均值滤波器的阶数
        """信号和槽"""
        self.controlWidget.ui.enable.toggled.connect(self.setEnabel)
        self.controlWidget.ui.arithmetic.toggled.connect(self.setFilterTypeArithmetic)
        self.controlWidget.ui.geometric.toggled.connect(self.setFilterTypeGeometric)
        self.controlWidget.ui.harmonic.toggled.connect(self.setFilterTypeHarmonic)
        self.controlWidget.ui.contra_harmonic.toggled.connect(self.setFilterTypeContraHarmonic)
        self.controlWidget.ui.K.valueChanged.connect(self.setKernelSize)
        self.controlWidget.ui.Q.valueChanged.connect(self.setQ)

    def processImage(self, image: np.array) -> np.ndarray:
        # 转化为RGB通道
        src = image
        if image.shape[2]==4:
            src = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        if self.filterType == "arithmetic":
            processed = cv2.blur(src, (self.KernelSize, self.KernelSize))
        elif self.filterType == "geometric":
            """
            先取Log再进行卷积，最后将结果取E
            """
            img_log = np.log1p(src.astype(np.float64))
            img_sum = cv2.boxFilter(img_log, ddepth=-1, ksize=(self.KernelSize, self.KernelSize))
            img_exp = np.expm1(img_sum)
            processed = img_exp.astype(src.dtype)
        elif self.filterType == "harmonic":
            """
            谐波滤波器
            """
            img_reciprocal = 1.0 / (src.astype(np.float64) + 1e-10)  # 防止除以0
            img_sum = cv2.boxFilter(img_reciprocal, ddepth=-1, ksize=(self.KernelSize, self.KernelSize))
            img_harmonic = 1.0 / (img_sum + 1e-10)
            processed = img_harmonic.astype(src.dtype)

        elif self.filterType == "contra_harmonic":
            """
            逆谐波滤波器
            """
            # if self.q == 0:
            #     raise ValueError("q cannot be zero for the contra-harmonic mean filter.")

            img_pow1 = np.power(src.astype(np.float64), self.q + 1)
            img_pow2 = np.power(src.astype(np.float64), self.q)

            img_sum1 = cv2.boxFilter(img_pow1, ddepth=-1, ksize=(self.KernelSize, self.KernelSize))
            img_sum2 = cv2.boxFilter(img_pow2, ddepth=-1, ksize=(self.KernelSize, self.KernelSize))

            img_contra_harmonic = img_sum1 / (img_sum2 + 1e-10)  # avoid division by zero
            processed = img_contra_harmonic.astype(image.dtype)
        else:
            raise Exception("no valid filter type")

        processed = cv2.cvtColor(processed, cv2.COLOR_BGR2BGRA)
        return processed

    def setFilterType(self, type):
        self.filterType = type
        self.componentAttributeUpdate.emit()

    def setFilterTypeArithmetic(self):
        self.setFilterType("arithmetic")

    def setFilterTypeGeometric(self):
        self.setFilterType("geometric")

    def setFilterTypeHarmonic(self):
        self.setFilterType("harmonic")

    def setFilterTypeContraHarmonic(self):
        self.setFilterType("contra_harmonic")

    def setKernelSize(self, k):
        self.KernelSize = k
        self.componentAttributeUpdate.emit()

    def setQ(self, q):
        self.q = q
        self.componentAttributeUpdate.emit()
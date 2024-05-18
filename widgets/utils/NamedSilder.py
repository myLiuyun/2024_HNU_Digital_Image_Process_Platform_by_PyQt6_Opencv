# name:Gong Xiaoyv
# Time  2024-05-15   14:09
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QRadioButton
from widgets.NamedSilder import Ui_NamedSilder
import numpy as np
"""
支持精度为0.1的Slider
"""

class NamedSilder(QWidget):
    valueChanged = pyqtSignal(float)

    def __init__(self, parent=None):
        super(NamedSilder, self).__init__(parent)
        self.ui = Ui_NamedSilder()
        self.ui.setupUi(self)
        self.max = 10
        self.min = 0
        self.k = 1  # Slider.value 到 NamedSlider.value 的转换系数，  Named.value = Slider.value / float(k)
        self.value = 0

        self.ui.slider.valueChanged.connect(self.SliderValChanged)

    def setName(self, name):
        self.ui.name.setText(str(name))

    def setValue(self, value):
        """暴露给外部的接口，value直接为Label上的值"""
        value = np.around(value, 1)
        self.value = value
        self.ui.val.setText(str(self.value))
        self.ui.slider.setValue(int(value / self.k))

    def SliderValChanged(self, value):
        """Slot，接收的信号为Slider上的value"""
        self.value = np.around(value * self.k, 1)
        self.ui.val.setText(str(self.value))
        self.valueChanged.emit(self.value)

    def setRangeAndK(self, min, max, k):
        self.setK(k)
        self.setRange(min, max)


    def setRange(self, min, max):
        self.min = min
        self.max = max
        self.ui.slider.setRange(self.min, int(self.max/self.k))

    def setK(self, k):
        k = int(k*10)/10.0
        self.k = k

    def getValue(self):
        return self.value

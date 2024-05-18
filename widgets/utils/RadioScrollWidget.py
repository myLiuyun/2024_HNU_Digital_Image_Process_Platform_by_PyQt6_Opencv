# name:Gong Xiaoyv
# Time  2024-05-09   10:39
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QRadioButton
from widgets.utils.Ui_RadioScrollWidget import Ui_RadioScrollWidget

class RadioScrollWidget(QWidget):
    valChanged = pyqtSignal(int)

    def __init__(self, parent=None, min_val=0, max_val=255):
        super(RadioScrollWidget, self).__init__(parent)
        self.ui = Ui_RadioScrollWidget()
        self.ui.setupUi(self)
        """初始化属性"""
        self.min_val = min_val
        self.max_val = max_val
        self.ui.slider.setRange(self.min_val, self.max_val)
        self.setSliderVla(self.max_val)
        self.setLabelVal(self.max_val)
        """初始化信号和槽"""
        self.ui.radioButton.toggled.connect(self.setSliderVla)
        self.ui.slider.valueChanged.connect(self.setLabelVal)
        self.ui.slider.valueChanged.connect(self.valChanged)

    def getValue(self) -> int:
        return self.ui.slider.value()

    def setSliderVla(self, val:bool):
        if val==False:
            self.ui.slider.setValue(self.min_val)
            self.valChanged.emit(self.min_val)
        else:
            self.ui.slider.setValue(self.max_val)
            self.valChanged.emit(self.max_val)

    def setLabelVal(self, val:int):
        self.ui.val.setText(str(val))

    def setName(self, str):
        self.ui.radioButton.setText(str)

    def setMax(self, val):
        self.ui.slider.setMaximum(val)
        self.ui.val.setText(str(val))
        self.max_val = val

    def setMin(self, val):
        self.ui.slider.setMinimum(val)
        self.ui.val.setText(str(val))
        self.min_val = val

    def setVal(self, val):
        if self.min_val<=val<=self.max_val:
            self.ui.val.setText(str(val))
            self.ui.slider.setValue(val)
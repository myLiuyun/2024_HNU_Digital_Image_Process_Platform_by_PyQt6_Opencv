# name:Gong Xiaoyv
# Time  2024-05-14   10:41
from PyQt6 import QtCore, QtGui, QtWidgets
from widgets.LocalThresholdingComponent import Ui_Form
from PyQt6.QtCore import Qt, pyqtSignal

class LocalThresholdingComponentWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(LocalThresholdingComponentWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
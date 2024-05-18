# name:Gong Xiaoyv
# Time  2024-05-14   11:03

from PyQt6 import QtCore, QtGui, QtWidgets
from widgets.KMeansThresholdingComponentWidget import Ui_KMeansThresholdingComponentWidget
from PyQt6.QtCore import Qt, pyqtSignal

class KMeansThresholdingComponentWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(KMeansThresholdingComponentWidget, self).__init__(parent)
        self.ui = Ui_KMeansThresholdingComponentWidget()
        self.ui.setupUi(self)
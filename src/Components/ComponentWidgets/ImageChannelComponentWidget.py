# name:Gong Xiaoyv
# Time  2024-05-09   10:11

from PyQt6 import QtCore, QtGui, QtWidgets
from widgets.ImageChannelComponentWidget import Ui_ImageChannelComponentWidget
from PyQt6.QtCore import Qt, pyqtSignal

class ImageChannelComponentWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ImageChannelComponentWidget()
        self.ui.setupUi(self)
        self.ui.R.setName("R")
        self.ui.G.setName("G")
        self.ui.B.setName("B")
        self.ui.A.setName("A")
